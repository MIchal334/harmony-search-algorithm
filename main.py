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
    cout = 0
    for i in range(len(results_tab)):
        if results_tab[i].fx > new_fx:
            break
        cout = cout + 1
    return cout


def shift_key(results_tab, key):
    for i in range(len(results_tab), key, -1):
        temp_obj = results_tab[i-1]
        results_tab[i] = temp_obj

    return  results_tab


def generate_start_value(size, amount_of_var, X_max, X_min):
    results = {}
    results.clear()
    obj = {}
    key = 0

    for i in range(size):
        X = []
        fx = 0

        for j in range(amount_of_var):
            X.append((X_max[j] - X_min[j]) * random.random() + X_min[j])

        fx = Fx(X)
        obj = Result(X, fx)

        key = find_new_key(results, fx)

        if key < len(results):
           results =  shift_key(results, key)

        results[key] = obj

    return results


def show_table(results_table, cout_value):
    for i in range(len(results_table)):
        info = ""
        info = info + "Nr " + str(i)

        for j in range(cout_value):
            info = info + " X" + str((j + 1)) + " = " + str(results_table[i].X[j])

        info = info + " f(x) = " + str(results_table[i].fx)

        print(info)


if __name__ == '__main__':
    HMS = 10
    HMCR = 0.85
    PAR = 0.45
    b = 10
    amount_of_var = 2

    step = 0
    X = []
    X_max = [10, 10] # Kolejno minima i maximna dla X1,X2,...,XN
    X_min = [-10, -10]

    results_table = generate_start_value(HMS, amount_of_var, X_max, X_min)

    show_table(results_table, amount_of_var)
