import steagsupports
from time import time
import steagframes


selected = input('Digite o nome do arquivo (.xlsx):')
caminho = r'C:\Users\julio.firmino\Desktop\plantas\simulado\{}.xlsx'.format(selected)
destino = r'c:\steag_plantas'
#steagsupports.workdata(caminho)
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
        steagframes.calcstringsbox(caminho, period, choose, destino)
    elif equipment == 3:
        steagframes.calcstrings(caminho, period, choose, destino)
    elif equipment == 4:
        steagframes.calcweather(caminho, period, choose, destino)
    v1 = time()
    tm = steagsupports.executiontime(v1, v0)
    print('Processo finalizado com sucesso!!!')
    print('Tempo de execução da aplicação: {} hs : {} min : {} seg'.format(tm[0], tm[1], tm[2]))
else:
    exit()
