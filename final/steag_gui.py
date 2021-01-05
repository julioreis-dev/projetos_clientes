import time
from tkinter import *
from tkcalendar import *

BLACK = '#000000'
CINZA = '#9ba4b4'
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
# CINZA = '#9ba4b4'
# BLUE = '#318fb5'
FONT_NAME = "Courier"

def get_startdate():
    start_label.config(text=calend.get_date())


def get_finishdate():
    finish_label.config(text=calend.get_date())


def optmonth():
    # print(opt_radio.get())
    return opt_radio.get()



window = Tk()
# window.title('Steag Energy Services')
window.title('Sistema de Conversão de Dados - Steag Energy Services')
window.geometry('740x600')
window.config(padx=20, pady=20, bg=CINZA)
t = time.localtime()

canvas = Canvas(width=700, height=100)
canvas.config(bg=CINZA, highlightthickness=0)
steag_file = PhotoImage(file='steag1.png')
canvas.create_image(350, 40, image=steag_file)
canvas.grid(row=0, column=0, columnspan=5)

canvas2 = Canvas(width=600, height=60, bg=CINZA, highlightthickness=0)
result = canvas2.create_text(320, 30, text='Processando', font=('Ariel', 10, 'bold'))
canvas2.place(bordermode=INSIDE, height=80, width=680, x=20, y=400)

calend = Calendar(window, selectmode='day', year=t[0], month=t[1], day=t[2], locale='pt_BR', date_pattern='dd/mm/y',
                  showweeknumbers=False, firstweekday='sunday', showothermonthdays=False)
calend.grid(row=1, column=3, columnspan=2, rowspan=2)

# timer_label = Label(text='Timer', fg=GREEN, bg=BLUE, font=(FONT_NAME, 30, 'bold'))
# timer_label.grid(row=0, column=1)
buttom_select = PhotoImage(file='button_select.png')
start_buttom = Button(text='Selecionar', image=buttom_select, font=(FONT_NAME, 12, 'bold'), command=get_startdate,
                      bg=CINZA, activebackground=CINZA, border='0')
start_buttom.grid(row=1, column=2)

reset_buttom = Button(text='Selecionar', font=(FONT_NAME, 12, 'bold'), command=get_finishdate, image=buttom_select,
                      bg=CINZA, activebackground=CINZA, border='0')
reset_buttom.grid(row=2, column=2)

buttom_image = PhotoImage(file='button.png')
run_buttom = Button(text='Submit', image=buttom_image, font=(FONT_NAME, 12, 'underline'), command=optmonth,
                    activebackground=CINZA, bd=5, bg=CINZA, border='0')
run_buttom.place(x=280, y=500)

label_date1 = Label(text='Data Inicial:', fg=BLACK, bg=CINZA, font=(FONT_NAME, 14, 'bold'), padx=10)
# label_date1.place(x=10, y=130)
label_date1.grid(row=1, column=0, sticky=E)

label_date2 = Label(text='Data Final:', fg=BLACK, bg=CINZA, font=(FONT_NAME, 14, 'bold'), padx=10)
# label_date2.place(x=10, y=200)
label_date2.grid(row=2, column=0, sticky=E)

label_plant = Label(text='Escolha uma das plantas disponíveis:', fg=BLACK, bg=CINZA,
                    font=(FONT_NAME, 14, 'bold'), padx=20, pady=40)
label_plant.grid(row=3, column=1, columnspan=3, sticky=W)

start_label = Label(text='', fg=BLACK, bg=CINZA, font=(FONT_NAME, 14, 'bold'), width=10)
# start_label.place(x=160, y=130)
start_label.grid(row=1, column=1, sticky=W)

finish_label = Label(text='', fg=BLACK, bg=CINZA, font=(FONT_NAME, 14, 'bold'), width=10)
finish_label.grid(row=2, column=1, sticky=W)

# label = Label(text='', fg='white', bg=GREEN, font=(FONT_NAME, 14, 'bold'))
# label.grid(row=6, column=0, columnspan=2)

opt_radio = IntVar()
opt_radio.set(1)
plants = [("são pedro", 1), ("juazeiro", 2), ("sol do futuro", 3)]

# Construção dos radio buttom da interface gráfica
incr = 0
for name_plant, val in plants:
    Radiobutton(window,
                text=name_plant.upper(),
                padx=20,
                variable=opt_radio,
                fg=BLACK,
                anchor='e',
                activeforeground='white',
                activebackground=CINZA,
                selectcolor=CINZA,
                bg=CINZA,
                font=('Arial', 12, 'bold'),
                command=optmonth,
                value=val).place(x=60 + incr, y=340)
    incr += 200

window.mainloop()
