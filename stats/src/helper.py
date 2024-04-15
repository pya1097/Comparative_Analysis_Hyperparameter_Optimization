import math, re
import sys, ast
import random
from datetime import datetime


def coerce(s):
    def fun(s2):
        return None if s2.lower() in ["null", "nil", "none"] else s2.lower() == "true" or (s2.lower() != "false" and s2)
    try:
        return float(s)
    except ValueError:
        return fun(re.match(r'^\s*(.*\S)', s).group(1)) if isinstance(s, str) else s

def cells(s):
    t = []
    for s1 in s.split(','):
        t.append(coerce(s1))
    return t

def csv(src):
    i=0
    src = sys.stdin if src == "−" else open(src ,"r")
    for s in src:
        i += 1
        yield i, cells(s)
    src.close()

def roundoff(n, ndecs=None):
    if type(n) == str:
        return n
    if math.floor(n) == n:
        return n
    if not ndecs: 
        ndecs = 2
    mult = 10**(ndecs)
    return math.floor(n * mult + 0.5) / mult

def shuffle(t):
    u = list(t)
    for i in range(len(u) - 1, 0, -1):
        j = random.randint(0,i)
        u[i], u[j] = u[j], u[i]
    return u

def slice(t, go=None, stop=None, inc=None):
    if go is not None and go < 0:
        go = len(t) + go
    if stop is not None and stop < 0:
        stop = len(t) + stop
    u = []
    for j in range((go or 1)//1, (stop or len(t))//1, (inc or 1)//1):
        u.append(t[j])
    return u

def o(t, n=None, u=None):
    if isinstance(t, (int, float)):
        return str(roundoff(t, n))
    if not isinstance(t, dict) and not isinstance(t, list):
        return str(t)
    u = []
    for k, v in t.items() if isinstance(t, dict) else enumerate(t):
        if str(k)[0] != '_':
            if len(t) > 0:
                u.append(o(v, n))
            else:
                u.append(f"{o(k, n)}: {o(v, n)}")
    return "{" + ", ".join(u) + "}"

def anyCustom(t):
    return random.choice(t)

def many(t, n=None):
    n = n or len(t)
    u = []
    for _ in range(n):
        u.append(any(t))
    return u

def keysort(t, fun):
    u = [{'x': x, 'y': fun(x)} for x in t]
    u.sort(key=lambda a: a['y'])
    v = [xy['x'] for xy in u]
    return v

def format_row(name, row, d2h_val=None):
    return_string = ""
    len_space = [11,11,9,10,11,10,9,9]

    def _format_item(item):
        try:
            float(item)
            return item
        except:
            return f"'{item}'"

    for i, item in enumerate(row):
        start_string = ""
        end_string=""
        if i == 0:
            start_string += "["
        if i == 7:
            end_string += "]"
        item_str = start_string + _format_item(str(item)) + end_string
        return_string +=  item_str + (" " * (len_space[i] - len(item_str)))
    return f"{name}\t\t\t{return_string}\t{'d2h-' if d2h_val is None else str(d2h_val)}"

def print_centroid(data_new,mid_100,div_100, the):
    print("date:{}\nfile:{}\nrepeat:{}\nseed:{}\nrows:{}\ncols:{}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"),the['file'],"20",the['seed'],len(data_new.rows), len(data_new.rows[0].cells)))
    print(format_row("names", data_new.cols.names,None))
    print(format_row("Mid"  , list(mid_100[0].values()),mid_100[1]))
    print(format_row("Div"  , list(div_100[0].values()),div_100[1]))

def print_smo(smo_output):
    smo_output = sorted(smo_output, key=lambda x: x[1])
    for op in smo_output:
        print(format_row("smo9",op[0],op[1]))

def print_any50(any50_output):
    any50_output = sorted(any50_output, key=lambda x: x[1])
    for op in any50_output:
        print(format_row("any50",op[0],op[1]))