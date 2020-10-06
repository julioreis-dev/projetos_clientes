import steagsupports_factory
from time import time
import steag_inverter as inv
import steag_stringbox as box
import steag_strings as stg
import steag_weather as wtr
from threading import Thread

'''
Esta aplicação tem por finalidade trabalhar a planilha com extensão (.xlsx) que contem os dados oriundos da 
extração VPN levando em consideração os critérios de cada equipamento e as suas respectivas plantas. O produto final
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
    def __init__(self, frame, period, place, destino, equip):
        self.frame = frame
        self.period = period
        self.place = place
        self.destino = destino
        self.equip = equip

    def factory(self):
        if self.equip == 1:
            inv.Inverter.calcinverter(self.frame, self.period, self.place, self.destino)
        elif self.equip == 2:
            box.Stringbox.calcstringsbox(self.frame, self.period, self.place, self.destino)
        elif self.equip == 3:
            stg.Strings.calcstrings(self.frame, self.period, self.place, self.destino)
        elif self.equip == 4:
            wtr.Weatherstation.calcweather(self.frame, self.period, self.place, self.destino)


def main():
    print('################# Steag Energy Service Brasil #################')
    selinverter = input('Digite o nome do arquivo INVERTER(.xlsx):')
    selstrbox = input('Digite o nome do arquivo STRING BOX(.xlsx):')
    selstr = input('Digite o nome do arquivo STRING(.xlsx):')
    selweather = input('Digite o nome do arquivo WEATHER STATION(.xlsx):')
    pathinverter = r'D:\OneDrive\Área de Trabalho\steag\atual\{}.xlsx'.format(selinverter)
    pathstrbox = r'D:\OneDrive\Área de Trabalho\steag\atual\{}.xlsx'.format(selstrbox)
    pathstr = r'D:\OneDrive\Área de Trabalho\steag\atual\{}.xlsx'.format(selstr)
    pathweather = r'D:\OneDrive\Área de Trabalho\steag\atual\{}.xlsx'.format(selweather)
    destino = r'c:\steag_plantas'
    period = steagsupports_factory.option()
    place = steagsupports_factory.option1()
    if place != 0:
        v0 = time()
        print('Processando.......\n')
        steagsupports_factory.createsheets(destino)
        steagsupports_factory.createsubsheets(destino)
        steagsupports_factory.sheetperiod(place, destino, period)
        openfiles = steagsupports_factory.openfiles(pathinverter, pathstrbox, pathstr, pathweather)
        x = Managerengine(openfiles[0], period, place, destino, 1)
        t1 = Thread(target=x.factory)
        t1.start()
        y = Managerengine(openfiles[1], period, place, destino, 2)
        t2 = Thread(target=y.factory)
        t2.start()
        z = Managerengine(openfiles[2], period, place, destino, 3)
        t3 = Thread(target=z.factory)
        t3.start()
        w = Managerengine(openfiles[3], period, place, destino, 4)
        t4 = Thread(target=w.factory)
        t4.start()
        v1 = time()
        tm = steagsupports_factory.executiontime(v1, v0)
        print('Tempo de execução da aplicação: {} hs : {} min : {} seg'.format(tm[0], tm[1], tm[2]))
        print('Processo finalizado com sucesso!!!')
    else:
        exit()


if __name__ == '__main__':
    main()
