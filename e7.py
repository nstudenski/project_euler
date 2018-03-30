primes = []
def is_prime(number,known_primes):
    status = True
    if number not in known_primes:
        for i in known_primes:
            if number % i == 0:
                status = False
    return status
            
primes = []
for i in range(2,110000):
    if is_prime(i,primes):
        primes.append(i)
    
print('found '+str(len(primes))+' prime numbers')
print('10,001st is '+str(primes[10000]))