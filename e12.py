import numpy as np
import pandas as pd
import time

start_time = time.time()

triangles = [0]
for i in range(12500):
    triangles.append(triangles[-1]+i)

def find_factors(n):
    n = n.values[0]
    count = 1 # 1 is counted as a factor
    max = int(np.sqrt(n)+1)
    factors = range(2,max)
    for i in factors:
        test = n % i
        if test==0:
            count = count + 2
    return count


triangles = pd.DataFrame({'triangle':triangles})
triangles['num_factors'] = triangles.apply(find_factors,axis=1)
print(triangles)
print('most_factors: ' + str(max(triangles['num_factors'])))
time_elapsed = time.time() - start_time
print('seconds elapsed: ' + str(time_elapsed))
print(triangles[triangles['num_factors']>500])
