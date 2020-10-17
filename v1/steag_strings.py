import pandas as pd
import steagsupports_factory


# Classe to create dataframe to string equipment and save in sheet destiny
class Strings:

    @staticmethod
    def calcstrings(frm, periodo, place, destino):
        df = frm.fillna(0.00)
        column = df.columns.values
        files = steagsupports_factory.sheetdestination(destino, periodo, place)
        numberstrings = 0
        for i in range(2, len(column)):
            columnfilter = [column[0], column[1], column[i]]
            df_fin = df.filter(items=columnfilter)
            df_fin = Strings.readframe(df_fin)
            df_fin = df_fin[[column[0], column[i]]]
            df_fin[column[i]] = df_fin[[column[i]]].astype(float)
            labelcolumn = Strings.labelstampstring(place, column[i])
            df_fin.rename(columns={'Date': 'timestamp', column[i]: labelcolumn}, inplace=True)
            namesfile = Strings.stamp2(periodo, column[i], place, 'String')
            sheetname = r'{}\{}.csv'.format(files, namesfile)
            df_fin.to_csv(sheetname, index=False)
            numberstrings += 1
            print('Arquivo "{}" salvo com sucesso!!!'.format(namesfile))

    @staticmethod
    def readframe(df):
        df['Date'] = pd.to_datetime(df['Date'])
        df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
        df['Time'] = pd.to_datetime(df['Time'])
        df['Time'] = df['Time'].dt.strftime('%H:%M:%S')
        df['Date'] = df['Date'] + ' ' + df['Time']
        return df

    @staticmethod
    # Function to create name to each file string
    def stamp2(*args):
        if args[2] == 1:
            namestamp1 = f'Sao Pedro-data-{args[0]}-{args[3]}-{args[1][12:27]}'
            return namestamp1
        elif args[2] == 2:
            namestamp2 = f'Juazeiro-data-{args[0]}-{args[3]}-{args[1][11:43]}'# realizar ajuste
            return namestamp2
        elif args[2] == 3:
            namestamp3 = f'Sol do Futuro-data-{args[0]}-{args[3]}-{args[1][16:52]}'# realizar Ajuste
            return namestamp3

    @staticmethod
    # Function to create label name to each string
    def labelstampstring(*args):
        if args[0] == 1:
            namestamp1 = f'{args[1][30:50]}'
            return namestamp1
        elif args[0] == 2:
            labelstamp2 = f'{args[1][46:66]}'
            return labelstamp2
        elif args[0] == 3:
            labelstamp3 = f'{args[1][55:75]}'
            return labelstamp3
