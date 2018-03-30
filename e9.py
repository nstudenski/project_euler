import numpy as np

def is_pyth(nums):
    if len(nums) != 3:
        print('list must contain 3 numbers')
        return None
    nums.sort()
    a = nums[0]
    b = nums[1]
    c = nums[2]
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

triples = [] 
products = [] 

for x in range(1,1000):
    for y in range(1,1000-x):
        z = 1000-x-y
        if is_pyth([x,y,z]):
            true.append((x,y,z))
            products.append(x*y*z)

print(true)
print(products)
