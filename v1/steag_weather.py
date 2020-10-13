import pandas as pd
import steagsupports_factory


# Classe to create dataframe to weather station equipment
class Weatherstation:

    @staticmethod
    def calcweather(frm, periodo, place, destino):
        plant = ['Sao Pedro', 'Juazeiro', 'Sol do Futuro']
        df_fin = frm
        df_fin = Weatherstation.readframe(df_fin)
        df_fin = df_fin.fillna(0.00)
        df_fin.rename(columns={'Date': 'timestamp'}, inplace=True)
        del df_fin['Time']
        direct = steagsupports_factory.sheetdestination(destino, periodo, place)
        namestamp = f'{plant[place - 1]}-data-{periodo}-Weather station'
        sheetname = r'{}\{}.csv'.format(direct, namestamp)
        df_fin.to_csv(sheetname, index=False)
        print('Arquivo "{}" salvo com sucesso!!!'.format(namestamp))

    @staticmethod
    def readframe(df):
        df['Date'] = pd.to_datetime(df['Date'])
        df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
        df['Time'] = pd.to_datetime(df['Time'])
        df['Time'] = df['Time'].dt.strftime('%H:%M:%S')
        df['Date'] = df['Date'] + ' ' + df['Time']
        return df