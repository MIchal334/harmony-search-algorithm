import math
from tkinter import *

root = Tk()
root.title("HS-Program")


def start_program(function_filed, x_min_filed, x_max_filed, amount_var):
    analize(function_filed)
    minimum_tab = extremum_analize(x_min_filed + "\n")
    maximum_tab = extremum_analize(x_max_filed + "\n")
    return


def analize(fun):
    fun = fun.lower()
    list_try = ["sin", "cos", "tg", "ctg"]
    index = []

    for x in list_try:
        if x in fun:
            index.append(fun.find(x))
    fun = add_math_world(fun, index)
    Fx([math.pi / 2, 2], fun)
    return


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


def Fx(X, function):
    x = X[0]
    y = X[1]
    sum = eval(function)
    print(sum)


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
fun_filed = Entry(root, width=70)
X_min_filed = Entry(root, width=50)
X_max_filed = Entry(root, width=50)
amount_var_filed = Entry(root, width=8)
HMCR_filed = Entry(root, width=8)
HMS_filed = Entry(root, width=8)
PAR_filed = Entry(root, width=8)

start_button = Button(text="Start",
                      command=lambda: start_program(fun_filed.get(), X_min_filed.get(), X_max_filed.get(),
                                                    amount_var_filed.get()))

clear_button = Button(text="Clear", command=clear)
fx_text = Label(root, text="F(X) = ")
xmin_text = Label(root, text="Xmin =")
xmax_text = Label(root, text="Xmax =")
amount_var_text = Label(root, text="Amount of\n Variable = ")
HMS_text = Label(root,text="HMS=")
HMCR_text = Label(root,text="HMCR=")
PAR_text = Label(root,text="PAR=")

# Place of components
fx_text.grid(row=0, column=0)
fun_filed.grid(row=0, column=1, columnspan=7, padx=10, pady=10)

xmin_text.grid(row=1, column=0)
X_min_filed.grid(row=1, column=1, columnspan=4, padx=10, pady=10)

xmax_text.grid(row=2, column=0)
X_max_filed.grid(row=2, column=1, columnspan=4, padx=10, pady=10)

amount_var_text.grid(row=3, column=0)
amount_var_filed.grid(row=3, column=1)
HMS_text.grid(row=3, column=2)
HMS_filed.grid(row=3, column=3)
HMCR_text.grid(row=3, column=4)
HMCR_filed.grid(row=3, column=5)
PAR_text.grid(row=3, column=6)
PAR_filed.grid(row=3, column=7)


start_button.grid(row=4, column=1)
clear_button.grid(row=4, column=2)

root.mainloop()
