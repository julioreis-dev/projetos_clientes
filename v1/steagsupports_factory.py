import os
import pandas as pd
import time
from datetime import datetime


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
        plant = input('################################################'
                      '\nEscolha uma das plantas disponíveis nesta aplicação:'
                      '\nDigite 1 --> São Pedro'
                      '\nDigite 2 --> Juazeiro'
                      '\nDigite 3 --> Sol do Futuro'
                      '\nDigite 0 --> Sair.'
                      '\n################################################'
                      '\nPrezado usuário, escolha uma opção?')
        if plant.isdigit():
            plant = int(plant)
            if plant in opt:
                return plant
            else:
                print('Opção incorreta!!!\nPor favor, tente novamente digitando alguma das opções existentes!!!')
                time.sleep(3)
        else:
            print('Opção Incorreta!!!\nAlgum character inválido foi digitado. As opções serão fornecidas novamente!!!')
            time.sleep(4)


# Function to open files
def openfiles(*args):
    openfiles_list = []
    cont = 1
    for n in range(0, 4):
        print('Iniciando Etapa {}/4...............'.format(cont))
        df_read = pd.read_excel(args[n])
        openfiles_list.append(df_read)
        time.sleep(2)
        print('Etapa {}/4................completed\n'.format(cont))
        cont += 1
        time.sleep(2)
    time.sleep(2)
    return openfiles_list


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
