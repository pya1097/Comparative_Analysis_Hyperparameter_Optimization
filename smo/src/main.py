from data import DATA 
from helper import *
from config import *
import random
import json
import time

# inputs = ['dtlz2','dtlz3','pom3a','pom3b','pom3c','SS-A','SS-B','SS-C','SS-D','Wine_quality']
file_output = 'rand_output_sample.txt'
inputs = ['digits','breastcancer','heartdisease','employeeattrition','marketing','fakebills','empturnover','cancer','kidneystone','gendervoice']

def gate(treatement, budget0, budget, some,input):
        score = []
        randomSeeds = random.sample(range(15000),20)    
        # randomSeeds = [8747]
        for randomSeed in randomSeeds:
            print('------------------------------------------------------------------------------------------')
            print('SEED: ', randomSeed,"    ", treatement,"     ",input)
            print('------------------------------------------------------------------------------------------')
            d = DATA(file_path) #loads the data
            l , acc = d.gate(randomSeed,budget0, budget, some,input)
            with open(file_output, 'a') as file:
                file.write('\n-------------------------------- BEST \n' + str(l.cells) + ' \n--------------------------------\n')
            score.append(acc)
            print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
             
        return score

def rand(treatement, n,input):
    randomSeeds = random.sample(range(15000),20) 
    
    rand_arr = []
    for randomSeed in randomSeeds:
        random.seed(randomSeed)
        d = DATA(file_path)
        rows = d.rows
        random.shuffle(rows)
        rowsN = random.sample(rows,n)
        rowsN.sort(key=lambda row: row.d2h(input))
        with open(file_output, 'a') as file:
                file.write('\n-------------------------------- BEST \n' + str(rowsN[0].cells) + ' \n--------------------------------\n')
        rand_arr.append(round(rowsN[0].cells[6],2))

    return rand_arr

if __name__ == "__main__":
    file_path = the['file']
    smos = {}

    start_time_0 = time.time()
    
    # for input in inputs:
    #     start_time_1 = time.time()
    #     with open(file_output, 'a') as file:
    #         file.write('\n_______________________________\nSMO for dataset ' + str(input)+'\n_______________________________\n')
        
    #     smos[input] = {}

    #     start_time = time.time()
    #     smos[input]['smo6'] = gate('smo6',2,4,0.5,input)
    #     end_time = time.time()
    #     with open(file_output, 'a') as file:
    #         file.write('\n*****************\nSMO6\n*****************\n' + str(smos[input]['smo6'])+'\nTime taken: ' + str(end_time - start_time) + ' seconds\n*****************\n\n*****************\n')
        
    #     start_time = time.time()
    #     smos[input]['smo14'] = gate('smo14',4,10,0.5,input)
    #     end_time = time.time()
    #     with open(file_output, 'a') as file:
    #         file.write('\n*****************\nSMO14\n*****************\n' + str(smos[input]['smo14'])+'\nTime taken: ' + str(end_time - start_time) + ' seconds\n*****************\n\n*****************\n')
        
    #     start_time = time.time()
    #     smos[input]['smo20'] = gate('smo20',4,16,0.5,input)
    #     end_time = time.time()
    #     with open(file_output, 'a') as file:
    #         file.write('\n*****************\nSMO20\n*****************\n' + str(smos[input]['smo20'])+'\nTime taken: ' + str(end_time - start_time) + ' seconds\n*****************\n\n*****************\n')
        
    #     start_time = time.time()
    #     smos[input]['smo60'] = gate('smo60',8,52,0.5,input)
    #     end_time = time.time()
    #     with open(file_output, 'a') as file:
    #         file.write('\n*****************\nSMO60\n*****************\n' + str(smos[input]['smo60'])+'\nTime taken: ' + str(end_time - start_time) + ' seconds\n*****************\n\n*****************\n')
        

    #     end_time_1 = time.time()
    #     with open(file_output, 'a') as file:
    #         file.write('\n*****************\nFINAL\n*****************\n' + str(smos[input])+'\nTime taken: ' + str(end_time_1 - start_time_1) + ' seconds\n*****************\n\n*****************\n')
    #         file.write('\n_______________________________\nEND for dataset ' + str(input)+'\n_______________________________\n')

    # end_time_0 = time.time()
    # with open(file_output, 'a') as file:
    #     file.write('\n*****************\nFINAL SMO OUTPUT ENTIRE DATA LIST\n*****************\n' + str(smos)+'\nTime taken: ' + str(end_time_0 - start_time_0) + '\n*****************\n\n*****************\n')

    rands = {}
    for input in inputs:
        start_time_1 = time.time()
        with open(file_output, 'a') as file:
            file.write('\n_______________________________\nRAND for dataset ' + str(input)+'\n_______________________________\n')
        
        rands[input] = {}

        start_time = time.time()
        rands[input]['rand6'] = rand('rand6',6,input)
        end_time = time.time()
        with open(file_output, 'a') as file:
            file.write('\n*****************\nRAND6\n*****************\n' + str(rands[input]['rand6'])+'\nTime taken: ' + str(end_time - start_time) + ' seconds\n*****************\n\n*****************\n')
        
        start_time = time.time()
        rands[input]['rand14'] = rand('rand14',14,input)
        end_time = time.time()
        with open(file_output, 'a') as file:
            file.write('\n*****************\nRAND14\n*****************\n' + str(rands[input]['rand14'])+'\nTime taken: ' + str(end_time - start_time) + ' seconds\n*****************\n\n*****************\n')
        
        start_time = time.time()
        rands[input]['rand20'] = rand('rand20',20,input)
        end_time = time.time()
        with open(file_output, 'a') as file:
            file.write('\n*****************\nRAND20\n*****************\n' + str(rands[input]['rand20'])+'\nTime taken: ' + str(end_time - start_time) + ' seconds\n*****************\n\n*****************\n')
        
        start_time = time.time()
        rands[input]['rand60'] = rand('rand60',60,input)
        end_time = time.time()
        with open(file_output, 'a') as file:
            file.write('\n*****************\nRAND60\n*****************\n' + str(rands[input]['rand60'])+'\nTime taken: ' + str(end_time - start_time) + ' seconds\n*****************\n\n*****************\n')
        

        end_time_1 = time.time()
        with open(file_output, 'a') as file:
            file.write('\n*****************\nFINAL\n*****************\n' + str(rands[input])+'\nTime taken: ' + str(end_time_1 - start_time_1) + ' seconds\n*****************\n\n*****************\n')
            file.write('\n_______________________________\nEND for dataset ' + str(input)+'\n_______________________________\n')

    end_time_0 = time.time()
    with open(file_output, 'a') as file:
        file.write('\n*****************\nFINAL RAND OUTPUT ENTIRE DATA LIST\n*****************\n' + str(rands)+'\nTime taken: ' + str(end_time_0 - start_time_0) + '\n*****************\n\n*****************\n')