import time
from tkinter import *
from tkcalendar import *

BLACK = '#000000'
CINZA = '#B4B7BF'
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
BLUE = '#0000CD'
FONT_NAME = "Courier"

window = Tk()
window.title('Steag Energy Services')
window.geometry('740x500')
window.config(padx=20, pady=20, bg=BLUE)
t = time.localtime()


def get_startdate():
    start_label.config(text=calend.get_date())


def get_finishdate():
    finish_label.config(text=calend.get_date())


def optmonth():
    # print(opt_radio.get())
    return opt_radio.get()


canvas = Canvas(width=700, height=80)
canvas.config(bg=BLUE, highlightthickness=0)
steag_file = PhotoImage(file='steag1.png')
canvas.create_image(350, 40, image=steag_file)
canvas.grid(row=0, column=0, columnspan=5)

canvas2 = Canvas(width=600, height=60, bg=BLUE, highlightthickness=0)
result = canvas2.create_text(150, 20, text='', font=('Ariel', 10, 'bold'))
canvas2.place(bordermode=OUTSIDE, height=80, width=700, x=20, y=350)

calend = Calendar(window, selectmode='day', year=t[0], month=t[1], day=t[2], locale='pt_BR', date_pattern='dd/mm/y',
                  showweeknumbers=False, firstweekday='sunday', showothermonthdays=False)
calend.grid(row=1, column=3, columnspan=2, rowspan=2)

# timer_label = Label(text='Timer', fg=GREEN, bg=BLUE, font=(FONT_NAME, 30, 'bold'))
# timer_label.grid(row=0, column=1)

start_buttom = Button(text='Selecionar', font=(FONT_NAME, 12, 'bold'), command=get_startdate,
                      activebackground=CINZA, bd=5)
start_buttom.grid(row=1, column=2)

reset_buttom = Button(text='Selecionar', font=(FONT_NAME, 12, 'bold'), command=get_finishdate,
                      activebackground=CINZA, bd=5)
reset_buttom.grid(row=2, column=2)

run_buttom = Button(text='Submit', font=(FONT_NAME, 12, 'underline'), command=optmonth, activebackground=CINZA, bd=5)
run_buttom.place(x=320, y=420)

label_date1 = Label(text='Data Inicial:', fg='white', bg=BLUE, font=(FONT_NAME, 14, 'bold'), padx=2, pady=2)
# label_date1.place(x=10, y=130)
label_date1.grid(row=1, column=0, sticky=W)

label_date2 = Label(text='Data Final:', fg='white', bg=BLUE, font=(FONT_NAME, 14, 'bold'), padx=2, pady=2)
# label_date2.place(x=10, y=200)
label_date2.grid(row=2, column=0, sticky=W)

label_plan = Label(text='Escolha uma das plantas disponíveis:', fg='white', bg=BLUE,
                   font=(FONT_NAME, 14, 'bold'))
label_plan.grid(row=3, column=1, columnspan=3, sticky=W)

start_label = Label(text='', fg='white', bg=BLUE, font=(FONT_NAME, 14, 'bold'), width=10)
# start_label.place(x=160, y=130)
start_label.grid(row=1, column=1, sticky=W)

finish_label = Label(text='', fg='white', bg=BLUE, font=(FONT_NAME, 14, 'bold'), width=10)
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
                fg='white',
                anchor='e',
                activeforeground=BLACK,
                activebackground='blue',
                selectcolor=BLUE,
                bg=BLUE,
                font=('Arial', 12, 'bold'),
                command=optmonth,
                value=val).place(x=60 + incr, y=280)
    incr += 200

window.mainloop()
