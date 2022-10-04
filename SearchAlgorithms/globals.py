import time
global agent_pos 
global matrix
global goal_pos 
goal_pos =()
agent_pos =(0, 1)
matrix = []
canvas =""
def color_maze():
    tile_width = 650/(goal_pos[1]+1) 
    tile_height = 650/(goal_pos[0]+1)
    for x, row in enumerate(matrix):
        for y, ch in enumerate(row):
           x1, y1 = (x*tile_width, y*tile_height)
           x2, y2 = (x1+tile_width, y1+tile_height)
           canvas.create_rectangle(x1, y1, x2, y2, fill=color_button(y,x,matrix), outline=color_button(y,x,matrix))

def color_button(x, y, matrix):
    if matrix[x, y] == 1:
        return '#669AFF'
    elif matrix[x, y] == 0:
        return '#041D50'
    elif matrix[x,y] == 2:
        return 'white'
    elif matrix[x,y] == 3:
        return 'red'

def mide_tiempo(funcion):
    def funcion_medida(*args, **kwargs):
        inicio = time.time()
        c = funcion(*args, **kwargs)
        print(time.time() - inicio)
        return c
    return funcion_medida