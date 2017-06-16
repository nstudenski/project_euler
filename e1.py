# find the sum of all multiples of three or five smaller than 1000

multiples = []

i = 999
while (i > 0) :
    if (i % 3 == 0) or (i % 5 == 0):
        multiples.append(i)
    i = i-1

sum = 0
for x in multiples:
    sum += x
    
print sum