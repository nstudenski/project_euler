coins = [1,2,5,10,20,50,100,200]

####################################################
### this finds permutations, I need combinations ###
####################################################
# def add_coin(amounts,coins,count):
#     if len(amounts) == 0:
#         return count
#     new_amounts = []
#     for amount in amounts:
#         for coin in coins:
#             if amount + coin == 200:
#                 count += 1
#             elif amount + coin < 200:
#                 new_amounts.append(amount + coin)
#     print(count)
#     return add_coin(new_amounts,coins,count)
###################################################


###################################################
########### loop way. works, but messy ############
###################################################
# count = 0
# for a in range(int(200/200+1)):
#     v200 = 200*a
#     if v200 == 200:
#         count += 1
#     elif v200 < 200:
#         for b in range(int(200/100+1)):
#             v100 = 100*b
#             if v100 + v200 == 200:
#                 count += 1
#             elif v100 + v200 < 200:
#                 for c in range(int(200/50+1)):
#                     v50 = c*50
#                     if v50 + v100 + v200 == 200:
#                         count += 1
#                     elif v50 + v100 + v200 < 200:
#                         for d in range(int(200/20+1)):
#                             v20 = d*20
#                             if v20 + v50 + v100 + v200 == 200:
#                                 count += 1
#                             elif v20 + v50 + v100 + v200 < 200:
#                                 for e in range(int(200/10+1)):
#                                     v10 = e*10
#                                     if v10 + v20 + v50 + v100 + v200 == 200:
#                                         count += 1
#                                     elif v10 + v20 + v50 + v100 + v200 < 200:
#                                         for f in range(int(200/5+1)):
#                                             v5 = f*5
#                                             if v5 + v10 + v20 + v50 + v100 + v200 == 200:
#                                                 count += 1
#                                             elif v5 + v10 + v20 + v50 + v100 + v200 < 200:
#                                                 for g in range(int(200/2+1)):
#                                                     v2 = g*2
#                                                     if v2 + v5 + v10 + v20 + v50 + v100 + v200 == 200:
#                                                         count += 1
#                                                     elif v2 + v5 + v10 + v20 + v50 + v100 + v200 < 200:
#                                                         for h in range(int(200/1+1)):
#                                                             v1 = h*1
#                                                             if v1 + v2 + v5 + v10 + v20 + v50 + v100 + v200 == 200:
#                                                                 count += 1                      
# print(count)
#################################################

################
### nice!!! ###
###############
def next_coin_values(coins, tgt_value, trial_vals = [0], count = 0):
    if len(coins) == 0:
        return count
    coin = coins[0]
    new_trials = []
    for trial in trial_vals:
        for n in range(int(tgt_value/coin+1)):
            v = coin * n + trial
            if v == tgt_value:
                count += 1
            elif v < tgt_value:
                new_trials.append(v)
    return(next_coin_values(coins[1:], tgt_value, new_trials, count))
                
            

print(next_coin_values(coins,200))

                                
            
            
        