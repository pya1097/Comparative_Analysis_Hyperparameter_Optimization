import math
from config import the

from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import warnings
from sklearn.exceptions import DataConversionWarning,ConvergenceWarning

class ROW:
    # Initializing ROW instance
    def __init__(self, t):
        self.cells = t


    def d2h(self,input, data=None):
        warnings.filterwarnings("ignore", message="Setting penalty=None will ignore the C and l1_ratio parameters")
        warnings.filterwarnings("ignore", category=DataConversionWarning)
        warnings.filterwarnings("ignore", category=ConvergenceWarning)
        if(len(self.cells)==6):
            X, y = pd.read_csv("se_data/"+input+"_X.csv"),pd.read_csv("se_data/"+input+"_y.csv")
            # X = X / X.max()
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=23)
            logistic = linear_model.LogisticRegression(max_iter=int(self.cells[0]), C=(self.cells[1]), tol=self.cells[2], fit_intercept=self.cells[3], dual=self.cells[4], penalty=self.cells[5])
            score = round(logistic.fit(X_train, y_train).score(X_test, y_test),3)
            self.cells.append(score)
            return score
        else:
            return self.cells[6]
        

    #Finding out how much a row likes the data
    def like(self, data, n, nHypotheses, the):
        # print(the)
        prior = (len(data.rows) + the['k']) / (n + the['k'] * nHypotheses)
        out = math.log(prior)

        for col in data.cols.x:
            v = self.cells[col.at]
            if v != "?":
                inc = col.like(v, prior, the)
                if inc == 0:
                    out += float('-inf')
                else:
                    out += math.log(inc)

        return math.exp(1) ** out
    
    # Classifier
    def likes(self,datas):
        n, nHypotheses = 0, 0
        most, out = None, None
        # print(the)

        for k, data in datas.items():
            n += len(data.rows)
            nHypotheses += 1

        for k, data in datas.items():
            tmp = self.like(data, n, nHypotheses, the)
            if most is None or tmp > most:
                most, out = tmp, k

        return out, most
