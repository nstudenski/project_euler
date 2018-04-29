## runs in ~44 seconds
#import time
#start = time.time()
#ls = ["0","1","2","3","4","5","6","7","8","9"]
#result = []
#for a in ls:
#    for b in ls:
#        if b != a:
#            for c in ls:
#                if (c != b) & (c != a):
#                    for d in ls:
#                        if (d != c) & (d != b) & (d != a):
#                            for e in ls:
#                                if (e != d) & (e != c) & (e != b) & (e != a):
#                                    for f in ls:
#                                        if (f != e) & (f != d) & (f != c) & (f != b) & (f != a):
#                                            for g in ls:
#                                                if (g != f) & (g != e) & (g != d) & (g != c) & (g != b) & (g != a):
#                                                    for h in ls:
#                                                        if (h != g) & (h != f) & (h != e) & (h != d) & (h != c) & (h != b) & (h != a):
#                                                            for i in ls:
#                                                                if (i != h) & (i != g) & (i != f) & (i != e) & (i != d) & (i != c) & (i != b) & (i != a):
#                                                                    for j in ls:
#                                                                        if (j != i) & (j != h) & (j != g) & (j != f) & (j != e) & (j != d) & (j != c) & (j != b) & (j != a):
#                                                                            result.append(a+b+c+d+e+f+g+h+i+j)
#print(time.time()-start)
# # finds answer of 2783915460
#
import time
begin = time.time()

import math
goal = 999999


def func(start,i,string,rem):
    new = start + i * math.factorial(len(rem)-1)
    if new < goal:
        string = func(start,i+1,string,rem)
    if new > goal:
        string = string + rem[i-1]
        start = start + (i-1) * math.factorial(len(rem)-1)
        rem.remove(rem[i-1])
        string = func(start,0,string,rem)
    if new == goal:
        for i in range(len(rem)):
            string = string + rem[-(i+1)]
    return string
    
start = 0
i = 0
n = 9
string = ""
rem = ["0","1","2","3","4","5","6","7","8","9"]
print(func(start,i,string,rem))
print(time.time()-begin)
