
from helper import *
from config import *
import random, statistics
from stats import SAMPLE, eg0

stats_data = {'rrp': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.967, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
              'smo6': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.967, 1.0, 1.0, 1.0, 1.0, 0.967, 1.0, 1.0, 1.0, 1.0, 0.967, 1.0, 1.0, 1.0], 
              'smo14': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], 
              'smo20': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]}

def hw7_part2(the):
    print("\n")
    print("\n")
    print("date:{}\nfile:{}\nrepeat:{}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),the['file'],"20"))

    eg0([
        SAMPLE(stats_data['rrp'], "rrp"),
        SAMPLE(stats_data['smo6'], "smo6"),
        SAMPLE(stats_data['smo14'], "smo14"), 
        SAMPLE(stats_data['smo20'], "smo20")
    ])



if __name__ == "__main__":
    file_path = the['file']

    hw7_part2(the)

    


