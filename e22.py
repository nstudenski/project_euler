import os
import numpy as np
import string

os.chdir('/users/nstudenski/project_euler/')
with open('e22_supplement.txt') as f:
    raw_names = f.readlines()[0]
raw_names = raw_names.split(',')
names = []
for name in raw_names:
    names.append(name.strip('"'))
names.sort()

num_names = len(names) + 1

print('there are {} names'.format(num_names))

num_unique = len(np.unique(names)) + 1

print('all names are unique: {}'.format(num_names==num_unique))

name_scores = []

def get_score(name):
    letter_vals = []
    for letter in name:
        letter_vals.append(string.ascii_uppercase.index(letter) + 1)
    name_position = names.index(name) + 1
    score = sum(letter_vals) * name_position
    return score
    
for name in names:
    name_scores.append(get_score(name))
    
print('sum of all scores is {}'.format(sum(name_scores)))
