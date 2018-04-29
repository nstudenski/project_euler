nums = []
# I know that the base can't be higher than 9
# because any number 10 or greater raised to any power
# will have more digits than its exponenent
for i in range(1,10):
    # I played around a bit and found that 9^22 has a length of 21
    # I wish I could explain the math better, but it makes sense to me
    # that the exponent has essentially passed the length of the number
    # and I figured that there cannot be a number for which len(i^j) = j
    # where j is higher than 21
    for j in range(1,22):
        if len(str(i**j)) == j:
           nums.append(i**j)
print(len(nums))