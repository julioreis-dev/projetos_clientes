import pandas as pd
import steagsupports


# caminho-0
# periodo - 1
# choose - 2
# destino - 3


def calcinverter(*args):
    column = steagsupports.organizefiles(args[0])
    lista_plant = steagsupports.organizetuplainverter(column)
    for i in lista_plant:
        df_fin = pd.read_excel(args[0])
        df_fin = steagsupports.readframe(df_fin)
        df_fin = df_fin[[column[0], i[0], i[1]]]
        df_fin = df_fin.fillna(0.00)
        df_fin.rename(columns={'Date': 'timestamp', i[0]: 'ACTIVE POWER', i[1]: 'COMS STATUS'}, inplace=True)
        namesfile = steagsupports.stamp(args[1], i[0], args[2], 'Inverter')
        files = steagsupports.sheetdestination(args[3], args[1], args[2])
        sheetname = r'{}\{}.csv'.format(files, namesfile)
        df_fin.to_csv(sheetname, index=False)


def calcstringsbox(*args):
    column = steagsupports.organizefiles(args[0])
    lista_plant = steagsupports.organizetuplastringsbox(column)
    for i in lista_plant:
        df_fin = pd.read_excel(args[0])
        df_fin = steagsupports.readframe(df_fin)
        df_fin = df_fin.fillna(0.00)
        df_fin = df_fin[[column[0], i[1], i[2], i[0]]]
        df_fin.rename(columns={'Date': 'timestamp', i[1]: 'Current', i[2]: 'Power', i[0]: 'COMS STATUS'}, inplace=True)
        namesfile = steagsupports.stamp1(args[1], i[0], args[2], 'String box')
        files = steagsupports.sheetdestination(args[3], args[1], args[2])
        sheetname = r'{}\{}.csv'.format(files, namesfile)
        df_fin.to_csv(sheetname, index=False)


def calcstrings(*args):
    pass


def calcweather(*args):
    df_fin = pd.read_excel(args[0])
    df_fin = steagsupports.readframe(df_fin)
    df_fin = df_fin.fillna(0.00)
    df_fin.rename(columns={'Date': 'timestamp'}, inplace=True)
    #df_fin['timestamp'] = pd.to_datetime(df_fin['timestamp'])
    #df_fin['timestamp'] = df_fin['timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')
    print(df_fin)
