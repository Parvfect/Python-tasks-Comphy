
import numpy as np

def generate(a, c, M, max_val, rstart):
    """ Returns random number sequence and ri and ri+1 seqeunces """
    r = []
    x = []
    y = []
    i = np.arange(1, max_val+1)

    rcurr = rstart
    r.append(rstart)

    for i in range(1, max_val):
        rcurr = ((a*rcurr + 1)%M)
        r.append(rcurr)

    x = [r[i] for i in range(len(r)) if i%2 == 0]
    y = [r[i] for i in range(len(r)) if i%2 != 0]

    return r, x, y

r,x,y = generate(1140671485, 128201163, 2**24, 100, 1)

print(r)