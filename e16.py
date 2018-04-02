number = 2**1000
number = str(number)
digits = []
for i in number:
    digits.append(int(i))
print(sum(digits))