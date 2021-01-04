import time
from tkinter import *
from tkcalendar import *

BLACK = '#000000'
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
BLUE = '#0000CD'
FONT_NAME = "Courier"

window = Tk()
window.title('Steag Energy Services')
window.config(padx=20, pady=20, bg=BLUE)
t = time.localtime()


def get_startdate():
    start_label.config(text=calend.get_date())


def get_finishdate():
    finish_label.config(text=calend.get_date())


def optmonth():
    return opt_radio.get()


canvas = Canvas(width=400, height=100)
canvas.config(bg=BLUE, highlightthickness=0)
steag_file = PhotoImage(file='steag1.png')
canvas.create_image(300, 40, image=steag_file)
# timer_text = canvas.create_text(50, 30, text='00:00', font=(FONT_NAME, 26, 'bold'), fill='white')
canvas.grid(row=0, column=1)

calend = Calendar(window, selectmode='day', year=t[0], month=t[1], day=t[2], locale='pt_BR', date_pattern='dd/mm/y',
                  showweeknumbers=False, firstweekday='sunday', showothermonthdays=False)
calend.grid(row=3, column=2)

# timer_label = Label(text='Timer', fg=GREEN, bg=BLUE, font=(FONT_NAME, 30, 'bold'))
# timer_label.grid(row=0, column=1)

start_buttom = Button(text='Selecionar', font=(FONT_NAME, 12, 'bold'), command=get_startdate)
start_buttom.place(x=300, y=130)

reset_buttom = Button(text='Selecionar', font=(FONT_NAME, 12, 'bold'), command=get_finishdate)
reset_buttom.place(x=300, y=200)

run_buttom = Button(text='Submit', font=(FONT_NAME, 12, 'underline'), command=get_finishdate)
run_buttom.grid(row=5, column=2)

label_date1 = Label(text='Data Inicial:', fg='white', bg=BLUE, font=(FONT_NAME, 14, 'bold'))
label_date1.place(x=10, y=130)

label_date2 = Label(text='Data Final:', fg='white', bg=BLUE, font=(FONT_NAME, 14, 'bold'))
label_date2.place(x=10, y=200)

label_plan = Label(text='Escolha uma das plantas disponíveis nesta aplicação:', fg='white', bg=BLUE,
                   font=(FONT_NAME, 12, 'bold'))
label_plan.grid(row=4, column=1)

start_label = Label(text='', fg='white', bg=BLUE, font=(FONT_NAME, 14, 'bold'))
start_label.place(x=160, y=130)

finish_label = Label(text='', fg='white', bg=BLUE, font=(FONT_NAME, 14, 'bold'))
finish_label.place(x=160, y=200)

opt_radio = IntVar()
opt_radio.set(1)
month = [("são pedro", 1), ("juazeiro", 2), ("sol do futuro", 3)]

# Construção dos radio buttom da interface gráfica
incr = 0
for plant, val in month:
    Radiobutton(window,
                text=plant,
                padx=20,
                variable=opt_radio,
                fg='white',
                anchor='e',
                activeforeground=BLACK,
                activebackground='blue',
                selectcolor=BLUE,
                bg=BLUE,
                font=('Arial', 15, 'bold'),
                command=optmonth,
                value=val).place(x=5 + incr, y=300)
    incr += 160

window.mainloop()
