import math
from config import the
from helper import *
import warnings
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

class ROW:
    # Initializing ROW instance
    def __init__(self, t):
        self.cells = t

    # # Distance to best values (and _lower_ is _better_).
    # def d2h(self, data):
    #     d, n, p = 0, 0, 2
    #     for col in data.cols.y:
    #         n += 1
    #         d += abs(col.heaven - col.norm(self.cells[col.at])) ** p
    #     return math.sqrt(d) / math.sqrt(n)
    
    
    def d2h(self, data=None):
        warnings.filterwarnings("ignore", message="Setting penalty=None will ignore the C and l1_ratio parameters")
        if(len(self.cells)==6):
            X, y = datasets.load_iris(return_X_y=True)
            X = X / X.max()
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=23)
            logistic = linear_model.LogisticRegression(max_iter=int(self.cells[0]), C=(self.cells[1]), tol=self.cells[2], fit_intercept=self.cells[3], dual=self.cells[4], penalty=self.cells[5])
            score = round(logistic.fit(X_train, y_train).score(X_test, y_test),3)
            self.cells.append(score)
            return score
        else:
            return self.cells[6]

    # Minkowski dsitance (the.p=1 is taxicab/Manhattan; the.p=2 is Euclidean)
    def dist(self, other, data):
        d, n, p = 0, 0, 2
        for col in data.cols.x:
            n += 1
            d += col.dist(self.cells[col.at], other.cells[col.at]) ** p
        return (d / n) ** (1 / p)

    def neighbors(self, data, rows=None):
        return keysort(rows or data.rows, fun=lambda row: self.dist(row, data))

   