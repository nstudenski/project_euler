def sum_squares(max):
    squares = []
    for i in range(max+1):
        squares.append(i**2)
    return sum(squares)

def squared_sum(max):
    items = []
    for i in range(max+1):
        items.append(i)
    return sum(items)**2

def diff_betw(max):
    diff = squared_sum(max) - sum_squares(max)
    return diff

print(diff_betw(100))