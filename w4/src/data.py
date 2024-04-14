#Read data file
from helper import *
from row import ROW
from cols import COLS
from sym import SYM
import random
from config import the

class DATA:

    def __init__(self, src=[], fun=None):
        self.rows = []
        self.cols = None
        if isinstance(src,str):
            for _,x in csv(src):
                self.add(x, fun)
        else:
            #for _,x in enumerate(src):
            self.add(src, fun)
    
    def add(self, t, fun=None):
        row = t if type(t) == ROW else ROW(t)
        # row = ROW(t) if type(t) == list else t
        if self.cols:
            if fun:
                fun(self, row)
            self.rows.append(self.cols.add(row))
        else:
        #    print('here', row)
           self.cols = COLS(row)

    def stats(self, fun = None, ndivs = None):
        u = {".N": len(self.rows)}
        for col in self.cols.all:
            if(isinstance(col, SYM)):
                u[col.txt] = int(col.mid())
            else:
                u[col.txt] = roundoff(col.mid())
        return u
    
    def classes_data(self):
        table = {}
        col = self.cols.klass
        table["N"] = len(self.rows)
        table["klasses"] = len(col.has)
        for key, val in col.has.items():
            table[key] = val
            table[key+"%"] = roundoff(val*100/len(self.rows), 2)
        return table
    

    
    
    def gate(self, randomSeed, budget0, budget, some):
        list_1,list_2,list_3, list_4, list_5, list_6 =[],[],[],[],[],[]
        random.seed(randomSeed)
        rows = random.sample(self.rows, len(self.rows)) #shuffles the data
        
        list_1.append(f"1. top6: {[r.cells[len(r.cells)-3:] for r in rows[:6]]}")
        list_2.append(f"2. top50:{[[r.cells[len(r.cells)-3:] for r in rows[:50]]]}")

        rows.sort(key=lambda row: row.d2h(self))
        list_3.append(f"3. most: {rows[0].cells[len(rows[0].cells)-3:]}")

        rows = random.sample(self.rows, len(self.rows))

        lite = rows[:budget0]
        dark = rows[budget0:]
        
        stats, bests = [], []
        for i in range(budget):
            best, rest = self.best_rest(lite, len(lite)**some)
            todo, selected = self.split(best, rest, lite, dark)
            list_4.append(f"4: rand:{random.sample(dark, budget0+i)[0].cells[-3:]}")
            list_5.append(f"5: mid: {selected.mid().cells[len(selected.mid().cells)-3:]}")
            list_6.append(f"6: top: {best.rows[0].cells[len(best.rows[0].cells)-3:]}")

            stats.append(selected.mid())
            bests.append(best.rows[0])
            lite.append(dark.pop(todo))


        print('\n'.join(map(str, list_1)))
        print('\n'.join(map(str, list_2)))
        print('\n'.join(map(str, list_3)))
        print('\n'.join(map(str, list_4)))
        print('\n'.join(map(str, list_5)))
        print('\n'.join(map(str, list_6)))

        return stats, bests

    def split(self, best, rest, lite, dark):
        selected = DATA(self.cols.names)
        max_value = float('-inf')
        out = 0
        for i, row in enumerate(dark):
            b = row.like(best, len(lite), 2, the)
            r = row.like(rest, len(lite), 2, the)
            if b > r:
                selected.add(row)
            tmp = abs(b + r) / abs(b - r + 1E-300)
            # print('tmp',tmp, 'max', max_value)
            if tmp > max_value:
                out, max_value = i, tmp
        return out, selected

    def best_rest(self, rows, want):
        rows.sort(key=lambda a: a.d2h(self))
        best = DATA(self.cols.names)
        rest = DATA(self.cols.names)
        for i, row in enumerate(rows):
            if i < want:
                best.add(row)
            else:
                rest.add(row)
        return best, rest
    
    def mid(self, cols=None):
        u = []
        for col in cols or self.cols.all:
            u.append(col.mid())
        return ROW(u)
    
    def div(self, cols=None):
        u = []
        for col in cols or self.cols.all:
            u.append(col.div())
        return ROW(u)

    def small(self):
        u = []
        for col in self.cols.all:
            u.append(col.small(the))
        return ROW(u)