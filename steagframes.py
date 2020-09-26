import pandas as pd
import steagsupports


# caminho-0, periodo - 1, choose - 2, destino - 3
# Create dataframe to inverter equipment and save in sheet destiny
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


# Create dataframe to stringbox equipment and save in sheet destiny
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


# Create dataframe to string equipment and save in sheet destiny
def calcstrings(*args):
    column = steagsupports.organizefiles(args[0])
    for i in column:
        df_fin = pd.read_excel(args[0])
        df_fin = steagsupports.readframe(df_fin)
        df_fin = df_fin.fillna(0.00)
        df_fin = df_fin[[column[0], i[0]]]
        df_fin.rename(columns={'Date': 'timestamp', i[0]: 'Current'}, inplace=True)
        namesfile = steagsupports.stamp1(args[1], i[0], args[2], 'String')
        files = steagsupports.sheetdestination(args[3], args[1], args[2])
        sheetname = r'{}\{}.csv'.format(files, namesfile)
        df_fin.to_csv(sheetname, index=False)


# Create dataframe to weather station equipment and save in sheet destiny
def calcweather(*args):
    plant = ['Sao Pedro', 'Juazeiro', 'Sol do Futuro']
    df_fin = pd.read_excel(args[0])
    df_fin = steagsupports.readframe(df_fin)
    df_fin = df_fin.fillna(0.00)
    df_fin.rename(columns={'Date': 'timestamp'}, inplace=True)
    direct = steagsupports.sheetdestination(args[3], args[1], args[2])
    namestamp = f'{plant[args[2] - 1]}-Weather Station'
    sheetname = r'{}\{}.csv'.format(direct, namestamp)
    df_fin.to_csv(sheetname, index=False)
    # df_fin['timestamp'] = pd.to_datetime(df_fin['timestamp'])
    # df_fin['timestamp'] = df_fin['timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')
    print(df_fin)
