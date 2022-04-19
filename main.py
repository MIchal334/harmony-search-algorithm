import random
import matplotlib.pyplot as plt
import numpy as np
import __future__


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


# def Fx(X):
#     # return 4 * X[0] - 2.1 * math.pow(X[1], 4.0) + (1 / 3) * math.pow(X[0], 6.0) + X[0] * X[1] - 4 * math.pow(X[1],2.0) + 4 * math.pow(X[1], 4.0)
#     # num1 = pow(X[0], 2.0) + X[1] - 11
#     # num2 = X[0] + pow(X[1], 2.0) - 7
#     return pow(num1, 2.0) + pow(num2, 2.0)


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
        X_l = np.arange(X_min[0], X_max[0], 0.1)
        Y_l = np.arange(X_min[1], X_max[1], 0.1)
        x1, x2 = np.meshgrid(X_l, Y_l)
        Z = eval(fun)
        plt.scatter(the_best_point_x, the_best_point_y, c="r")

        for i in range(len(the_best_point_x)):
            plt.annotate("Iter "+str((i+1)*10)+"%", (the_best_point_x[i], the_best_point_y[i]), c="red")

        plt.imshow(Z, extent=[X_min[0] - 1, X_max[0] + 1, X_min[1] - 1, X_max[1] + 1])
        plt.imshow(Z, extent=[min(the_best_point_x) - 1, max(the_best_point_x) + 1, min(the_best_point_y) - 1, max(the_best_point_y) + 1])
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
        draw(X_max, X_min, fun, X_var, the_best_point_x, the_best_point_y)


    return results
    # for i in range(4):
    #     print()
    #
    # print("Wynik calosci")
    # iter = 0
    # for r in results:
    #     print()
    #     print("Dla ", (iter + 1) * graph_step)
    #     # print(r)
    #     show_table(r, amount_of_var)
    #     iter = iter + 1
