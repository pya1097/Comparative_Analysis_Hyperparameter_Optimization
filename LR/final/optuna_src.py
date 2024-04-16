from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import optuna
import warnings
import os
import shutil

script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, 'optuna_outputs')

if os.path.exists(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir, exist_ok=True)

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

def objective(trial):
    params = {
        'tol' : trial.suggest_uniform('tol' , 1e-6 , 1e-3),
        'C' : trial.suggest_loguniform("C", 1e-2, 1),
        'max_iter' : trial.suggest_int('max_iter', 100, 5000, step=100),
        'fit_intercept' : trial.suggest_categorical('fit_intercept', [True, False]),
        'penalty' : trial.suggest_categorical('penalty', ['l2', 'none'])
    }

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=23)
    logistic = linear_model.LogisticRegression(**params)
    accuracy = logistic.fit(X_train, y_train).score(X_test, y_test)
    return accuracy

inputs = ['digits','breastcancer','iris','whitewine','socialnetworkads','heartdisease','titanic','employeeattrition','pumpkinseeds','marketing','bankloan','date','fakebills','empturnover','cancer','wine','kidneystone','mineorrock','gendervoice','possum']
n_trials_list = [2,3] #50,100,200,500
iters = 20

for inputf in inputs:
    acc_dict = {}
    for n_trials in n_trials_list:
        with open((os.path.join(output_dir,inputf+'.txt')), 'a') as file:
            file.write('\n_______________________________\optuna' + str(n_trials)+'\n_______________________________\n')
        acc_list = []
        acc = 0
        i = iters
        while i > 0:
            X = pd.read_csv(os.path.join(script_dir,inputf+'_X.csv')).values
            y = pd.read_csv(os.path.join(script_dir,inputf+'_y.csv')).values
            study = optuna.create_study(direction = 'maximize' , pruner = optuna.pruners.HyperbandPruner())
            study.optimize(objective, n_trials = n_trials)
            acc_list.append(study.best_value)
            acc += float(study.best_value)
            with open((os.path.join(output_dir,inputf+'.txt')), 'a') as file:
                file.write('\n\nthe best params:' + str(study.best_trial.params))
                file.write('\nthe best value:' + str(study.best_value))
            i -= 1
        with open((os.path.join(output_dir,inputf+'.txt')), 'a') as file:
            file.write('\n*****************************\nAverage optimal accuracy:' + str(acc/iters)+'\n*****************************\n')
        acc_dict['optuna'+str(n_trials)] = acc_list
    with open((os.path.join(output_dir,inputf+'.txt')), 'a') as file:
        file.write('\n*****************\n\n*****************\n' + str(acc_dict)+'\n*****************\n\n*****************\n')