from data import DATA 
from helper import *
from config import *
import random


def rrp(data_new):
    score = []
    for i in range(0,20):
        print('------------------------------------------------------------------------------------------')
        print("RRP Iteration: ",i)
        print('------------------------------------------------------------------------------------------')
        best, _, _ = data_new.branch()
        max = -100
        for r in best.rows:
            if max < round(r.d2h(data_new),3):
                max = round(r.d2h(data_new),3)
        score.append(max)
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

    return score

if __name__ == "__main__":
    file_path = the['file']

    data_new = DATA(the['file'])

    final_score = {}
    final_score['rrp'] = rrp(data_new)
    print(final_score)


