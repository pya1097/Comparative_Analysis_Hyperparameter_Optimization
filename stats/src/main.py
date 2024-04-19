
from helper import *
from config import *
import random, statistics
from stats import SAMPLE, eg0
from rrp_final_outputs import *
from smo_final_outputs import *
from hyperopt_final_outputs import *
from skopt_final_outputs import *
from optuna_final_outputs import *
from rand_outputs import * 

inputs = ['dtlz2','dtlz3','pom3a','pom3b','pom3c','SS-A','SS-B','SS-C','SS-D','Wine_quality','digits','breastcancer','heartdisease','employeeattrition','marketing','fakebills','empturnover','cancer','kidneystone','gendervoice',]


def hw7_part2(sample_list, the):
    print("\n")
    print("\n")
    print("date:{}\nfile:{}\nrepeat:{}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),the['file'],"20"))

    eg0(sample_list)

    print("\n==============================================================================================================================")


if __name__ == "__main__":

    file_output = 'stats_output_new.txt'

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
        if input in stats_data_rand:
            for key, val in stats_data_rand[input].items():
                sample_list.append(SAMPLE(val, key))


        if len(sample_list)>0:
            hw7_part2(sample_list, the)

        with open(file_output, 'a') as file:
            file.write('\n_______________________________\nEND for dataset ' + str(input)+'\n_______________________________\n')

    


