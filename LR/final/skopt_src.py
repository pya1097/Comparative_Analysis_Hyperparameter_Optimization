from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from skopt import BayesSearchCV
from skopt.space import Real, Categorical, Integer
import warnings
import os
import shutil
import time

script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, 'skopt_outputs')

if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir, exist_ok=True)

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

def objective(params):
  params['max_iter'] = int(params['max_iter'])
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=23)
  logistic = linear_model.LogisticRegression(**params)
  accuracy = logistic.fit(X_train, y_train).score(X_test, y_test)

  return -accuracy

# inputs = ['digits','breastcancer','iris','whitewine','socialnetworkads','heartdisease','titanic','employeeattrition','pumpkinseeds','marketing','bankloan','date','fakebills','empturnover','cancer','wine','kidneystone','mineorrock','gendervoice','possum']
inputs = ['digits','breastcancer']
n_trials_list = [6,14,20,60,100] #50,100,200,500
iters =20

param_space = {
    'C': Real(1e-6, 1e+6, prior='log-uniform'),
    'penalty': Categorical([None, 'l2']),
    'max_iter': Integer(50, 5000),
    'tol': Real(1e-6, 1e-2, prior='uniform'),
    'fit_intercept': Categorical([True, False])
}

res = {}
for inputf in inputs:
    acc_dict = {}
    time_dict = {}
    res[inputf] = {}
    for n_trials in n_trials_list:
        start_time = time.time()
        with open((os.path.join(output_dir,inputf+'.txt')), 'a') as file:
            file.write('\n_______________________________\nskopts' + str(n_trials)+'\n_______________________________\n')
        acc_list = []
        acc = 0
        i = iters
        while i > 0:
            X = pd.read_csv(os.path.join(script_dir,inputf+'_X.csv')).values
            y = pd.read_csv(os.path.join(script_dir,inputf+'_y.csv')).values
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=23)
            logistic = linear_model.LogisticRegression()
            opt = BayesSearchCV(logistic,param_space,scoring='accuracy',n_iter=n_trials,cv=2,verbose=1)
            opt.fit(X_train, y_train)
            acc_list.append(opt.best_score_)
            acc += float(opt.best_score_)
            with open((os.path.join(output_dir,inputf+'.txt')), 'a') as file:
                file.write('\n\nthe best params:' + str(opt.best_params_))
                file.write('\nthe best value:' + str(opt.best_score_))
            i -= 1
        with open((os.path.join(output_dir,inputf+'.txt')), 'a') as file:
            file.write('\n*****************************\nAverage optimal accuracy:' + str(acc/iters)+'\n*****************************\n')
        end_time = time.time()
        acc_dict['skopt'+str(n_trials)] = acc_list
        acc_r_list = [round(x, 2) for x in acc_list]
        res[inputf]['skopt'+str(n_trials)] = acc_r_list
        time_dict['skopt'+str(n_trials)] = end_time - start_time
    with open((os.path.join(output_dir,inputf+'.txt')), 'a') as file:
        file.write('\n---------------------\nAccuracy\n---------------------\n' + str(acc_dict)+'\n---------------------\n')
        file.write('\n---------------------\nTime\n---------------------\n' + str(time_dict)+'\n---------------------\n')
with open((os.path.join(output_dir,'skopt_final.txt')), 'a') as file:
    file.write('\n---------------------\nAggregate\n---------------------\n' + str(res)+'\n---------------------\n')
    
    