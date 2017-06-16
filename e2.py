# find the sum of even fibonacci numbers smaller than four million

fibonacci = [1,2]
next = fibonacci[-1] + fibonacci[-2]


while (next < 4000000):
    fibonacci.append(next)
    next = fibonacci[-1] + fibonacci[-2]

sum = 0
for i in fibonacci:
    if (i % 2 == 0):
        sum += i
        
print sum

