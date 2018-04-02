import pandas as pd
import os
os.chdir('/users/nstudenski/project_euler')
grid = pd.read_csv('e11_supplement.csv',header=None)

def find_product(group):
    product = 1
    for i in group:
        product = product * i
    return product

def horiz_groups(df,num):
    max_ix = num-1
    products = []
    for y in range(len(grid)):
        for x in range(len(grid)-max_ix):
            group = grid.loc[y,x:x+max_ix]
            products.append(find_product(group))
    return products

def vert_groups(df,num):
    max_ix = num-1
    products = []
    for x in range(len(grid)):
        for y in range(len(grid)-max_ix):
            group = grid.loc[y:y+max_ix,x]
            products.append(find_product(group))
    return products

def diag_groups_SE(df,num):
    max_ix = num-1
    products = []
    for x in range(len(grid)-max_ix):
        for y in range(len(grid)-max_ix):
            group = []
            for i in range(num):
                group.append(grid.loc[y+i,x+i])
            products.append(find_product(group))
    return products

def diag_groups_NE(df,num):
    max_ix = num-1
    products = []
    for x in range(len(grid)-max_ix):
        for y in range(max_ix,len(grid)):
            group = []
            for i in range(num):
                group.append(grid.loc[y-i,x+i])
            products.append(find_product(group))
    return products

horiz_products = horiz_groups(grid,4)
vert_products = vert_groups(grid,4)
SE_products = diag_groups_SE(grid,4)
NE_products = diag_groups_NE(grid,4)

all_products = horiz_products + vert_products + SE_products + NE_products

print(max(all_products))
