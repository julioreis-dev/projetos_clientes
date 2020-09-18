import os
import pandas as pd
import time


def readarticle(files):
    df = pd.read_csv(files, sep=',')
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['timestamp'] = df['timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')
    # df['ACTIVE POWER'] = pd.to_datetime(df['ACTIVE POWER'])
    # df['ACTIVE POWER'] = df['ACTIVE POWER'].dt.strftime('%H:%M:%S')
    df = df[['timestamp', 'ACTIVE POWER', 'COMS STATUS']]
    df.to_csv(files, index=False)


def criar_pastas(pasta):
    if not os.path.isdir(pasta):
        os.mkdir(pasta)


def criar_sub(pasta):
    sheet1 = os.path.join(pasta, 'são pedro')
    sheet2 = os.path.join(pasta, 'juazeiro')
    sheet3 = os.path.join(pasta, 'sol do futuro')
    sheets = [sheet1, sheet2, sheet3]
    for n in sheets:
        if not os.path.isdir(n):
            os.mkdir(n)


def organizefiles(files):
    df_data = pd.read_excel(files)
    colunas = df_data.columns.values
    return colunas


'Analize data of equipment inversores'
def organizetupla(data):
    listdata = []
    lencollumn = len(data)
    index1 = 1
    index2 = 2
    flag = True
    while flag:
        collumntupla = (data[index1], data[index2])
        listdata.append(collumntupla)
        index1 += 2
        index2 += 2
        if index2 > lencollumn:
            flag = False
    return listdata


def option():
    flag = True
    while flag:
        opt = [0, 1, 2, 3]
        plant = int(input('################################################'
                          '\nTipos de opções disponíveis nesta aplicação:'
                          '\nDigite 1 --> São Pedro'
                          '\nDigite 2 --> Juazeiro'
                          '\nDigite 3 --> Sol do Futuro'
                          '\nDigite 0 --> Sair.'
                          '\n################################################'
                          '\nPrezado usuário, escolha uma opção?'))
        if plant in opt:
            return plant
        else:
            print('Opção incorreta, tente novamente.')
            time.sleep(3)


def sheet_destination():
    pass
