import steagsupports
from time import time
import steagframes

'''
Esta aplicação tem por finalidade trabalhar a planilha com extensão (.xlsx) que contem os dados oriundos da extração VPN
levando em consideração os critérios de cada equipamento e as suas respectivas plantas. O produto final
fornece diversos arquivos divididos com extenção (.csv) que servirá como base para a aplicação corporativa 
que calcula os indices de interesse e relevância do negócio.
'''


def main():
    selected = input('Digite o nome do arquivo (.xlsx):')
    caminho = r'D:\OneDrive\Área de Trabalho\steag\atual\{}.xlsx'.format(selected)
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


if __name__ == '__main__':
    main()
