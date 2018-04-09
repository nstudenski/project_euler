fibs = [1,1]

for i in range(2,5000):
    new = fibs[i-2] + fibs[i-1]
    fibs.append(new)
    n_digits = len(str(new))
    if n_digits == 1000:
        #add one to convert to a zero index 
        print(i+1)
        break