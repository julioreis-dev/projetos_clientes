import steagsupports
from time import time
import steagframes


caminho = r'D:\OneDrive\Área de Trabalho\steag\atual\Sol do Futuro - AGOSTO 2020_2020_09_18.xlsx'
destino = r'c:\steag_plantas'
steagsupports.createsheets(destino)
steagsupports.createsubsheets(destino)
period = steagsupports.option()
choose = steagsupports.option1()
equipment = steagsupports.option2()
steagsupports.sheetperiod(choose, destino, period)
if choose != 0:
    print('Processando.......\n')
    v0 = time()
    if equipment == 1:
        steagframes.calcinverter(caminho, period, choose, destino)
    elif equipment == 2:
        steagframes.calcstrings(caminho, period, choose, destino)
    elif equipment == 3:
        steagframes.calcwether(caminho, period, choose, destino)
    v1 = time()
    executiontime = (v1 - v0)
    print('Processo finalizado com sucesso!!!')
    print('Tempo de execução da aplicação: {} hs : {} min : {} seg'
          .format(executiontime//3600, executiontime//60, round((executiontime % 60)//1, 2)))
else:
    exit()
