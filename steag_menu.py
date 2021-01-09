import steagsupports_factory
from time import time, sleep
import steag_inverter as inv
import steag_stringbox as box
import steag_strings as stg
import steag_weather as wtr
import steagsupports_factory as stf
from threading import Thread
import time
from tkinter import *
from tkcalendar import *
from datetime import datetime

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


BLACK = '#000000'
CINZA = '#9ba4b4'
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
FONT_NAME = "Courier"


class Gui_interface:

    def gui(self):
        self.window = Tk()
        self.window.title('Sistema de Conversão de Dados - Steag Energy Services')
        self.window.geometry('740x600')
        self.window.config(padx=20, pady=20, bg=CINZA)
        t = time.localtime()

        canvas = Canvas(width=700, height=100)
        canvas.config(bg=CINZA, highlightthickness=0)
        steag_file = PhotoImage(file='steag1.png')
        canvas.create_image(350, 40, image=steag_file)
        canvas.grid(row=0, column=0, columnspan=5)

        self.canvas2 = Canvas(width=600, height=60, bg=CINZA, highlightthickness=0)
        self.result = self.canvas2.create_text(320, 30, text='', font=('Ariel', 10, 'bold'))
        self.canvas2.place(bordermode=INSIDE, height=80, width=680, x=20, y=400)

        self.calend = Calendar(self.window, selectmode='day', year=t[0], month=t[1], day=t[2], locale='pt_BR',
                               date_pattern='dd/mm/y',
                               showweeknumbers=False, firstweekday='sunday', showothermonthdays=False)
        self.calend.grid(row=1, column=3, columnspan=2, rowspan=2)

        buttom_select = PhotoImage(file='button_select.png')
        start_buttom = Button(text='Selecionar', image=buttom_select, font=(FONT_NAME, 12, 'bold'),
                              command=self.get_startdate,
                              bg=CINZA, activebackground=CINZA, border='0', cursor='top_left_corner')
        start_buttom.grid(row=1, column=2)

        reset_buttom = Button(text='Selecionar', font=(FONT_NAME, 12, 'bold'), command=self.get_finishdate,
                              image=buttom_select,
                              bg=CINZA, activebackground=CINZA, border='0')
        reset_buttom.grid(row=2, column=2)

        buttom_image = PhotoImage(file='button.png')
        run_buttom = Button(text='Submit', image=buttom_image, font=(FONT_NAME, 12, 'underline'), command=self.main,
                            activebackground=CINZA, bd=5, bg=CINZA, border='0')
        run_buttom.place(x=280, y=500)

        label_date1 = Label(text='Data Inicial:', fg=BLACK, bg=CINZA, font=(FONT_NAME, 14, 'bold'), padx=10)
        label_date1.grid(row=1, column=0, sticky=E)

        label_date2 = Label(text='Data Final:', fg=BLACK, bg=CINZA, font=(FONT_NAME, 14, 'bold'), padx=10)
        label_date2.grid(row=2, column=0, sticky=E)

        label_plant = Label(text='Escolha uma das plantas disponíveis:', fg=BLACK, bg=CINZA,
                            font=(FONT_NAME, 14, 'bold'), padx=20, pady=40)
        label_plant.grid(row=3, column=1, columnspan=3, sticky=W)

        # start_label = Label(text='', fg=BLACK, bg=CINZA, font=(FONT_NAME, 14, 'bold'), width=10)
        self.start_label = Entry(self.window, bd=2, width=10, textvariable=StringVar(),
                                 font=(FONT_NAME, 14, 'bold'), bg=CINZA)
        self.start_label.grid(row=1, column=1, sticky=W)

        # finish_label = Label(text='', fg=BLACK, bg=CINZA, font=(FONT_NAME, 14, 'bold'), width=10)
        self.finish_label = Entry(self.window, bd=2, width=10, textvariable=StringVar(),
                                  font=(FONT_NAME, 14, 'bold'), bg=CINZA)
        self.finish_label.grid(row=2, column=1, sticky=W)

        self.opt_radio = IntVar()
        self.opt_radio.set(1)
        plants = [("são pedro", 1), ("juazeiro", 2), ("sol do futuro", 3)]

        # Construção dos radio buttom da interface gráfica
        incr = 0
        for name_plant, val in plants:
            Radiobutton(self.window,
                        text=name_plant.upper(),
                        padx=20,
                        variable=self.opt_radio,
                        fg=BLACK,
                        anchor='e',
                        activeforeground='white',
                        activebackground=CINZA,
                        selectcolor=CINZA,
                        bg=CINZA,
                        font=('Arial', 12, 'bold'),
                        command=self.optmonth,
                        value=val).place(x=60 + incr, y=340)
            incr += 200
        self.window.mainloop()

    def get_startdate(self):
        self.start_label.insert(0, self.calend.get_date())


    def get_finishdate(self):
        self.finish_label.insert(0, self.calend.get_date())


    def patterndate(self):
        date1 = self.start_label.get()
        start = stf.formatdates(date1)
        date2 = self.start_label.get()
        end = stf.formatdates(date2)
        sheet_name = start + '_' + end
        return sheet_name

    def optmonth(self):
        return self.opt_radio.get()

    def main(self):
        pathfiles = r'C:\convert\entrada'
        destino = r'c:\convert\saida'
        listpath = steagsupports_factory.catalogfiles(pathfiles)
        period = self.patterndate()
        place = self.optmonth()
        self.canvas2.itemconfig(self.result, text='Processando..............')
        steagsupports_factory.createsheets(destino)
        steagsupports_factory.sheetperiod(place, destino, period)
        sleep(2)
        print('Realizando leitura dos arquivos!!!')
        # sleep(2)
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


if __name__ == '__main__':
    x = Gui_interface()
    x.gui()
