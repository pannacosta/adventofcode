# Much Improved solution
import re
from collections import defaultdict

my_file = open("filepath/input_d6.txt", "r")
content = my_file.read()
my_file.close()
split = re.split(r"\n|,",content)
cleaned_input = [int(item) for item in split[:-1]]

d = defaultdict(int,{k:0 for k in list(range(0,9))})

for fish in cleaned_input:
    d[fish] += 1

def lanternfish_pop(input_dict, days):
    for day in range(0,days):
        timer_decay_by_1 = {k-1:v for k,v in input_dict.items()}
        new_dict = defaultdict(int,timer_decay_by_1)
        new_dict[8] = new_dict[8] +  new_dict[-1]
        new_dict[6] = new_dict[-1]+new_dict[6]
        del new_dict[-1]
        input_dict = new_dict
    print(sum(new_dict.values()))
        
lanternfish_pop(d,80) #challenge 1
lanternfish_pop(d,256) #challenge 2

##################### worse solution below

#initial solution only for challenge 1
for _ in repeat(None, 80):
    #step 1: subtract 1 from everything
    values_subtracted_df = input_df - 1

    #step 2: create array from column where values equal -1, change values to 8
    new_lantern_fish_col = values_subtracted_df.loc[values_subtracted_df['timer'] == -1]
    new_lantern_fish = new_lantern_fish_col['timer'].values
    new_lantern_fish[new_lantern_fish == -1] = 8
    
    #step 3: replace -1 with 6
    values_subtracted_df['timer'].replace({-1:6},inplace = True)

    #step 4: append new row to df with 8's and explode
    if len(new_lantern_fish) > 0:
        new_row = {'timer':new_lantern_fish}
        new_df = values_subtracted_df.append(new_row,ignore_index = True)
        input_df = new_df.explode('timer',ignore_index=True)
    else:
        input_df = values_subtracted_df
len(input_df)
