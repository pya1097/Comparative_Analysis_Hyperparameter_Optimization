
from helper import *
from config import *
import random, statistics
from stats import SAMPLE, eg0

inputs = ['digits','breastcancer','iris','whitewine','socialnetworkads','heartdisease','titanic','employeeattrition','pumpkinseeds','marketing','bankloan','date','fakebills','empturnover','cancer','wine','kidneystone','mineorrock','gendervoice','possum']

stats_data_rrp = {'digits':{'rrp': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.967, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]}}
stats_data_smo = {'digits':{'smo6': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.967, 1.0, 1.0, 1.0, 1.0, 0.967, 1.0, 1.0, 1.0, 1.0, 0.967, 1.0, 1.0, 1.0], 
              'smo14': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], 
              'smo20': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]}}

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

        if len(sample_list)>0:
            hw7_part2(sample_list, the)

        with open(file_output, 'a') as file:
            file.write('\n_______________________________\nEND for dataset ' + str(input)+'\n_______________________________\n')

    


