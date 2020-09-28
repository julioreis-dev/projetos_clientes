import pandas as pd
import steagsupports


# caminho-0, periodo - 1, choose - 2, destino - 3
# Function to create dataframe to inverter equipment and save in sheet destiny
def calcinverter(*args):
    df = pd.read_excel(args[0])
    column = df.columns.values
    lista_plant = steagsupports.organizetuplainverter(column)
    numberinv = 0
    for i in lista_plant:
        columnfilter = [column[0], column[1], i[0], i[1]]
        df_fin = df.filter(items=columnfilter)
        df_fin = steagsupports.readframe(df_fin)
        df_fin = df_fin[[column[0], i[0], i[1]]]
        df_fin = df_fin.fillna(0.00)
        df_fin.rename(columns={'Date': 'timestamp', i[0]: 'ACTIVE POWER', i[1]: 'COMS STATUS'}, inplace=True)
        namesfile = steagsupports.stamp(args[1], i[0], args[2], 'Inverter')
        files = steagsupports.sheetdestination(args[3], args[1], args[2])
        sheetname = r'{}\{}.csv'.format(files, namesfile)
        df_fin.to_csv(sheetname, index=False)
        numberinv+=1
        print('Arquivo "{}" salvo com sucesso!!!'.format(namesfile))
    return numberinv


# Function to create dataframe to stringbox equipment and save in sheet destiny
def calcstringsbox(*args):
    df = pd.read_excel(args[0])
    column = df.columns.values
    lista_plant = steagsupports.organizetuplastringsbox(column)
    numberbox=0
    for i in lista_plant:
        columnfilter = [column[0], column[1], i[1], i[2], i[0]]
        df_fin = df.filter(items=columnfilter)
        df_fin = steagsupports.readframe(df_fin)
        df_fin = df_fin[[column[0], i[1], i[2], i[0]]]
        df_fin = df_fin.fillna(0.00)
        df_fin.rename(columns={'Date': 'timestamp', i[1]: 'Current', i[2]: 'Power', i[0]: 'COMS STATUS'}, inplace=True)
        namesfile = steagsupports.stamp1(args[1], i[0], args[2], 'String box')
        files = steagsupports.sheetdestination(args[3], args[1], args[2])
        sheetname = r'{}\{}.csv'.format(files, namesfile)
        df_fin.to_csv(sheetname, index=False)
        numberbox+=1
        print('Arquivo "{}" salvo com sucesso!!!'.format(namesfile))
    return numberbox


# Function to create dataframe to string equipment and save in sheet destiny
def calcstrings(*args):
    df = pd.read_excel(args[0])
    column = df.columns.values
    numberstrings=0
    for i in range(2, len(column)):
        columnfilter = [column[0], column[1], column[i]]
        df_fin = df.filter(items=columnfilter)
        df_fin = steagsupports.readframe(df_fin)
        df_fin = df_fin[[column[0], column[i]]]
        df_fin = df_fin.fillna(0.00)
        df_fin.rename(columns={'Date': 'timestamp', column[i]: 'DC Current String'}, inplace=True)
        namesfile = steagsupports.stamp2(args[1], column[i], args[2], 'String')
        files = steagsupports.sheetdestination(args[3], args[1], args[2])
        sheetname = r'{}\{}.csv'.format(files, namesfile)
        df_fin.to_csv(sheetname, index=False)
        numberstrings+=1
        print('Arquivo "{}" salvo com sucesso!!!'.format(namesfile))
    return numberstrings


# Function o create dataframe to weather station equipment and save in sheet destiny
def calcweather(*args):
    plant = ['Sao Pedro', 'Juazeiro', 'Sol do Futuro']
    df_fin = pd.read_excel(args[0])
    df_fin = steagsupports.readframe(df_fin)
    df_fin = df_fin.fillna(0.00)
    df_fin.rename(columns={'Date': 'timestamp'}, inplace=True)
    del df_fin['Time']
    direct = steagsupports.sheetdestination(args[3], args[1], args[2])
    namestamp = f'{plant[args[2] - 1]}-Weather Station'
    sheetname = r'{}\{}.csv'.format(direct, namestamp)
    df_fin.to_csv(sheetname, index=False)
    print('Arquivo "{}" salvo com sucesso!!!'.format(namestamp))
    return 1


