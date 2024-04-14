import math
from config import the

class ROW:
    # Initializing ROW instance
    def __init__(self, t):
        self.cells = t

    # ROW class methods
        
    # Method to calculate distancce to heaven
    def d2h(self, data):
        d, n = 0, 0
        for col in data.cols.y:
            n = n + 1
            d = d + abs(col.heaven - col.norm(self.cells[col.at]))**2
        return (d**0.5)/(n**0.5)

    #Finding out how much a row likes the data
    def like(self, data, n, nHypotheses, the):
        # print(the)
        prior = (len(data.rows) + the['k']) / (n + the['k'] * nHypotheses)
        out = math.log(prior)

        for col in data.cols.x:
            v = self.cells[col.at]
            if v != "?":
                inc = col.like(v, prior, the)
                if inc == 0:
                    out += float('-inf')
                else:
                    out += math.log(inc)

        return math.exp(1) ** out
    
    # Classifier
    def likes(self,datas):
        n, nHypotheses = 0, 0
        most, out = None, None
        # print(the)

        for k, data in datas.items():
            n += len(data.rows)
            nHypotheses += 1

        for k, data in datas.items():
            tmp = self.like(data, n, nHypotheses, the)
            if most is None or tmp > most:
                most, out = tmp, k

        return out, most
