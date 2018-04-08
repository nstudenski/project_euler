import os
import time
import copy
start = time.time()

#read triangle from text file
#now, the format is a list of strings, each string is one level of the triangle
os.chdir('/users/nstudenski/project_euler/')
with open('e67_supplement.txt') as f:
    triangle = f.readlines()

#remove newline characters from each string
for level in range(len(triangle)):
    triangle[level] = triangle[level].strip('\n')
  
#turn each string into a list of values in that level  
for level in range(len(triangle)):
    triangle[level] = triangle[level].split(' ')
 
#convert values from str to int 
for level in range(len(triangle)):
    for pos in range(level+1):
        triangle[level][pos] = int(triangle[level][pos])

known_tri = copy.deepcopy(triangle)
for level in range(len(known_tri)):
    for pos in range(level+1):
        known_tri[level][pos] = None
        

def best_path(level,pos,value):
    #if we don't know the number
    if known_tri[level][pos] == None:
        #best path beginning at the top of triangle is simply the top value
        if level == 0:
            result = value + triangle[0][0]
        else:
            #if the path originates at the leftmost end of the bottom level
            #of the triangle, there is only one possible path
            if pos == 0:
                result = best_path(level-1,pos,value + triangle[level][pos])
            #same if the path originates at the rightmost end
            elif len(triangle[level])-1 == pos:
                result = best_path(level-1,pos-1,value + triangle[level][pos])
            #otherwise, the optimal path is the best of the two paths
            #that branch from the current position
            else:
                a = best_path(level-1,pos-1,value + triangle[level][pos])
                b = best_path(level-1,pos,value + triangle[level][pos])
                result = (max(a,b))
        known_tri[level][pos] = result - value
        return result
    #if we already know the best path from here, use the known value
    else: return value + known_tri[level][pos]
          
bests = []
bottom = len(triangle)-1
for i in range(len(triangle[bottom])):
    bests.append(best_path(bottom,i,0))

time_delta = time.time() - start
print('time elapsed: {} seconds'.format(time_delta))