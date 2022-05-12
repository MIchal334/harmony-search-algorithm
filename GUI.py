import math
from tkinter import *

import GUI2
from main import main_start
from tkinter import messagebox


def start_program(function_filed, x_min_filed, x_max_filed, amount_var, HMCR, HMS, PAR, iterrations, B, root):
    try:
        fun = analize(function_filed)
        minimum_tab = extremum_analize(x_min_filed + "\n")
        maximum_tab = extremum_analize(x_max_filed + "\n")
        isOK = check_data(amount_var, HMCR, HMS, PAR, iterrations, B, minimum_tab, maximum_tab)
        if isOK:
            results = main_start(int(HMS), float(HMCR), float(PAR), float(B), int(amount_var), int(iterrations),
                                 maximum_tab,
                                 minimum_tab,
                                 fun)
            root.destroy()
            GUI2.start_calculations(results, int(amount_var), int(iterrations), function_filed, x_min_filed,
                                    x_max_filed, HMS,
                                    HMCR,
                                    PAR, B, int(100))


    except:
        messagebox.showwarning("Błąd", "Wystąpił nieoczekiwany błąd. Proszę sprawdź wszystkie dane")


def check_data(amount_var, HMCR, HMS, PAR, iterrations, B, min_tab, max_tab):
    if int(amount_var) <= 0 or float(HMCR) < 0 or int(HMS) <= 0 or float(PAR) < 0 or int(iterrations) <= 0 or float(
            B) < 0:
        messagebox.showwarning("Błąd wejciowy", "Paremetry wejciowe powinny być większe od 0")
        return False
    if float(HMCR) > 1 or float(PAR) > 1:
        messagebox.showwarning("Błąd", "Prawdopodństwo HMCR oraz PAR powinno być miejsze niż 1")
        return False

    if int(amount_var) > 5:
        messagebox.showwarning("Błąd", "Maxmalna liczba zmiennych to 5")
        return False

    if len(min_tab) != int(amount_var):
        messagebox.showwarning("Błąd", "Błądy wymiar tablicy minimów")
        return False

    if len(max_tab) != int(amount_var):
        messagebox.showwarning("Błąd", "Błądy wymiar tablicy maximow")
        return False

    if len(min_tab) != len(max_tab):
        messagebox.showwarning("Błąd", "Różne wymiary tablicy minimów i maximów")
        return False

    if check_max_and_min(min_tab, max_tab):
        messagebox.showwarning("Błąd", "Jedno z maxmimów jest mniejsze lub równe minimum")
        return False

    if check_B(min_tab, max_tab, B):
        messagebox.showwarning("Błąd", "Parametr B jest za duży względem minimów i maximów")
        return False

    return True


def check_max_and_min(min_tab, max_tab):
    for i in range(len(min_tab)):
        temp_min = min_tab[i]
        temp_max = max_tab[i]
        if temp_max <= temp_min:
            return True

    return False


def check_B(min_tab, max_tab, B):
    diffrence_tab = []

    for i in range(len(min_tab)):
        temp_min = min_tab[i]
        temp_max = max_tab[i]
        diffrence_tab.append(abs(temp_max - temp_min))

    min_dif = min(diffrence_tab)

    if float(B) > min_dif / 2:
        return True

    return False


def analize(fun):
    fun = fun.lower()
    list_try = ["sin", "cos", "tan", "exp"]
    index = []

    for x in list_try:
        if x in fun:
            cout = fun.count(x)
            temp_c = 0
            start = 0
            while temp_c < cout:
                tmep_index = fun.find(x, start)
                index.append(tmep_index)
                start = start + tmep_index + 1
                temp_c = temp_c + 1

    index = sorted(index)
    print(index)
    fun = add_math_world(fun, index)
    print("WYYNIK TO ", fun)
    return fun


