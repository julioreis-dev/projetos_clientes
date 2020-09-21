import pandas as pd
import steagsupports
from time import time


caminho = r'D:\OneDrive\Área de Trabalho\steag\atual\SPD - AGOSTO 2020_2020_09_18.xlsx'
destino = r'c:\steag_plantas'
steagsupports.createsheets(destino)
steagsupports.createsubsheets(destino)
period = steagsupports.option()
choose = steagsupports.option1()
steagsupports.sheetperiod(choose, destino, period)
if choose != 0:
    print('Processando.......\n')
    v0 = time()
    column = steagsupports.organizefiles(caminho)
    lista_plant = steagsupports.organizetupla(column)
    for i in lista_plant:
        df_fin = pd.read_excel(caminho)
        df_fin = df_fin.fillna(0.00)
        df_fin = df_fin[[column[0], i[0], i[1]]]
        df_fin.rename(columns={'Date': 'timestamp', i[0]: 'ACTIVE POWER', i[1]: 'COMS STATUS'}, inplace=True)
        frame = steagsupports.readframe(df_fin)
        filename = steagsupports.stamp(period, i[0], choose)
        files = steagsupports.sheetdestination(destino, period, choose)
        sheetname = f'{files}\{filename}.csv'
        frame.to_csv(sheetname, index=False)
    v1 = time()
    executiontime = (v1 - v0)
    print('Processo finalizado com sucesso!!!')
    print('Tempo de execução da aplicação: {} hs : {} min : {} seg'
          .format(executiontime//3600, executiontime//60, round((executiontime % 60)//1, 2)))
else:
    exit()
