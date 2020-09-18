import pandas as pd
import os


def readarticle(files):
    df = pd.read_csv(files, sep=',')
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['timestamp'] = df['timestamp'].dt.strftime('%Y-%m-%d')
    df['ACTIVE POWER'] = pd.to_datetime(df['ACTIVE POWER'])
    df['ACTIVE POWER'] = df['ACTIVE POWER'].dt.strftime('%H:%M:%S')
    df = df[['timestamp', 'ACTIVE POWER', 'COMS', 'STATUS']]
    df.to_csv(files, index=False)


def organizefiles(files):
    df_data = pd.read_excel(files)
    colunas = df_data.columns.values
    return colunas


'''Analize data of equipment inversores'''
def organizetupla(data):
    listdata = []
    lencollumn = len(data)
    index1 = 1
    index2 = 2
    flag = True
    while flag:
        #print(column[index1], column[index2])
        collumntupla = (column[index1], column[index2])
        listdata.append(collumntupla)
        index1 += 2
        index2 += 2
        if index2 > lencollumn:
            flag = False
    return listdata


def criar_pastas(pasta):
    if not os.path.isdir(pasta):
        os.mkdir(pasta)

def criar_sub(pasta):
    newdir = pasta + ''
    if pasta:
        if not os.path.isdir():
            os.mkdir()



caminho = r'C:\Users\julio.firmino\Desktop\plantas\SPD - AGOSTO 2020_2020_09_18.xlsx'
destino = r'c:\steag_plantas'
criar_pastas(destino)
#readarticle(caminho)
column = organizefiles(caminho)
x = organizetupla(column)
print(x)
for i in x:
    df_fin = pd.read_excel(caminho)
    df_fin = df_fin[[column[0], i[0], i[1]]]
    print(df_fin)
