import steagsupports_factory
from time import time, sleep
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
Data - Hora - Active Power - COMS STATUS
Variáveis String Box
Data - Hora - COMS STATUS - Current - Power
Variáveis Strings
Data - Hora - DC CURRENT STRING XX
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
    pathfiles = r'C:\convert\entrada'
    destino = r'c:\convert\saida'
    listpath = steagsupports_factory.catalogfiles(pathfiles)
    period = steagsupports_factory.option()
    place = steagsupports_factory.option1()
    if place != 0:
        print('Processando..............')
        steagsupports_factory.createsheets(destino)
        steagsupports_factory.sheetperiod(place, destino, period)
        sleep(2)
        print('Realizando leitura dos arquivos!!!')
        sleep(2)
        openfiles = steagsupports_factory.openfiles(listpath[0], listpath[1], listpath[2], listpath[3])
        v0 = time()
        print('Iniciando extração dos arquivos!!!\n')
        sleep(2)
        listdata = [(0, 1), (1, 2), (3, 4), (2, 3)]
        for n in listdata:
            if n[0] == 2:
                manager = Managerengine(openfiles[n[0]], period, place, destino, n[1])
                tag = Thread(target=manager.factory)
                tag.start()
                tag.join()
            else:
                manager = Managerengine(openfiles[n[0]], period, place, destino, n[1])
                tag = Thread(target=manager.factory)
                tag.start()
        v1 = time()
        tm = steagsupports_factory.executiontime(v1, v0)
        print(tm)
        steagsupports_factory.closeapp()
    else:
        steagsupports_factory.closeapp()
        exit()


if __name__ == '__main__':
    main()
