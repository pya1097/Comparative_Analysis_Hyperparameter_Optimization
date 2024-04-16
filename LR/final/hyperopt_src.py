from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from hyperopt import hp, tpe, fmin, Trials
import warnings
import os
import shutil

script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, 'hyperopt_outputs')

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

inputs = ['digits','gendervoice','breastcancer','iris','whitewine','socialnetworkads','heartdisease','titanic','employeeattrition','pumpkinseeds','marketing','bankloan','date','fakebills','empturnover','cancer','wine','kidneystone','mineorrock','possum']
n_trials_list = [1,2] #50,100,200,500
iters =20

params = {
    'tol' : hp.uniform('tol' , 1e-6 , 1e-3),
    'C' : hp.loguniform("C", 1e-2, 1),
    'max_iter' : hp.quniform('max_iter', 100, 5000, 100),
    'fit_intercept' : hp.choice('fit_intercept', [True, False]),
    'penalty' : hp.choice('penalty', ['l2', 'none'])
}

for inputf in inputs:
    acc_dict = {}
    for n_trials in n_trials_list:
        with open((os.path.join(output_dir,inputf+'.txt')), 'a') as file:
            file.write('\n_______________________________\nhyperopt' + str(n_trials)+'\n_______________________________\n')
        acc_list = []
        acc = 0
        i = iters
        while i > 0:
            X = pd.read_csv(os.path.join(script_dir,inputf+'_X.csv')).values
            y = pd.read_csv(os.path.join(script_dir,inputf+'_y.csv')).values
            tpe_algo = tpe.suggest
            trials = Trials()
            best_params = fmin(fn=objective,space=params,algo=tpe_algo,max_evals=n_trials,trials=trials)
            best_loss = min(trials.losses())
            acc_list.append(-best_loss)
            acc += -float(best_loss)
            with open((os.path.join(output_dir,inputf+'.txt')), 'a') as file:
                file.write('\n\nthe best params:' + str(best_params))
                file.write('\nthe best value:' + str(-best_loss))
            i -= 1
        with open((os.path.join(output_dir,inputf+'.txt')), 'a') as file:
            file.write('\n*****************************\nAverage optimal accuracy:' + str(acc/iters)+'\n*****************************\n')
        acc_dict['hyperopt'+str(n_trials)] = acc_list
    with open((os.path.join(output_dir,inputf+'.txt')), 'a') as file:
        file.write('\n*****************\n\n*****************\n' + str(acc_dict)+'\n*****************\n\n*****************\n')