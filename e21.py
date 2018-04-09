import numpy as np

def d(n):
    divisors = []
    divisors.append(1)
    for i in range(2,int(np.sqrt(n))):
        if n % i == 0: 
            divisors.append(int(i))
            divisors.append(int(n / i))
    return sum(divisors)
    
def is_amicable(a):
    b = d(a)
    if a == d(b):
        return [True,a,b]
    else:
        return [False,None,None]

amicables = []

for i in range(10000):
    ams = is_amicable(i)
    if ams[0]:
        if ams[1] != ams[2]:
            amicables.append(ams[1])
            amicables.append(ams[2])

amicables = np.unique(amicables)

print(sum(amicables))