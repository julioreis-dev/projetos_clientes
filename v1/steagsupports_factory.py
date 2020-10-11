import os
import pandas as pd
import time
from datetime import datetime
import re


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

    sheets = ['são pedro', 'juazeiro', 'sol do futuro']
    for n in sheets:
        sheet = os.path.join(pasta, n)
        if not os.path.isdir(sheet):
            os.mkdir(sheet)


# Function to prepare date to use as names in sheets
def formatdates(date):
    timedata = datetime.strptime(date, '%d/%m/%Y').date()
    formatdata = timedata.strftime('%Y-%m-%d')
    return formatdata


# Function to create period sheet to receive all content
def sheetperiod(*args):
    dictplant = {1: 'são pedro', 2: 'juazeiro', 3: 'sol do futuro'}
    sheets = os.path.join(args[1], dictplant[args[0]], args[2])
    if not os.path.isdir(sheets):
        os.mkdir(sheets)


# Function to inform correct sheet destiny address
def sheetdestination(*args):
    dictplant = {1: 'são pedro', 2: 'juazeiro', 3: 'sol do futuro'}
    sheetdest = os.path.join(args[0], dictplant[args[2]], args[1])
    return sheetdest


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
    return 'Tempo de execução da aplicação: {} hs : {} min : {} seg\nProcesso finalizado com sucesso!!!' \
        .format(hr, minute, seg)


def closeapp():
    print('Encerrando a aplicação.........')
    time.sleep(5)
    print('Aplicação encerrada com segurança!!!')


def catalogfiles(directory):
    listfile = []
    listequip = ['INVERTER', 'STRINGBOX', 'STRING', 'WEATHER STATION']
    lista_arquivos = os.listdir(directory)
    for plant in listequip:
        for contents in lista_arquivos:
            if re.search('\\b' + plant + '\\b', contents, re.IGNORECASE):
                content = os.path.join(directory, contents)
                if os.path.isfile(content):
                    listfile.append(content)
                    break
    return listfile
