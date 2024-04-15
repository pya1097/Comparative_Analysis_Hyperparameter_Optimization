#Read data file
from helper import *
from row import ROW
from cols import COLS
from sym import SYM
import random
from config import the
from Node import NODE
import numpy as np

class DATA:

    def __init__(self, src=[], fun=None):
        self.rows = []
        self.cols = None
        if isinstance(src, str):
            for _, x in csv(src):
                self.add(x, fun)
        else:
            # for row in src:
            self.add(src, fun)


    def add(self, t, fun=None):
        # row = t if isinstance(t, ROW) else ROW(t)
        row = t if type(t) == ROW else ROW(t)
        if self.cols:
            if fun:
                fun(self, row)
            self.cols.add(row)
            self.rows.append(row)
        else:
            self.cols = COLS(row)

    # def stats(self, fun = None, ndivs = None):
    #     u = {".N": len(self.rows)}
    #     for col in self.cols.all:
    #         if(isinstance(col, SYM)):
    #             u[col.txt] = int(col.mid())
    #         else:
    #             u[col.txt] = roundoff(col.mid())
    #     return u
    def stats(self, fun=None, ndivs=None):
        u = {}
        for col in self.cols.all:
            if(isinstance(col, SYM)):
                if(col.txt == "origin"):
                    u[col.txt] = int(col.mid())
                else:
                    u[col.txt] = col.mid()
            else:
                u[col.txt] = round(col.mid(),2)
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


        # print('\n'.join(map(str, list_1)))
        # print('\n'.join(map(str, list_2)))
        # print('\n'.join(map(str, list_3)))
        # print('\n'.join(map(str, list_4)))
        # print('\n'.join(map(str, list_5)))
        # print('\n'.join(map(str, list_6)))

        # return stats, bests
        return stats, bests, [bests[-1].cells, round(bests[-1].d2h(self),2)]
    
    def any50(self, random_seed):
        random.seed(random_seed)
        rows = random.sample(self.rows, 50)
        return [rows[0].cells, round(rows[0].d2h(self),2)]

    def best_100(self, random_seed):
        random.seed(random_seed)
        rows = random.sample(self.rows, len(self.rows))
        rows.sort(key=lambda row: row.d2h(self))
        return [rows[0].cells, round(rows[0].d2h(self),2)]

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
    
    def clone(self, rows=None, newData=None):
        newData = DATA([self.cols.names])
        for row in rows or []:
            newData.add(row)
        return newData


    def farapart(self, rows, sortp, a=None, b=None, far=None, evals=0):
        far = int(len(rows) * 0.95) + 1
        evals = 1 if a is not None else 2
        
        a = a or random.choice(rows)
    
        sorted_neighbors = a.neighbors(self, rows)
        a = a or sorted_neighbors[0]
        b = sorted_neighbors[min(far, len(sorted_neighbors) - 1)]
        
        if sortp and b.d2h(self) < a.d2h(self):
            a, b = b, a
        
        return a, b, a.dist(b, self), evals
    
    def half(self, rows, sortp, before):
        the_half = min(len(rows) // 2, len(rows))
        some = random.sample(rows, the_half)
        a, b, C, evals = self.farapart(some, sortp, before)
        def d(row1, row2):
            return row1.dist(row2, self)
        
        def project(r):
            return (d(r, a)**2 + C**2 - d(r, b)**2) / (2 * C)
        rows_sorted = sorted(rows, key=project)
        mid_point = len(rows) // 2
        as_ = rows_sorted[:mid_point]
        bs = rows_sorted[mid_point:]
        return as_, bs, a, b, C, d(a, bs[0]), evals
    
    def far(the, data_new):
        print()
        print("Task 2:\n")
        target_distance = 0.95
        current_distance = 0
        attempts = 0

        while current_distance < target_distance and attempts < 200:
            a, b, C, _ = data_new.farapart(data_new.rows, sortp=True)
            current_distance = C
            attempts += 1
        if current_distance <= target_distance:
            print(f"far1: {a.cells}")
            print(f"far2: {b.cells}")
            print(f"distance: {current_distance}")
        else:
            print("No pair found within the target distance after maximum attempts.")

        #print(f"Total Attempts: {attempts}")
        return current_distance, attempts
    
    def tree(self, sortp):
        evals = 0

        def _tree(data, above = None):
            nonlocal evals
            node = NODE(data)

            if len(data.rows) > 2 * (len(self.rows) ** 0.5):
                lefts, rights, node.left, node.right, node.C, node.cut, evals1 = self.half(data.rows, sortp, above)
                evals += evals1
                node.lefts = _tree(self.clone(lefts), node.left)
                node.rights = _tree(self.clone(rights), node.right)

            return node

        return _tree(self), evals
    
    def branch(self, stop=None, rest=None, _branch=None, evals=None):
        evals, rest = 1, []
        stop = stop or (2 * (len(self.rows) ** 0.5))

        def _branch(data, above=None, left=None, lefts=None, rights=None):
            nonlocal evals, rest

            if len(data.rows) > stop:
                lefts, rights, left, _, _, _, _  = self.half(data.rows, True, above)
                evals += 1
                for row1 in rights:
                    rest.append(row1)

                return _branch(self.clone(lefts), left)
            else:
                return self.clone(data.rows), self.clone(rest), evals

        return _branch(self)
    
    def stats_div(self, fun=None, ndivs=None):
        u = {}
        for col in self.cols.all:
            if(isinstance(col, SYM)):
                if(col.txt == "origin"):
                    u[col.txt] = round(col.div(),2)
                else:
                    u[col.txt] = col.div()
            else:
                u[col.txt] = round(col.div(),2)
   
        return u

    def mid_div(self):
        d2h_vals = [r.d2h(self) for r in self.rows]
        return[[self.stats(), round(np.mean(d2h_vals),2)],[self.stats_div(), round(np.std(d2h_vals),2)]]
