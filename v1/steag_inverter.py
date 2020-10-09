import pandas as pd
import steagsupports_factory


# Classe to create inverter dataframe and save in sheet destiny
class Inverter:

    @staticmethod
    def calcinverter(frm, periodo, place, destino):
        df = frm.fillna(0.00)
        column = df.columns.values
        lista_plant = Inverter.organizetuplainverter(column)
        files = steagsupports_factory.sheetdestination(destino, periodo, place)
        numberinv = 0
        for i in lista_plant:
            columnfilter = [column[0], column[1], i[0], i[1]]
            df_fin = df.filter(items=columnfilter)
            df_fin = Inverter.readframe(df_fin)
            df_fin = df_fin[[column[0], i[0], i[1]]]
            df_fin.rename(columns={'Date': 'timestamp', i[0]: 'ACTIVE POWER', i[1]: 'COMS STATUS'}, inplace=True)
            namesfile = Inverter.stamp(periodo, i[0], place, 'Inverter')
            sheetname = r'{}\{}.csv'.format(files, namesfile)
            df_fin.to_csv(sheetname, index=False)
            numberinv += 1
            print('Arquivo "{}" salvo com sucesso!!!'.format(namesfile))

    @staticmethod
    # Function to analize data of equipment inverter
    def organizetuplainverter(listcol):
        flag = True
        listdata = []
        lencollumn = len(listcol)
        index1 = 2
        index2 = 3
        while flag:
            collumntupla = (listcol[index1], listcol[index2])
            listdata.append(collumntupla)
            index1 += 2
            index2 += 2
            if index2 > lencollumn:
                flag = False
        return listdata

    @staticmethod
    def readframe(df):
        df['Date'] = pd.to_datetime(df['Date'])
        df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
        df['Time'] = pd.to_datetime(df['Time'])
        df['Time'] = df['Time'].dt.strftime('%H:%M:%S')
        df['Date'] = df['Date'] + ' ' + df['Time']
        return df

    @staticmethod
    def stamp(*args):
        if args[2] == 1:
            namestamp1 = f'Sao Pedro-data-{args[0]}-{args[3]}-{args[1][12:21]}'
            return namestamp1
        elif args[2] == 2:
            namestamp2 = f'Juazeiro-data-{args[0]}-{args[3]}-{args[1][11:22]}'
            return namestamp2
        elif args[2] == 3:
            namestamp3 = f'Sol do Futuro-data-{args[0]}-{args[3]}-{args[1][16:27]}'
            return namestamp3
