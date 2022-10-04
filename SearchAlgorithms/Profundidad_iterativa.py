from asyncio import current_task
from tkinter import Canvas
import numpy as np
from . import globals as gl
from memory_profiler import profile

class Stack: 
    items = []
    def __init__(self):
        self.items = []

    def is_empty(self): 
        return self.items == []
     
    def push(self, item):
        self.items.insert(0, item)
     
    def pop(self): 
        return self.items.pop(0)
     
    def print_stack(self): 
        print(self.items)

    def element_in(self,item):
        return item in self.items

    def peek(self):
        return self.items[0]

def color_button(x, y, matrix):
    if matrix[x, y] == 1:
        return '#669AFF'
    elif matrix[x, y] == 0:
        return '#041D50'
    elif matrix[x,y] == 2:
        return 'white'
    elif matrix[x,y] == 3:
        return 'red'

def color_maze(canvas,maze_):
    maze_height = len(maze_)
    maze_width = len(maze_[0])
    height = 650/maze_height
    width = 650/maze_width 

    for x, row in enumerate(maze_):
        for y, ch in enumerate(row):
            x1, y1 = (x*width, y*height)
            x2, y2 = (x1+width, y1+height)
            canvas.create_rectangle(x1, y1, x2, y2, fill=color_button(y,x,maze_), outline=color_button(y,x,maze_))

def backTracking(solution,maze_,startCell,goal,canvas):
    solution = solution[::-1]
    current_ = solution[0]
    maze_[goal[0]][goal[1]] = 3
    maze_[startCell[0]][startCell[1]] = 3
    while current_[1] != startCell:
        key = current_[1]
        maze_[key[0]][key[1]] = 3 
        for x in solution:
            if key == x[0]:
                current_ = x
        solution.pop(0)
    color_maze(canvas,np.array(maze_))

@gl.mide_tiempo
#@profile
def _profundidad(startCell,goalCell,maze_,canvas):
    frontier = Stack()
    visited = Stack()
    solution = []

    maze_[startCell[0]][startCell[1]] = 2
    frontier.push(startCell)
    visited.push(startCell)
    currentCell = frontier.peek()

    while currentCell != list(goalCell):
        
        #revisamos las celulas adyacentes

        # derecha
        if (0 <= currentCell[0]  <= len(maze_)-1) and (0 <= currentCell[1] + 1 < len(maze_[0])):
            if (maze_[currentCell[0]][currentCell[1]+1] == 1) and not(visited.element_in([currentCell[0],currentCell[1]+1])):
                frontier.push([currentCell[0],currentCell[1]+1])
                maze_[currentCell[0]][currentCell[1]+1] = 2
                solution.append([[currentCell[0],currentCell[1]+1],currentCell])

        # Abajo
        if (0 <= currentCell[0] +1 < len(maze_)) and (0 <= currentCell[1] < len(maze_[0])):
            if (maze_[currentCell[0]+1][currentCell[1]] == 1) and not(visited.element_in([currentCell[0]+1,currentCell[1]])):
                frontier.push([currentCell[0]+1,currentCell[1]])
                maze_[currentCell[0]+1][currentCell[1]] = 2
                solution.append([[currentCell[0]+1,currentCell[1]],currentCell])

        #Iniciando por la celula de la izquierda
        if (0 <= currentCell[0] <= len(maze_)-1) and (0 <= currentCell[1] - 1 < len(maze_[0])):
            if (maze_[currentCell[0]][currentCell[1]-1] == 1) and not(visited.element_in([currentCell[0],currentCell[1]-1])):
                frontier.push([currentCell[0],currentCell[1]-1])
                maze_[currentCell[0]][currentCell[1]-1] = 2
                solution.append([[currentCell[0],currentCell[1]-1],currentCell])
    
        # Arriba
        if (0 <= currentCell[0] -1 <= len(maze_)-1) and (0 <= currentCell[1] < len(maze_[0])):
            if (maze_[currentCell[0]-1][currentCell[1]] == 1) and not(visited.element_in([currentCell[0]-1,currentCell[1]])):
                frontier.push([currentCell[0]-1,currentCell[1]])
                maze_[currentCell[0]-1][currentCell[1]] = 2
                solution.append([[currentCell[0]-1,currentCell[1]],currentCell])

        currentCell =frontier.pop()
        visited.push(currentCell)

    color_maze(canvas,np.array(maze_))
    backTracking(solution,maze_,startCell,goalCell,canvas)