def clear(fun_filed, X_min_filed, X_max_filed, amount_var_filed, HMS_filed, HMCR_filed, PAR_filed, iterrations_filed,
          b_f):
    fun_filed.delete(0, END)
    X_min_filed.delete(0, END)
    X_max_filed.delete(0, END)
    amount_var_filed.delete(0, END)
    HMS_filed.delete(0, END)
    HMCR_filed.delete(0, END)
    PAR_filed.delete(0, END)
    iterrations_filed.delete(0, END)
    b_f.delete(0, END)


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
    world = "math."
    sum = 0
    for i in indexes:
        str1 = str[0:i + sum]
        str2 = world + str[i + sum:]
        str = str1 + str2
        sum = sum + len(world)
    return str


# Init Button and filed


def main(fun_f, x_min_f, x_max_f, amount_f, hms_f, hmcr_f, par_f, iter_f, b_f):
    root = Tk()
    root.title("HS-Program")

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
                                                        PAR_filed.get(), iterrations_filed.get(), B_filed.get(), root))

    clear_button = Button(frame_controler, text="Wyczyść", padx=5, pady=5,
                          command=lambda: clear(fun_filed, X_min_filed, X_max_filed, amount_var_filed, HMS_filed,
                                                HMCR_filed, PAR_filed, iterrations_filed, B_filed))
    fx_text = Label(frame_input, text="F(X) = ")
    xmin_text = Label(frame_input, text="Xmin =")
    xmax_text = Label(frame_input, text="Xmax =")
    amount_var_text = Label(frame_data, text="Ilość zmiennych = ")
    HMS_text = Label(frame_data, text="HMS=")
    HMCR_text = Label(frame_data, text="HMCR=")
    PAR_text = Label(frame_data, text="PAR=")
    iter_text = Label(frame_data, text="Iterracje=")
    B_text = Label(frame_data, text="B=")

    frame_input.grid(column=0, row=0)
    frame_data.grid(column=1, row=0)
    frame_controler.grid(column=0, row=1, columnspan=2)
    # Place of components
    fx_text.grid(row=0, column=0)
    fun_filed.grid(row=0, column=1, columnspan=4, padx=10, pady=10)
    fun_filed.insert(0, fun_f)

    xmin_text.grid(row=1, column=0)
    X_min_filed.grid(row=1, column=1, columnspan=4, padx=10, pady=10)
    X_min_filed.insert(0, x_min_f)

    xmax_text.grid(row=2, column=0)
    X_max_filed.grid(row=2, column=1, columnspan=4, padx=10, pady=10)
    X_max_filed.insert(0, x_max_f)

    amount_var_text.grid(row=0, column=0)
    amount_var_filed.grid(row=0, column=1)
    amount_var_filed.insert(0, amount_f)

    HMS_text.grid(row=1, column=0)
    HMS_filed.grid(row=1, column=1)
    HMS_filed.insert(0, hms_f)

    HMCR_text.grid(row=2, column=0)
    HMCR_filed.grid(row=2, column=1)
    HMCR_filed.insert(0, hmcr_f)

    PAR_text.grid(row=3, column=0)
    PAR_filed.grid(row=3, column=1)
    PAR_filed.insert(0, par_f)

    iter_text.grid(row=4, column=0)
    iterrations_filed.grid(row=4, column=1)
    iterrations_filed.insert(0, iter_f)

    B_text.grid(row=5, column=0)
    B_filed.grid(row=5, column=1)
    B_filed.insert(0, b_f)

    start_button.grid(row=0, column=0)
    clear_button.grid(row=0, column=1)

    root.mainloop()


if __name__ == '__main__':
    fun_f = "x1+x2"
    x_min_f = "-5;-5"
    x_max_f = "5;5"
    amount_f = "2"
    hms_f = "10"
    hmcr_f = "0.8"
    par_f = "0.3"
    iter_f = "1000"
    b_f = "1"
    main(fun_f, x_min_f, x_max_f, amount_f, hms_f, hmcr_f, par_f, iter_f, b_f)
