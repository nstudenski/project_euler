#iterate through each combination of digits and calculate the two numbers
special_nums = []
for i in range(0,10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                for m in range(10):
                    for n in range(10):
                        for o in range(10):
                            prod = ((i**5 + j**5 + k**5 + l**5 + m**5 + n**5 + o**5))
                            chars = (int((str(i) + str(j) + str(k) + str(l) + str(m) + str(n) + str(o))))
                            if prod == chars:
                                special_nums.append(prod)
print(sum(special_nums)-1)