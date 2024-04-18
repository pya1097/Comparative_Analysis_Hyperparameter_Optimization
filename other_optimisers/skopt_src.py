import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from skopt import gp_minimize
from skopt.space import Real, Integer
import warnings
import time
import os
import pandas as pd

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

# inputs = ['digits','gendervoice','breastcancer','iris','whitewine','socialnetworkads','heartdisease','titanic','employeeattrition','pumpkinseeds','marketing','bankloan','date','fakebills','empturnover','cancer','wine','kidneystone','mineorrock','possum']
inputs = ['dtlz2','dtlz3','pom3a','pom3b','pom3c','SS-A','SS-B','SS-C','SS-D','Wine_quality']
n_trials_list = [12,20,60,100] 
iters =20

# Define the search space for hyperparameters
space = [
    Real(0.0001, 0.1, name='C'),  # Inverse of regularization strength
    Integer(1, 100, name='max_iter'),  # Maximum number of iterations
    Real(0.0001, 0.9999, name='tol')  # Tolerance for stopping criteria
]

# Define the objective function to minimize (negative mean cross-validated accuracy)
def objective(params):
    C, max_iter, tol = params
    model = LogisticRegression(C=C, max_iter=max_iter, tol=tol)
    return -np.mean(cross_val_score(model, X, y, cv=5, scoring='accuracy'))


script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, 'skopt_outputs')
data_dir = "/Users/priyaandurkar/Documents/Spring 2024/ASE/Project/se_data"

res = {}
for inputf in inputs:
    acc_dict = {}
    time_dict = {}
    res[inputf] = {}
    for n_trials in n_trials_list:
        start_time = time.time()
        with open((os.path.join(output_dir,inputf+'.txt')), 'a') as file:
            file.write('\n_______________________________\nskopt' + str(n_trials)+'\n_______________________________\n')
        acc_list = []
        acc = 0
        i = iters
        while i > 0:
            X = pd.read_csv(os.path.join(data_dir,inputf+'_X.csv')).values
            y = pd.read_csv(os.path.join(data_dir,inputf+'_y.csv')).values
            
            result = gp_minimize(objective, space, n_calls=n_trials, random_state=42)

            # Get the best hyperparameters
            best_params = result.x
            best_score = -result.fun

            acc_list.append(best_score)
            # acc += -float(best_loss)
            with open((os.path.join(output_dir,inputf+'.txt')), 'a') as file:
                file.write('\n\nthe best params:' + str(best_params))
                file.write('\nthe best value:' + str(best_score))
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