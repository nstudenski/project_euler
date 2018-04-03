import time
start_time = time.time()
import pandas as pd
pd.set_option('display.max_rows', 100)

starterdf = pd.Series(range(1000000))
starterdf = pd.DataFrame(starterdf)
starterdf.columns = ['num']
starterdf['steps'] = 0

# I think this code is pretty bad and could be simplified.
# I thought it would be faster if I gave it memory but it is not
# 71 seconds using find_sequence_2
# 77 using find_sequence_1
def find_sequence_1(start,count):
    if start == 1:
        return count
    if start == 0:
        return count
    if start % 2 == 0:
        return find_sequence_1(start/2,count+1)
    else:
        return find_sequence_1(start*3+1,count+1)
 
starterdf['steps'] = starterdf['num'].apply(find_sequence_1,count=1)

#def find_sequence_2(start,count):
#    if start == 1:
#        return count
#    if start == 0:
#        return count
#    if start < 10000:
#        if finaldf.iloc[int(start),1] != 0:
#            rest_count = finaldf.iloc[int(start),1]
#            return find_sequence_2(1,count + rest_count)
#    if start % 2 == 0:
#        return find_sequence_2(start/2,count+1)
#    else:
#        return find_sequence_2(start*3+1,count+1)
#
#finaldf = pd.Series(range(1000000))
#finaldf = pd.DataFrame(finaldf)
#finaldf.columns = ['num']
#finaldf['steps'] = 0
#finaldf.loc[:9999,:] = starterdf.copy()
#
#finaldf['steps'] = finaldf['num'].apply(find_sequence_2,count=1)

time_elapsed = time.time()-start_time
print('execution time: '+str(time_elapsed))