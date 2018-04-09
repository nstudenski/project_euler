import numpy as np
import pandas as pd
def next_month_start(year,month,wday_begin):
    month_len = 31
    if month == 2:
        month_len = 28
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    month_len = 29
            else:
                month_len = 29
    if month in [9,4,6,11]:
        month_len = 30
    wday_begin = (wday_begin + month_len) % 7
    return wday_begin

monthlist = []

mons = np.repeat([range(1,13)],101,axis=0)

for year in mons:
    for month in year:
        monthlist.append(month)

yearlist = np.repeat(range(1900,2001),12)

dates = pd.DataFrame({'year':yearlist,'month':monthlist})

dates['start_wday'] = 1

for i in range(1,1212):
    last_year = dates.iloc[i-1,1]
    last_month = dates.iloc[i-1,0]
    last_begin = dates.iloc[i-1,2]
    dates.iloc[i,2] = next_month_start(last_year,last_month,last_begin)
    
dates = dates[dates['year'] > 1900]
dates = dates[dates['start_wday'] == 0]
print(len(dates))