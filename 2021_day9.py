import re
import numpy as np
import io
import math
from collections import defaultdict

content = []
with io.open("filepath/input_d9.txt", "r", newline=None) as fd:
    for line in fd:
        line = line.replace("\n", "")
        content.append([int(point) for point in line])

content = np.array(content)

m,n = content.shape
flattened = content.flatten()

#Challenge #1
def is_lowpoint(point_list):
    point,left,right,up,down = point_list
    if (min(point_list) == point) and (np.count_nonzero(point_list == point) == 1):
        return True
    else:
        return False

def check_for_lowpoints(array):
    low_points = []
    for index, point in enumerate(array):
        #left,right,up,down = array[index-1],array[index+1],array[index-m],array[index+m]
        if index < m:
            up = np.nan
        else:
            up = array[index-m]
        if index >= array.size - m:
            down = np.nan
        else:
            down = array[index+m]
        if index % m == m-m:
            left = np.nan
        else:
            left = array[index-1]
        if index % m == m-1:
            right = np.nan
        else:
            right = array[index+1]
        adjacent_points = [point,left,right,up,down]
        if is_lowpoint(adjacent_points) is True:
            low_points.append(point+1)
    return sum(low_points)

check_for_lowpoints(flattened)

#Challenge 2
import math
from collections import defaultdict

def make_graph(array):
    graph = defaultdict(list)
    index_map = np.nditer(array, flags=['multi_index'])
    num_rows,num_cols = array.shape
    for point in index_map:
        x,y = index_map.multi_index
        if x >= num_rows-1 or y >= num_cols-1:
            pass
        else:
            if x-1 >= 0 and array[x-1,y] != 9:
                graph[x,y].append((x-1,y))
            if x+1 < num_rows and array[x+1,y] != 9:
                graph[x,y].append((x+1,y))
            if y-1 >= 0 and array[x,y-1] != 9:
                graph[x,y].append((x,y-1))
            if y+1 < num_cols and array[x,y+1] != 9:
                graph[x,y].append((x,y+1))
    return graph

def BFS_Search(array): #works because after we build the graph, we have coordinates as keys tied to a list indexes for every value that is part of a basin
    graph = make_graph(array)
    basin_sizes = []
    visited = set() # use set to track visited nodes
    for v in list(graph.keys()):
        if v in visited: continue # this ensures we are not visiting the same coordinates a second time
        basin_size = 0 #start at 0 each time
        q = [v] 
        while q:
            node = q.pop(0)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor) # add neighbor to set
                    q.append(neighbor) #add 
                    basin_size += 1 #add 1 to basin size counter
        basin_sizes.append(basin_size)
    return math.prod(sorted(basin_sizes,reverse=True)[:3])

BFS_Search(content)
