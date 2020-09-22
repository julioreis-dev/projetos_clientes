import pandas as pd
import steagsupports


#caminho-0
#periodo - 1
#choose - 2
#destino - 3


def calcinverter(*args):
    column = steagsupports.organizefiles(args[0])
    lista_plant = steagsupports.organizetupla(column)
    for i in lista_plant:
        df_fin = pd.read_excel(args[0])
        df_fin = df_fin.fillna(0.00)
        df_fin = df_fin[[column[0], i[0], i[1]]]
        df_fin.rename(columns={'Date': 'timestamp', i[0]: 'ACTIVE POWER', i[1]: 'COMS STATUS'}, inplace=True)
        frame = steagsupports.readframe(df_fin)
        filename = steagsupports.stamp(args[1], i[0], args[2])
        files = steagsupports.sheetdestination(args[3], args[1], args[2])
        sheetname = f'{files}\{filename}.csv'
        frame.to_csv(sheetname, index=False)


def calcstrings(*args):
    pass


def calcwether(*args):
    pass
