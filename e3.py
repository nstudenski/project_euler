# find the largest prime factor of 600851475143               
to_be_factored = int(raw_input('enter a number and i\'ll tell you it\'s prime factors '))      
dummy_factors = []
odd_factors = []
prime_factors = []
not_prime = []

def getfactors(factor_me):
    for i in range (1, int(factor_me ** .5)):
        if (factor_me % i == 0) and (i % 2 != 0):
            odd_factors.append(i)
    return odd_factors
    
odd_factors = getfactors(to_be_factored)
prime_factors = odd_factors
odd_factors.remove(1)

for (i) in odd_factors:
    for j in odd_factors:
        #print '{0} / {1}'.format(i, j)
        if (i % j == 0) and (i != j):
            if i in odd_factors:
                not_prime.append(i)

not_prime = list(set(not_prime))
not_prime.sort()
odd_factors.sort()

print 'NO'
print not_prime
print odd_factors


prime = list(set(odd_factors) - set(not_prime))

prime.sort()
 
print prime

# why doesn't this work
#for i in odd_factors
#    if i in not_prime
#    master_odd_factors.remove(i)