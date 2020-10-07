import steagsupports_factory
from time import time
import steag_inverter as inv
import steag_stringbox as box
import steag_strings as stg
import steag_weather as wtr

'''
Esta aplicação tem por finalidade trabalhar a planilha com extensão (.xlsx) que contem os dados oriundos da extração VPN
levando em consideração os critérios de cada equipamento e as suas respectivas plantas. O produto final
fornece diversos arquivos divididos com extensão (.csv) que servirá como base para a aplicação corporativa 
que calcula os indices de interesse e relevância do negócio.
Dados de entrada:
Variáveis Inversores
Active Power - COMS STATUS
Variáveis String Box
COMS STATUS - Current - Power
Variáveis Strings
DC CURRENT STRING XX
'''


class Managerengine:
    def __init__(self, caminho, period, place, destino, equip):
        self.caminho = caminho
        self.period = period
        self.place = place
        self.destino = destino
        self.equip = equip

    def factory(self):
        if self.equip == 1:
            inv.Inverter.calcinverter(self.caminho, self.period, self.place, self.destino)
        elif self.equip == 2:
            box.Stringbox.calcstringsbox(self.caminho, self.period, self.place, self.destino)
        elif self.equip == 3:
            stg.Strings.calcstrings(self.caminho, self.period, self.place, self.destino)
        elif self.equip == 4:
            wtr.Weatherstation.calcweather(self.caminho, self.period, self.place, self.destino)


def main():
    print('################# Steag Energy Service Brasil #################')
    selected = input('Digite o nome do arquivo (.xlsx):')
    caminho = r'D:\OneDrive\Área de Trabalho\steag\atual\{}.xlsx'.format(selected)
    destino = r'c:\steag_plantas'
    period = steagsupports_factory.option()
    place = steagsupports_factory.option1()
    if place != 0:
        equipment = steagsupports_factory.option2()
        if equipment != 0:
            print('Processando.......\n')
            v0 = time()
            steagsupports_factory.createsheets(destino)
            steagsupports_factory.createsubsheets(destino)
            steagsupports_factory.sheetperiod(place, destino, period)
            Managerengine(caminho, period, place, destino, equipment).factory()
            v1 = time()
            tm = steagsupports_factory.executiontime(v1, v0)
            print('Tempo de execução da aplicação: {} hs : {} min : {} seg'.format(tm[0], tm[1], tm[2]))
            print('Processo finalizado com sucesso!!!')
    else:
        exit()


if __name__ == '__main__':
    main()