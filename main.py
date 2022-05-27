import random
import matplotlib.pyplot as plt
import numpy as np
import math
import threading

class Result:

    def __init__(self, X, fx):
        self.X = X
        self.fx = fx


def Fx(X, function):
    for i in range(len(X)):
        temp_str = "x" + str(i + 1)
        exec("%s = %f" % (temp_str, X[i]))

    sum = eval(function)
    return round(sum, 4)


def find_new_key(results_tab, new_fx):
    amount = 0
    for i in range(len(results_tab)):
        if results_tab[i].fx > new_fx:
            break
        amount = amount + 1
    return amount


def shift_key(results_tab, key, size_max):
    for i in range(len(results_tab), key, -1):
        if i < size_max:
            temp_obj = results_tab[i - 1]
            results_tab[i] = temp_obj

    return results_tab


def generate_start_value(size, amount_of_var, X_max, X_min, fun):
    results_tab = {}
    results_tab.clear()
    obj = {}
    key = 0

    for i in range(size):
        X = create_list_of_random_value(X_max, X_min, amount_of_var)
        results_tab = add_new_value_to_list(X, results_tab, size, fun)
    return results_tab


def add_new_value_to_list(X, results, size, fun):
    fx = Fx(X, fun)
    obj = Result(X, fx)
    key = find_new_key(results, fx)
    if key < size:
        results = shift_key(results, key, size)
        results[key] = obj
    return results


def create_list_of_random_value(X_max, X_min, amount_of_var):
    X = []
    for j in range(amount_of_var):
        X.append(round(random_from_range(X_min[j], X_max[j]), 4))
    return X


def show_table(results_table, cout_value):
    for i in range(len(results_table)):
        info = ""
        info = info + "Nr " + str(i)

        for j in range(cout_value):
            info = info + " X" + str((j + 1)) + " = " + str(results_table[i].X[j])

        info = info + " f(x) = " + str(results_table[i].fx)

        print(info)


def random_from_range(A, B):
    return (B - A) * random.random() + A


def draw(X_max, X_min, fun, X_var, the_best_point_x, the_best_point_y):
    print(the_best_point_x)

    if len(X_var) == 2:
        Xl = np.arange(X_min[0], X_max[0], 0.1)
        Yl = np.arange(X_min[1], X_max[1], 0.1)
        x1, x2 = np.meshgrid(Xl, Yl)
        fun = fun.replace("math", "np")
        Z = eval(fun)
        # for i in range(len(the_best_point_x)):
        #     plt.annotate("Iter "+str((i+1)*10)+"%", (the_best_point_x[i], the_best_point_y[i]), c="red")

        for i in range(len(the_best_point_x) - 1):
            xi = the_best_point_x[i]
            yi = the_best_point_y[i]
            xii = the_best_point_x[i + 1]
            yii = the_best_point_y[i + 1]
            dx = xii - xi
            dy = yii - yi
            plt.arrow(x=xi, y=yi,
                      dx=dx, dy=dy, width=.02)

    # plt.imshow(Z, extent=[min(the_best_point_x) - 1, max(the_best_point_x) + 1, min(the_best_point_y) - 1,
    #                       max(the_best_point_y) + 1])
    plt.contourf(Z, extent=[min(the_best_point_x) - 1, max(the_best_point_x) + 1, min(the_best_point_y) - 1,
                          max(the_best_point_y) + 1])
    plt.colorbar()
    plt.show()


def main_start(HMS, HMCR, PAR, b, amount_of_var, amount_of_step, X_max, X_min, fun):
    X = []
    results_table = generate_start_value(HMS, amount_of_var, X_max, X_min, fun)
    threshold1 = HMCR * (1 - PAR)
    threshold2 = HMCR * PAR
    threshold3 = 1 - HMCR
    results = []
    the_best_point_x = []
    the_best_point_y = []
    graph_step = amount_of_step / 10

    show_table(results_table, amount_of_var)

    iterrator = 0
    for i in range(amount_of_step):
        X_var = []
        x_list = []
        decision_var = random.random()

        if decision_var <= threshold1:
            for j in range(amount_of_var):
                row_number = random.randint(0, HMS - 1)
                X_var.append(results_table[row_number].X[j])
            results_table = add_new_value_to_list(X_var, results_table, HMS, fun)

        elif decision_var <= (threshold2 + threshold1):
            for j in range(amount_of_var):
                correction = random_from_range(-b, b)
                row_number = random.randint(0, HMS - 1)
                temp_value = results_table[row_number].X[j]
                temp_value = round(temp_value + correction, 4)

                if temp_value < X_min[j]:
                    temp_value = X_min[j]

                if temp_value > X_max[j]:
                    temp_value = X_max[j]

                X_var.append(temp_value)

            results_table = add_new_value_to_list(X_var, results_table, HMS, fun)

        else:
            X_var = create_list_of_random_value(X_max, X_min, amount_of_var)
            results_table = add_new_value_to_list(X_var, results_table, HMS, fun)

        if iterrator == graph_step:
            results.append(results_table.copy())
            if amount_of_var == 2:
                the_best_point_x.append(results_table[0].X[0])
                the_best_point_y.append(results_table[0].X[1])
            iterrator = 1
        else:
            iterrator = iterrator + 1

    results.append(results_table.copy())
    if amount_of_var == 2:
        the_best_point_x.append(results_table[0].X[0])
        the_best_point_y.append(results_table[0].X[1])
        th = threading.Thread(target=lambda: draw(X_max, X_min, fun, X_var, the_best_point_x, the_best_point_y))
        th.start()


    return results
