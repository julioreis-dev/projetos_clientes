import os
import pandas as pd
import time
from datetime import datetime


def readframe(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['timestamp'] = df['timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')
    df = df[['timestamp', 'ACTIVE POWER', 'COMS STATUS']]
    return df


def createsheets(pasta):
    if not os.path.isdir(pasta):
        os.mkdir(pasta)


def createsubsheets(pasta):
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
    flag = True
    listdata = []
    lencollumn = len(data)
    index1 = 1
    index2 = 2
    while flag:
        collumntupla = (data[index1], data[index2])
        listdata.append(collumntupla)
        index1 += 2
        index2 += 2
        if index2 > lencollumn:
            flag = False
    return listdata


def option():
    date1 = input('Digite a data inicial: ')
    start = formatdates(date1)
    date2 = input('Digite a data final: ')
    end = formatdates(date2)
    sheet_name = start + '_' + end
    return sheet_name


def option1():
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


def formatdates(date):
    timedata = datetime.strptime(date, '%d/%m/%Y').date()
    formatdata = timedata.strftime('%Y-%m-%d')
    return formatdata


def sheetperiod(*args):
    if args[0] == 1:
        sheetdest = f'{args[1]}\são pedro'
        sheets = os.path.join(sheetdest, args[2])
        if not os.path.isdir(sheets):
            os.mkdir(sheets)
    elif args[0] == 2:
        sheetdest = f'{args[1]}\juazeiro'
        sheets = os.path.join(sheetdest, args[2])
        if not os.path.isdir(sheets):
            os.mkdir(sheets)
    elif args[0] == 3:
        sheetdest = f'{args[1]}\sol do futuro'
        sheets = os.path.join(sheetdest, args[2])
        if not os.path.isdir(sheets):
            os.mkdir(sheets)


def sheetdestination(*args):
    if args[2] == 1:
        sheetdest1 = f'{args[0]}\são pedro\{args[1]}'
        return sheetdest1
    elif args[2] == 2:
        sheetdest2 = f'{args[0]}\juazeiro\{args[1]}'
        return sheetdest2
    elif args[2] == 3:
        sheetdest3 = f'{args[0]}\sol do futuro\{args[1]}'
        return sheetdest3


def stamp(*args):
    if args[2] == 1:
        namestamp1 = f'são pedro - {args[0]} - {args[1][12:21]}'
        return namestamp1
    elif args[2] == 2:
        namestamp2 = f'juazeiro - {args[0]} - {args[1][10:22]}'
        return namestamp2
    elif args[2] == 3:
        namestamp3 = f'sol do futuro - {args[0]} - {args[1][16:27]}'
        return namestamp3
