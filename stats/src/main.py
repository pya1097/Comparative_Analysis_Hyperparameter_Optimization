
from helper import *
from config import *
import random, statistics
from stats import SAMPLE, eg0

inputs = ['digits','breastcancer','iris','whitewine','socialnetworkads','heartdisease','titanic','employeeattrition','pumpkinseeds','marketing','bankloan','date','fakebills','empturnover','cancer','wine','kidneystone','mineorrock','gendervoice','possum']

stats_data_rrp = {'digits':{'rrp': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.967, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},'breastcancer':{'rrp': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.967, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]}}
stats_data_smo = {'digits':{'smo6': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.967, 1.0, 1.0, 1.0, 1.0, 0.967, 1.0, 1.0, 1.0, 1.0, 0.967, 1.0, 1.0, 1.0], 
              'smo14': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], 
              'smo20': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]},
              'breastcancer':{'smo6': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.967, 1.0, 1.0, 1.0, 1.0, 0.967, 1.0, 1.0, 1.0, 1.0, 0.967, 1.0, 1.0, 1.0], 
              'smo14': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], 
              'smo20': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]}}

stats_data_hyperopt= {'digits': {'hyperopt1': [0.96, 0.97, 0.96, 0.96, 0.96, 0.97, 0.96, 0.97, 0.96, 0.97, 0.97, 0.97, 0.96, 0.96, 0.96, 0.96, 0.96, 0.96, 0.96, 0.96], 'hyperopt2': [0.97, 0.97, 0.96, 0.97, 0.98, 0.96, 0.96, 0.97, 0.98, 0.97, 0.97, 0.98, 0.97, 0.98, 0.97, 0.97, 0.97, 0.97, 0.96, 0.96]}, 'breastcancer': {'hyperopt1': [0.35, 0.35, 0.93, 0.93, 0.96, 0.96, 0.91, 0.96, 0.98, 0.91, 0.96, 0.96, 0.96, 0.96, 0.96, 0.96, 0.96, 0.93, 0.96, 0.93], 'hyperopt2': [0.93, 0.96, 0.96, 0.96, 0.92, 0.93, 0.96, 0.93, 0.96, 0.98, 0.91, 0.35, 0.96, 0.96, 0.96, 0.93, 0.96, 0.92, 0.92, 0.98]}}
stats_data_optuna = {'digits': {'optuna2': [0.96, 0.96, 0.97, 0.96, 0.96, 0.94, 0.96, 0.95, 0.96, 0.96, 0.96, 0.96, 0.96, 0.96, 0.96, 0.96, 0.96, 0.95, 0.94, 0.96], 'optuna3': [0.96, 0.97, 0.96, 0.96, 0.97, 0.96, 0.96, 0.96, 0.96, 0.96, 0.96, 0.96, 0.96, 0.96, 0.96, 0.96, 0.96, 0.96, 0.96, 0.96]}, 'breastcancer': {'optuna2': [0.96, 0.98, 0.98, 0.96, 0.96, 0.34, 0.97, 0.96, 0.96, 0.96, 0.86, 0.96, 0.98, 0.76, 0.96, 0.72, 0.96, 0.82, 0.96, 0.96], 'optuna3': [0.98, 0.96, 0.96, 0.82, 0.96, 0.34, 0.96, 0.96, 0.96, 0.96, 0.96, 0.96, 0.96, 0.98, 0.96, 0.96, 0.96, 0.96, 0.96, 0.98]}}
stats_data_skopt = {'digits': {'skopt1': [0.96, 0.95, 0.95, 0.95, 0.95, 0.92, 0.95, 0.74, 0.39, 0.94, 0.95, 0.93, 0.95, 0.95, 0.95, 0.94, 0.95, 0.95, 0.93, 0.93], 'skopt2': [0.96, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.96, 0.95, 0.94, 0.96, 0.95, 0.96]}, 'breastcancer': {'skopt1': [0.92, 0.94, 0.94, 0.47, 0.91, 0.38, 0.93, 0.94, 0.62, 0.95, 0.94, 0.89, 0.94, 0.94, 0.91, 0.94, 0.9, 0.93, 0.94, 0.93], 'skopt2': [0.94, 0.91, 0.93, 0.89, 0.92, 0.93, 0.93, 0.94, 0.94, 0.62, 0.62, 0.93, 0.93, 0.62, 0.92, 0.93, 0.93, 0.93, 0.94, 0.93]}}


def hw7_part2(sample_list, the):
    print("\n")
    print("\n")
    print("date:{}\nfile:{}\nrepeat:{}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),the['file'],"20"))

    eg0(sample_list)

    print("\n==============================================================================================================================")


if __name__ == "__main__":

    file_output = 'stats_output.txt'

    for input in inputs:
        with open(file_output, 'a') as file:
            file.write('\n_______________________________\nSTATS for dataset ' + str(input)+'\n_______________________________\n')
        sample_list = []
        if input in stats_data_rrp:
            for key, val in stats_data_rrp[input].items():
                sample_list.append(SAMPLE(val, key))
        if input in stats_data_smo:
            for key, val in stats_data_smo[input].items():
                sample_list.append(SAMPLE(val, key))
        if input in stats_data_hyperopt:
            for key, val in stats_data_hyperopt[input].items():
                sample_list.append(SAMPLE(val, key))
        if input in stats_data_optuna:
            for key, val in stats_data_optuna[input].items():
                sample_list.append(SAMPLE(val, key))
        if input in stats_data_skopt:
            for key, val in stats_data_skopt[input].items():
                sample_list.append(SAMPLE(val, key))


        if len(sample_list)>0:
            hw7_part2(sample_list, the)

        with open(file_output, 'a') as file:
            file.write('\n_______________________________\nEND for dataset ' + str(input)+'\n_______________________________\n')

    


