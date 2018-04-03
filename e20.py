def factorial(n):
    if n==1:
        return 1
    else: 
        return n * factorial(n-1)
    
solution = str(factorial(100))

nums = []

for i in solution: 
    nums.append(int(i))
    
print(sum(nums))