# Function to create dataframe to inverter equipment and save in sheet destiny
# def calcinverter(*args):
#     column = steagsupports.organizefiles(args[0])
#     lista_plant = steagsupports.organizetuplainverter(column)
#     for i in lista_plant:
#         df_fin = pd.read_excel(args[0])
#         df_fin = steagsupports.readframe(df_fin)
#         df_fin = df_fin[[column[0], i[0], i[1]]]
#         df_fin = df_fin.fillna(0.00)
#         df_fin.rename(columns={'Date': 'timestamp', i[0]: 'ACTIVE POWER', i[1]: 'COMS STATUS'}, inplace=True)
#         namesfile = steagsupports.stamp(args[1], i[0], args[2], 'Inverter')
#         files = steagsupports.sheetdestination(args[3], args[1], args[2])
#         sheetname = r'{}\{}.csv'.format(files, namesfile)
#         df_fin.to_csv(sheetname, index=False)
#         print('Arquivo {} salvo com sucesso!!!'.format(namesfile))


# Function to create dataframe to stringbox equipment and save in sheet destiny
# def calcstringsbox(*args):
#     column = steagsupports.organizefiles(args[0])
#     lista_plant = steagsupports.organizetuplastringsbox(column)
#     for i in lista_plant:
#         df_fin = pd.read_excel(args[0])
#         df_fin = steagsupports.readframe(df_fin)
#         df_fin = df_fin.fillna(0.00)
#         df_fin = df_fin[[column[0], i[1], i[2], i[0]]]
#         df_fin.rename(columns={'Date': 'timestamp', i[1]: 'Current', i[2]: 'Power', i[0]: 'COMS STATUS'}, inplace=True)
#         namesfile = steagsupports.stamp1(args[1], i[0], args[2], 'String box')
#         files = steagsupports.sheetdestination(args[3], args[1], args[2])
#         sheetname = r'{}\{}.csv'.format(files, namesfile)
#         df_fin.to_csv(sheetname, index=False)


# Function to create dataframe to string equipment and save in sheet destiny
# def calcstrings(*args):
#     column = steagsupports.organizefiles(args[0])
#     for i in column:
#         df_fin = pd.read_excel(args[0])
#         df_fin = steagsupports.readframe(df_fin)
#         df_fin = df_fin.fillna(0.00)
#         df_fin = df_fin[[column[0], i[0]]]
#         df_fin.rename(columns={'Date': 'timestamp', i[0]: 'Current'}, inplace=True)
#         namesfile = steagsupports.stamp1(args[1], i[0], args[2], 'String')
#         files = steagsupports.sheetdestination(args[3], args[1], args[2])
#         sheetname = r'{}\{}.csv'.format(files, namesfile)
#         df_fin.to_csv(sheetname, index=False)


# Function o create dataframe to weather station equipment and save in sheet destiny
# def calcweather(*args):
#     plant = ['Sao Pedro', 'Juazeiro', 'Sol do Futuro']
#     df_fin = pd.read_excel(args[0])
#     df_fin = steagsupports.readframe(df_fin)
#     df_fin = df_fin.fillna(0.00)
#     df_fin.rename(columns={'Date': 'timestamp'}, inplace=True)
#     direct = steagsupports.sheetdestination(args[3], args[1], args[2])
#     namestamp = f'{plant[args[2] - 1]}-Weather Station'
#     sheetname = r'{}\{}.csv'.format(direct, namestamp)
#     df_fin.to_csv(sheetname, index=False)
#     # df_fin['timestamp'] = pd.to_datetime(df_fin['timestamp'])
#     # df_fin['timestamp'] = df_fin['timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')
#     print(df_fin)
