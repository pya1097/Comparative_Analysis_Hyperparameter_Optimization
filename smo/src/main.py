from data import DATA 
from helper import *
from config import *
import random

def gate(treatement, budget0, budget, some):
        score = []
        randomSeeds = random.sample(range(15000),20)    
        # randomSeeds = [8747]
        for randomSeed in randomSeeds:
            print('------------------------------------------------------------------------------------------')
            print('SEED: ', randomSeed,"    ", treatement)
            print('------------------------------------------------------------------------------------------')
            d = DATA(file_path) #loads the data
            score.append(d.gate(randomSeed,budget0, budget, some))
            print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
             
        return score

if __name__ == "__main__":
    file_path = the['file']
    smos = {}
    smos['smo6'] = gate(2,4,0.5)
    smos['smo14'] = gate(4,10,0.5)
    smos['smo20'] = gate(4,16,0.5)
    print(smos)

    if the['help']:
        print(help_str)