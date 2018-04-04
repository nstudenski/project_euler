import pandas as pd
import itertools
import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)
    
def num_paths(dimension):
    lst = list(itertools.product([0, 1], repeat=dimension*2))
    lst = pd.DataFrame(lst)
    lst['sum'] = lst.apply(lambda x: sum(x),axis=1)
    return len(lst[lst['sum']==dimension])
print '2x2 grid has {} paths'.format(num_paths(2))
print nCr(4,2)#*.5**2+.5**2
print '3x3 grid has {} paths'.format(num_paths(3))
print nCr(6,3)
print '4x4 grid has {} paths'.format(num_paths(4))
print nCr(8,4)
print '5x5 grid has {} paths'.format(num_paths(5))
print nCr(10,5)

print nCr(40,20)