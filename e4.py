#function to find whether num is a palindrome
def is_palindrome(num):
    num = str(num)
    #this will be an array tallying whether each first half character matches with
    #the corresponding second half score
    char_match = []
    if len(num) % 2 == 0:
        #for each number in the first half, check whether it matches
        for i in range(int(len(num)/2)):
            if num[i] == num[-(i+1)]:
                char_match.append(0)
            else:
                char_match.append(1)
    else:
        for i in range(int((len(num)-1)/2)):
            if num[i] == num[-(i+1)]:
                char_match.append(0)
            #add a 1 to char_match array for each letter that doesn't match palindrome pattern
            else:
                char_match.append(1)
    if sum(char_match) > 0:
        return False
    else:
        return True
    
def find_largest(num_digits):
    sm = 10**(num_digits-1)
    lg = 10**num_digits
    palindromes = []
    for i in range(sm,lg):
        for j in range(sm,lg):
            product = i*j
            if is_palindrome(product):
                palindromes.append(product)
    return max(palindromes)

print(find_largest(3))
