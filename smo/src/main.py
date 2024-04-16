from data import DATA 
from helper import *
from config import *
import random
import json
import time

inputs = ['digits','breastcancer','iris','whitewine','socialnetworkads','heartdisease','titanic','employeeattrition','pumpkinseeds','marketing','bankloan','date','fakebills','empturnover','cancer','wine','kidneystone','mineorrock','gendervoice','possum']
# inputs = ['digits']

def gate(treatement, budget0, budget, some,input):
        score = []
        randomSeeds = random.sample(range(15000),20)    
        # randomSeeds = [8747]
        for randomSeed in randomSeeds:
            print('------------------------------------------------------------------------------------------')
            print('SEED: ', randomSeed,"    ", treatement,"     ",input)
            print('------------------------------------------------------------------------------------------')
            d = DATA(file_path) #loads the data
            score.append(d.gate(randomSeed,budget0, budget, some,input))
            print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
             
        return score

if __name__ == "__main__":
    file_path = the['file']
    smos = {}

    start_time_0 = time.time()
    file_output = 'smo_output.txt'
    for input in inputs:
        start_time_1 = time.time()
        with open(file_output, 'a') as file:
            file.write('\n_______________________________\nSMO for dataset ' + str(input)+'\n_______________________________\n')
        
        smos[input] = {}

        start_time = time.time()
        smos[input]['smo6'] = gate('smo6',2,4,0.5,input)
        end_time = time.time()
        with open(file_output, 'a') as file:
            file.write('\n*****************\nSMO6\n*****************\n' + str(smos[input]['smo6'])+'\nTime taken: ' + str(end_time - start_time) + ' seconds\n*****************\n\n*****************\n')
        
        start_time = time.time()
        smos[input]['smo14'] = gate('smo14',4,10,0.5,input)
        end_time = time.time()
        with open(file_output, 'a') as file:
            file.write('\n*****************\nSMO14\n*****************\n' + str(smos[input]['smo14'])+'\nTime taken: ' + str(end_time - start_time) + ' seconds\n*****************\n\n*****************\n')
        
        start_time = time.time()
        smos[input]['smo20'] = gate('smo20',4,16,0.5,input)
        end_time = time.time()
        with open(file_output, 'a') as file:
            file.write('\n*****************\nSMO20\n*****************\n' + str(smos[input]['smo20'])+'\nTime taken: ' + str(end_time - start_time) + ' seconds\n*****************\n\n*****************\n')
        
        start_time = time.time()
        smos[input]['smo60'] = gate('smo60',8,52,0.5,input)
        end_time = time.time()
        with open(file_output, 'a') as file:
            file.write('\n*****************\nSMO60\n*****************\n' + str(smos[input]['smo60'])+'\nTime taken: ' + str(end_time - start_time) + ' seconds\n*****************\n\n*****************\n')
        

        end_time_1 = time.time()
        with open(file_output, 'a') as file:
            file.write('\n*****************\nFINAL\n*****************\n' + str(smos[input])+'\nTime taken: ' + str(end_time_1 - start_time_1) + ' seconds\n*****************\n\n*****************\n')
            file.write('\n_______________________________\nEND for dataset ' + str(input)+'\n_______________________________\n')

    end_time_0 = time.time()
    with open(file_output, 'a') as file:
        file.write('\n*****************\nFINAL SMO OUTPUT ENTIRE DATA LIST\n*****************\n' + str(smos)+'\nTime taken: ' + str(end_time_0 - start_time_0) + '\n*****************\n\n*****************\n')