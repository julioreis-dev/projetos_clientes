import steagsupports
from time import time
import steagframes

'''
Esta aplicação tem por finalidade trabalhar a planilha com extensão (.xlsx) que contem os dados oriundos da extração VPN
levando em consideração os critérios de cada equipamento e as suas respectivas plantas. O produto final
fornece diversos arquivos divididos com extensão (.csv) que servirá como base para a aplicação corporativa 
que calcula os indices de interesse e relevância do negócio.
'''


def main():
    print('################# Steag Energy Service Brasil #################')
    selected = input('Digite o nome do arquivo (.xlsx):')
    caminho = r'D:\OneDrive\Área de Trabalho\steag\atual\{}.xlsx'.format(selected)
    destino = r'c:\steag_plantas'
    steagsupports.createsheets(destino)
    steagsupports.createsubsheets(destino)
    period = steagsupports.option()
    place = steagsupports.option1()
    if place != 0:
        equipment = steagsupports.option2()
        if equipment != 0:
            v0 = time()
            steagsupports.sheetperiod(place, destino, period)
            print('Processando.......\n')
            if equipment == 1:
                continv = steagframes.calcinverter(caminho, period, place, destino)
                print('\nVolume de dados: {} arquivos processados'.format(continv))
            elif equipment == 2:
                contbox = steagframes.calcstringsbox(caminho, period, place, destino)
                print('\nVolume de dados: {} arquivos processados'.format(contbox))
            elif equipment == 3:
                contstrings = steagframes.calcstrings(caminho, period, place, destino)
                print('\nVolume de dados: {} arquivos processados'.format(contstrings))
            elif equipment == 4:
                contweather = steagframes.calcweather(caminho, period, place, destino)
                print('\nVolume de dados: {} arquivo processado'.format(contweather))
            v1 = time()
            tm = steagsupports.executiontime(v1, v0)
            print('Tempo de execução da aplicação: {} hs : {} min : {} seg'.format(tm[0], tm[1], tm[2]))
            print('Processo finalizado com sucesso!!!')
    else:
        exit()


if __name__ == '__main__':
    main()
