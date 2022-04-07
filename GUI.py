import math
from tkinter import *
from main import main_start

root = Tk()
root.title("HS-Program")


def start_program(function_filed, x_min_filed, x_max_filed, amount_var, HMCR, HMS, PAR, iterrations, B):
    fun = analize(function_filed)
    minimum_tab = extremum_analize(x_min_filed + "\n")
    maximum_tab = extremum_analize(x_max_filed + "\n")
    main_start(HMS,HMCR,PAR,B,amount_var,iterrations,maximum_tab,minimum_tab,fun)


def analize(fun):
    fun = fun.lower()
    list_try = ["sin", "cos", "tg", "ctg"]
    index = []

    for x in list_try:
        if x in fun:
            index.append(fun.find(x))
    fun = add_math_world(fun, index)
    return fun


def clear():
    fun_filed.delete(0, END)


def extremum_analize(extrema_str):
    X = []

    number = ""

    for c in extrema_str:

        if c == ";" or c == "\n":
            X.append(int(number))
            number = ""
        else:
            number = number + c

    return X


def add_math_world(str, indexes):
    print(str)
    for i in indexes:
        str1 = str[0:i]
        print(str1)
        str2 = "math." + str[i:]
        print(str2)
        str = str1 + str2
    print(str)
    return str


# Init Button and filed

frame_input = LabelFrame(root, text="dane wejsciowe", padx=15, pady=15)
frame_data = LabelFrame(root, text="parametry wejśsciowe", padx=15, pady=15)
frame_controler = LabelFrame(root, padx=5, pady=5)
fun_filed = Entry(frame_input, width=50)
X_min_filed = Entry(frame_input, width=50)
X_max_filed = Entry(frame_input, width=50)
amount_var_filed = Entry(frame_data, width=10)
HMCR_filed = Entry(frame_data, width=10)
HMS_filed = Entry(frame_data, width=10)
PAR_filed = Entry(frame_data, width=10)
iterrations_filed = Entry(frame_data, width=10)
B_filed = Entry(frame_data, width=10)

start_button = Button(frame_controler, text="Start", padx=5, pady=5,
                      command=lambda: start_program(fun_filed.get(), X_min_filed.get(), X_max_filed.get(),
                                                    amount_var_filed.get(), HMCR_filed.get(), HMS_filed.get(),
                                                    PAR_filed.get(), iterrations_filed.get(), B_filed.get()))

clear_button = Button(frame_controler, text="Clear", padx=5, pady=5, command=clear)
fx_text = Label(frame_input, text="F(X) = ")
xmin_text = Label(frame_input, text="Xmin =")
xmax_text = Label(frame_input, text="Xmax =")
amount_var_text = Label(frame_data, text="Amount of\n Variable = ")
HMS_text = Label(frame_data, text="HMS=")
HMCR_text = Label(frame_data, text="HMCR=")
PAR_text = Label(frame_data, text="PAR=")
iter_text = Label(frame_data, text="Iterations=")
B_text = Label(frame_data, text="B=")

frame_input.grid(column=0, row=0)
frame_data.grid(column=1, row=0)
frame_controler.grid(column=0, row=1, columnspan=2)
# Place of components
fx_text.grid(row=0, column=0)
fun_filed.grid(row=0, column=1, columnspan=4, padx=10, pady=10)

xmin_text.grid(row=1, column=0)
X_min_filed.grid(row=1, column=1, columnspan=4, padx=10, pady=10)

xmax_text.grid(row=2, column=0)
X_max_filed.grid(row=2, column=1, columnspan=4, padx=10, pady=10)

amount_var_text.grid(row=0, column=0)
amount_var_filed.grid(row=0, column=1)
HMS_text.grid(row=1, column=0)
HMS_filed.grid(row=1, column=1)
HMCR_text.grid(row=2, column=0)
HMCR_filed.grid(row=2, column=1)
PAR_text.grid(row=3, column=0)
PAR_filed.grid(row=3, column=1)
iter_text.grid(row=4, column=0)
iterrations_filed.grid(row=4, column=1)
B_text.grid(row=5, column=0)
B_filed.grid(row=5, column=1)

start_button.grid(row=0, column=0)
clear_button.grid(row=0, column=1)

root.mainloop()
