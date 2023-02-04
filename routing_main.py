
import heapq

import numpy as np

import matplotlib.pyplot as plt

from matplotlib.pyplot import figure

import picar_4wd as fc

import time


def heuristic(a, b):

    return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)


def astar(array, start, goal):

    neighbors = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

    close_set = set()

    came_from = {}

    gscore = {start:0}

    fscore = {start:heuristic(start, goal)}

    oheap = []

    heapq.heappush(oheap, (fscore[start], start))
 

    while oheap:

        current = heapq.heappop(oheap)[1]

        if current == goal:

            data = []

            while current in came_from:

                data.append(current)

                current = came_from[current]

            return data

        close_set.add(current)

        for i, j in neighbors:

            neighbor = current[0] + i, current[1] + j            

            tentative_g_score = gscore[current] + heuristic(current, neighbor)

            if 0 <= neighbor[0] < array.shape[0]:

                if 0 <= neighbor[1] < array.shape[1]:                

                    if array[neighbor[0]][neighbor[1]] == 1:

                        continue

                else:

                    # array bound y walls

                    continue

            else:

                # array bound x walls

                continue
 

            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):

                continue
 

            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:

                came_from[neighbor] = current

                gscore[neighbor] = tentative_g_score

                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)

                heapq.heappush(oheap, (fscore[neighbor], neighbor)) 



def generate_grid():
    grid = np.zeros((100,100))
    for i in range(-60, 61, 2):
        time.sleep(0.1)
        tmp  = fc.get_distance_at(i)
        if (tmp == -2):
            continue
        print(tmp)
        x = 49 + np.int(tmp * np.sin(np.radians(i)))
        y =  np.int(tmp * np.cos(np.radians(i)))
        if (x > 99):
            x = 96
        if (y > 99):
            y = 96

        #grid[x-3:x+3, y-3:y+3] = 1
        grid[x,y] = 1
    return grid


    
    





start = (50,0)

goal = (50, 90)

grid = generate_grid()

fig, ax = plt.subplots(figsize=(12,12))

ax.imshow(grid, cmap=plt.cm.Dark2)

ax.scatter(start[1],start[0], marker = "*", color = "yellow", s = 200)

ax.scatter(goal[1],goal[0], marker = "*", color = "red", s = 200)

plt.show()


#route = astar(grid, start, goal)

#route = route + [start]

#route = route[::-1]

#x_coords = []

#y_coords = []

#for i in (range(0,len(route))):

#    x = route[i][0]

#    y = route[i][1]

#    x_coords.append(x)

#    y_coords.append(y)

## plot map and path

#fig, ax = plt.subplots(figsize=(20,20))

#ax.imshow(grid, cmap=plt.cm.Dark2)

#ax.scatter(start[1],start[0], marker = "*", color = "yellow", s = 200)

#ax.scatter(goal[1],goal[0], marker = "*", color = "red", s = 200)

#ax.plot(y_coords,x_coords, color = "black")

#plt.show()



 
