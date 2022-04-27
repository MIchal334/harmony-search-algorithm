from tkinter import *
from tkinter import ttk
import GUI


option_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


def start_calculations(results, amount_of_var, iteration, fun_f, x_min_f, x_max_f, hms_f, hmcr_f, par_f, b_f, chose_f):
    root = Tk()
    root.title("HS-Program")
    chose = IntVar()
    chose.set(chose_f)

    frame_options = LabelFrame(root, text="Opcje", padx=15, pady=15)
    frame_results = LabelFrame(root, text="Wyniki dla " + str(chose.get()) + "%")

    quit = Button(frame_options, text="Quit", command=root.destroy)
    back = Button(frame_options, text="Back",
                  command=lambda: to_main_menu(fun_f, x_min_f, x_max_f, amount_of_var, hms_f, hmcr_f, par_f, iteration,
                                               b_f,root))
    refreshe = Button(frame_options, text="Refresh",
                      command=lambda: create_new(root, results, amount_of_var, iteration, fun_f, x_min_f, x_max_f,
                                                 hms_f, hmcr_f, par_f, b_f, chose.get()))
    chose_menu = OptionMenu(frame_options, chose, *option_list)

    frame_results.grid(column=0, row=0, rowspan=3)
    frame_options.grid(column=0, row=4)

    quit.grid(column=0, row=0)
    chose_menu.grid(column=1, row=0)
    refreshe.grid(column=2, row=0)
    back.grid(column=3, row=0)

    prepare_tab(frame_results, amount_of_var, results, chose.get())
    root.mainloop()


def to_main_menu(fun_f, x_min_f, x_max_f, amount_f, hms_f, hmcr_f, par_f, iter_f, b_f,root):
    root.destroy()
    GUI.main(fun_f, x_min_f, x_max_f, amount_f, hms_f, hmcr_f, par_f, iter_f, b_f)


def create_new(root, results, amount_of_var, iteration, fun_f, x_min_f, x_max_f,
               hms_f, hmcr_f, par_f, b_f, chose_f):
    root.destroy()
    start_calculations(results, amount_of_var, iteration, fun_f, x_min_f, x_max_f,
                       hms_f, hmcr_f, par_f, b_f, chose_f)


def prepare_tab(frame_results, amount, results, chose):
    my_table = ttk.Treeview(frame_results)
    my_table['columns'] = prepare_column(amount)
    my_table.column("#0", width=0, stretch=NO)
    my_table.column("HMS", anchor=CENTER, width=80)
    for i in range(amount):
        my_table.column("X" + str(i + 1), anchor=CENTER, width=80)
    my_table.column("F(x)", anchor=CENTER, width=80)

    my_table.heading("#0", text="", anchor=CENTER)
    my_table.heading("HMS", text="HMS", anchor=CENTER)

    for i in range(amount):
        my_table.heading("X" + str(i + 1), text="X" + str(i + 1), anchor=CENTER)

    my_table.heading("F(x)", text="F(x)", anchor=CENTER)

    print(chose)
    nr = int((chose / 10) - 1)
    result = results[nr]
    my_table = prepare_data(result, my_table, amount)
    my_table.pack()


def prepare_data(results, my_tab, amount):
    for i in range(len(results)):
        val = prepare_values(amount, i, results)
        my_tab.insert(parent='', index='end', iid=i, text='',
                      values=val)
    return my_tab


def prepare_column(amount):
    colmun = []
    colmun.append('HMS')

    for i in range(amount):
        colmun.append('X' + str(i + 1))

    colmun.append('F(x)')
    return tuple(colmun)


def prepare_values(amount, i, result):
    values = []
    values.append(i)

    for j in range(amount):
        values.append(result[i].X[j])

    values.append(result[i].fx)
    return tuple(values)
