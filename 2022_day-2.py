#day 2 answer
import re

my_file = open("input_2022_d2.txt", "r")
content = my_file.read()
puzzle_input_d2 = content.split("\n")
my_file.close()

list_of_games = [tuple(re.split(r"\s+", val)) for val in puzzle_input_d2]

game_result_dict = {'A':[('X',3),('Y',6),('Z',0)],
          'B':[('X',0),('Y',3),('Z',6)],
          'C':[('X',6),('Y',0),('Z',3)]
         }

your_play_dict = {'X':1,'Y':2,'Z':3}

###pt.1

score_list = []

for index,item in enumerate(list_of_games):
    key_match = game_result_dict.get(item[0],"empty")
    if key_match == 'empty':
        pass
    else:
        key_match = game_result_dict[item[0]] #returns value list of matching dict key
        your_ans_val = your_play_dict[item[1]]
        game_score = key_match[your_ans_val-1][1]
        score_list.append(game_score+your_ans_val)

sum(score_list)


###pt.2

move_score_dict = {'X':0,'Y':3,'Z':6}

pt2_score_list = []

for index,item in enumerate(list_of_games):
    key_match = game_result_dict.get(item[0],"empty")
    if key_match == 'empty':
        pass
    else:
        key_match = game_result_dict[item[0]]
        needed_outcome = move_score_dict[item[1]]
        needed_play = [item[0] for item in key_match if item[1] == needed_outcome]
        your_ans_val = your_play_dict[needed_play[0]]
        game_score = key_match[your_ans_val-1][1]
        pt2_score_list.append(game_score+your_ans_val)
    
sum(pt2_score_list)
