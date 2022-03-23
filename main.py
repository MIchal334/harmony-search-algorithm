import math
from random import seed
import random


class Result:

    def __init__(self, X, fx):
        self.X = X
        self.fx = fx


def Fx(X):
    return 4 * X[0] - 2.1 * math.pow(X[1], 4.0) + (1 / 3) * math.pow(X[0], 6.0) + X[0] * X[1] - 4 * math.pow(X[1],
                                                                                                             2.0) + 4 * math.pow(
        X[1], 4.0)


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


def generate_start_value(size, amount_of_var, X_max, X_min):
    results_tab = {}
    results_tab.clear()
    obj = {}
    key = 0

    for i in range(size):
        X = create_list_of_random_value(X_max, X_min, amount_of_var)
        results_tab = add_new_value_to_list(X, results_tab, size)
    return results_tab


def add_new_value_to_list(X, results, size):
    fx = Fx(X)
    obj = Result(X, fx)
    key = find_new_key(results, fx)
    if key < size:
        results = shift_key(results, key, size)
    results[key] = obj
    return results


def create_list_of_random_value(X_max, X_min, amount_of_var):
    X = []
    for j in range(amount_of_var):
        X.append(random_from_range(X_min[j], X_max[j]))

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


def get_x_list(results_table, j):
    return  None


if __name__ == '__main__':
    HMS = 3
    HMCR = 0.85
    PAR = 0.45
    b = 1
    amount_of_var = 2
    amount_of_step = 10

    step = 0
    X = []
    X_max = [10, 10]  # Kolejno minima i maximna dla X1,X2,...,XN
    X_min = [-10, -10]

    results_table = generate_start_value(HMS, amount_of_var, X_max, X_min)

    threshold1 = HMCR * (1 - PAR)
    threshold2 = HMCR * PAR
    threshold3 = 1 - HMCR

    show_table(results_table, amount_of_var)
    for i in range(4):
        X_var = []
        x_list = []
        decision_var = random.random()

        if decision_var <= threshold1:
            print("P1")
            for j in range(amount_of_var):
                row_number = random.randint(0,HMS)
                X_var.append(results_table[row_number].X[j])
            results_table = add_new_value_to_list(X_var, results_table, HMS)
            show_table(results_table, amount_of_var)

        elif decision_var <= (threshold2 + threshold1):
            print("P2")

            for j in range(amount_of_var):
                correction = random_from_range(-b, b)
                row_number = random.randint(0,HMS)
                temp_value = results_table[row_number].X[j]
                temp_value = temp_value + correction

                if temp_value < X_min[j]:
                    temp_value = X_min[j]

                if temp_value > X_max[j]:
                    temp_value = X_max[j]

                X_var.append(temp_value)

            results_table = add_new_value_to_list(X_var, results_table, HMS)
            show_table(results_table, amount_of_var)

        else:
            print("P3")
            X_var = create_list_of_random_value(X_max, X_min, amount_of_var)
            results_table = add_new_value_to_list(X_var, results_table, HMS)
            show_table(results_table, amount_of_var)
