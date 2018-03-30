import time
import numpy as np

initial = time.time()


#previous, (more elegant imo) but slower function
#def is_prime(number,known_primes):
#    status = True
#    if number not in known_primes:
#        for i in [x for x in known_primes if x <= np.sqrt(number)]:
#            if number % i != 0:
#                status = False
#    return status
#


def fast_primey(number):
    if number == 2:
        return True
    if number < 2:
        return False
    if number % 2 == 0:
        return False
    for i in range(3,int(np.sqrt(number)+1)):
        if number % i == 0:
            return False
    return True

def primes_below(num):            
    primes = []
    for i in range(2,num):
        if fast_primey(i):
            primes.append(i)
    return primes
    

print(sum(primes_below(2000000)))
print('length: '+str(time.time()-initial))

