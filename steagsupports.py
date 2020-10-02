import os
import pandas as pd
import time
from datetime import datetime
from random import randint


# Function to input extract period
def option():
    print('################################################')
    print('Digite o período de extração dos dados:')
    date1 = input('Data inicial: ')
    start = formatdates(date1)
    date2 = input('Data final: ')
    end = formatdates(date2)
    sheet_name = start + '_' + end
    return sheet_name


# Option to choose plants
def option1():
    flag = True
    while flag:
        opt = [0, 1, 2, 3]
        plant = int(input('################################################'
                          '\nEscolha uma das plantas disponíveis nesta aplicação:'
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


# Option to choose equipments
def option2():
    flag = True
    while flag:
        opt2 = [0, 1, 2, 3, 4]
        plant2 = int(input('################################################'
                           '\nSelecione um tipo de equipamento disponível:'
                           '\nDigite 1 --> Inversores'
                           '\nDigite 2 --> Strings Box'
                           '\nDigite 3 --> Strings'
                           '\nDigite 4 --> Weather Station'
                           '\nDigite 0 --> Sair.'
                           '\n################################################'
                           '\nPrezado usuário, escolha uma opção?'))
        if plant2 in opt2:
            return plant2
        else:
            print('Opção incorreta, tente novamente.')
            time.sleep(3)


# Function to format date column and time column
def readframe(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
    df['Time'] = pd.to_datetime(df['Time'])
    df['Time'] = df['Time'].dt.strftime('%H:%M:%S')
    df['Date'] = df['Date'] + ' ' + df['Time']
    return df


# Function to create sheet 'steag_plantas'
def createsheets(pasta):
    if not os.path.isdir(pasta):
        os.mkdir(pasta)


# Function to create sheet to each plant inside 'steag_plantas'
def createsubsheets(pasta):
    sheet1 = os.path.join(pasta, 'são pedro')
    sheet2 = os.path.join(pasta, 'juazeiro')
    sheet3 = os.path.join(pasta, 'sol do futuro')
    sheets = [sheet1, sheet2, sheet3]
    for n in sheets:
        if not os.path.isdir(n):
            os.mkdir(n)


# Function that return list with column names(Descarte)
def organizefiles(files):
    df_data = pd.read_excel(files)
    colun = df_data.columns.values
    return colun


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


# Function to analize data of equipment stringbox
def organizetuplastringsbox(listcol):
    flag = True
    listdata = []
    lencollumn = len(listcol)
    index1 = 2
    index2 = 3
    index3 = 4
    while flag:
        collumntupla = (listcol[index1], listcol[index2], listcol[index3])
        listdata.append(collumntupla)
        index1 += 3
        index2 += 3
        index3 += 3
        if index2 > lencollumn:
            flag = False
    return listdata


# Function to analize data of equipment strings (descarte)
def organizetuplastrings(listcol):
    flag = True
    listdata = []
    lencollumn = len(listcol)
    index1 = 2
    while flag:
        collumntupla = (listcol[index1])
        listdata.append(collumntupla)
        index1 += 1
        if index1 > lencollumn:
            flag = False
    return listdata


# Function to prepare date to use as names in sheets
def formatdates(date):
    timedata = datetime.strptime(date, '%d/%m/%Y').date()
    formatdata = timedata.strftime('%Y-%m-%d')
    return formatdata


# Function to create period sheet to receive all content
def sheetperiod(*args):
    if args[0] == 1:
        sheets = os.path.join(args[1], 'são pedro', args[2])
        if not os.path.isdir(sheets):
            os.mkdir(sheets)
    elif args[0] == 2:
        sheets = os.path.join(args[1], 'juazeiro', args[2])
        if not os.path.isdir(sheets):
            os.mkdir(sheets)
    elif args[0] == 3:
        sheets = os.path.join(args[1], 'sol do futuro', args[2])
        if not os.path.isdir(sheets):
            os.mkdir(sheets)


# Function to inform correct sheet destiny address
def sheetdestination(*args):
    if args[2] == 1:
        sheetdest1 = os.path.join(args[0], 'são pedro', args[1])
        return sheetdest1
    elif args[2] == 2:
        sheetdest2 = os.path.join(args[0], 'juazeiro', args[1])
        return sheetdest2
    elif args[2] == 3:
        sheetdest3 = os.path.join(args[0], 'sol do futuro', args[1])
        return sheetdest3


# Function to create name to each file inverter
def stamp(*args):
    workplant(10)
    if args[2] == 1:
        namestamp1 = f'Sao Pedro-data-{args[0]}-{args[3]}-{args[1][12:21]}'
        return namestamp1
    elif args[2] == 2:
        namestamp2 = f'Juazeiro-data-{args[0]}-{args[3]}-{args[1][11:22]}'
        return namestamp2
    elif args[2] == 3:
        namestamp3 = f'Sol do Futuro-data-{args[0]}-{args[3]}-{args[1][16:27]}'
        return namestamp3


# Function to create name to each file stringbox
def stamp1(*args):
    workplant(10)
    if args[2] == 1:
        namestamp1 = f'Sao Pedro-data-{args[0]}-{args[3]}-{args[1][12:25]}'
        return namestamp1
    elif args[2] == 2:
        namestamp2 = f'Juazeiro-data-{args[0]}-{args[3]}-{args[1][11:25]}'
        return namestamp2
    elif args[2] == 3:
        namestamp3 = f'Sol do Futuro-data-{args[0]}-{args[3]}-{args[1][16:46]}'
        return namestamp3


# Function to create name to each file string
def stamp2(*args):
    workplant(10)
    if args[2] == 1:
        namestamp1 = f'Sao Pedro-data-{args[0]}-{args[3]}-{args[1][12:27]}'
        return namestamp1
    elif args[2] == 2:
        namestamp2 = f'Juazeiro-data-{args[0]}-{args[3]}-{args[1][11:43]}'
        return namestamp2
    elif args[2] == 3:
        namestamp3 = f'Sol do Futuro-data-{args[0]}-{args[3]}-{args[1][16:52]}'
        return namestamp3


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


# Function to calculate time execution
def executiontime(*args):
    execution = args[0] - args[1]
    hr = execution // 3600
    if hr == 0:
        minute = execution // 60
        seg = round((execution % 60) // 1, 2)
    else:
        resthr = execution % 3600
        minute = resthr // 60
        seg = round((minute % 60) // 1, 2)
    return hr, minute, seg


def workplant(temp):
    sec = randint(0, temp)
    time.sleep(sec)
