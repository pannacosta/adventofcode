import numpy as np
import io
from collections import defaultdict

content = []
with io.open("filepath/input_d10.txt", "r", newline=None) as fd:
    for line in fd:
        line = line.replace("\n", "")
        content.append(line)

def find_corrupted_chunk(line):
    open_chars = ['(','{','[','<']
    close_chars = [')','}',']','>']
    stack = []
    for position, char in enumerate(line):
        if char in open_chars:
            stack.append(char)
        elif char in close_chars:
            if open_chars[close_chars.index(char)] == stack[-1]:
                stack.pop()
            else:
                return char
    bracket_swap = {open_chars[i]: close_chars[i] for i in range(len(open_chars))}
    if len(stack) > 0:
        return [bracket_swap[item] for item in stack][::-1]

def score_corrupted_chunks(lines): #Part 1
    score_maps = defaultdict(lambda: [0,0])
    for line in lines:
        corrupted_char = find_corrupted_chunk(line)
        if isinstance(corrupted_char,str): 
            score_maps[corrupted_char][0] += 1
    illegal_scores = {')':3,'}':1197,']':57,'>':25137}
    for key, value in score_maps.items():
        if key in illegal_scores.keys():
            score_maps[key][1] = illegal_scores[key]
    results = [np.prod(item) for item in list(score_maps.values())]
    return sum(results)

def repair_incomplete_chunks(lines): #Part 2 
    incomplete_chunks_records = []
    for line in lines:
        incomplete_chunks = find_corrupted_chunk(line)
        if isinstance(incomplete_chunks,list):
            incomplete_chunks_records.append(incomplete_chunks)
    score_swap = {')':1,']':2,'}':3,'>':4}
    brackets_to_numbers = [
        [score_swap[bracket] for bracket in line]
        for line in incomplete_chunks_records
        ]
    scored_chunks = []
    for line in brackets_to_numbers:
        completion_score = 0
        for score in line:
            completion_score *= 5
            completion_score += score
        scored_chunks.append(completion_score)
    sorted_scores = sorted(scored_chunks)
    return sorted_scores[int(len(sorted_scores)/2)]
    
print('Part 1 is:',score_corrupted_chunks(content))
print('Part 2 is:',repair_incomplete_chunks(content))
