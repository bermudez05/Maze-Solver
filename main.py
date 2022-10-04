import tkinter as tk
from tkinter.messagebox import YES
from tkinter import filedialog
from tokenize import String
import numpy as np
import csv
import SearchAlgorithms.globals as gl
import SearchAlgorithms.Astar as Astar
import SearchAlgorithms.Anchura as Anchura
import SearchAlgorithms.Busqueda_Greedy as Greedy
import SearchAlgorithms.Costo_uniforme as C_U
import SearchAlgorithms.Profundidad as Profundidad
import SearchAlgorithms.Profundidad_iterativa as P_I
# Funciones a incluir en cada archivo de algoritmo
# para ek coloreado de la solucion

maze = ""
widthScreen = 0
heightScreen = 0
tile_height =0
tile_width =0

def color_button(x, y, matrix):
    if matrix[x, y] == 1:
        return '#669AFF'
    elif matrix[x, y] == 0:
        return '#041D50'
    elif matrix[x,y] == 2:
        return 'white'
    elif matrix[x,y] == 3:
        return 'red'
def _lectura_maze():

    # importamos el laberinto en formato csv
    mazeReader = csv.reader(open(maze))

    matrix = []
    # hacemos la lectura del laberinto linea por linea
    for row in mazeReader:
        if row != []:
            row = [0 if x == 'w' else 1 for x in row]
            matrix.append(row)

    # identificamos la posicion inicial y la final
    gl.agent_pos = (0, matrix[0].index(1))
    gl.goal_pos = (len(matrix) - 1, matrix[len(matrix) - 1].index(1))

    matrix = np.array(matrix) 
    return matrix

def MazeSolverBoard():
    root = tk.Tk()
    root.title(f"{maze}")
    root.configure(background='#7C9DDE')
    root.geometry("%dx%d" %(widthScreen,heightScreen))
    gl.canvas = tk.Canvas(master=root, height=650, width=650)
    gl.matrix = np.array(gl.matrix) 
    tile_width = 650/(gl.goal_pos[1]+1) 
    tile_height = 650/(gl.goal_pos[0]+1)
    gl.canvas.pack(expand=YES)
    gl.canvas.configure(background='#7C9DDE')
    for x, row in enumerate(gl.matrix):
        for y, ch in enumerate(row):
           x1, y1 = (x*tile_width, y*tile_height)
           x2, y2 = (x1+tile_width, y1+tile_height)
           gl.canvas.create_rectangle(x1, y1, x2, y2, fill=color_button(y,x,gl.matrix), outline=color_button(y,x,gl.matrix))
    #dropdown para la seleccion del algoritmo
    select_algo = tk.Frame(master=root)
    select_algo.pack(side=tk.BOTTOM,fill=tk.X)
        # Dropdown menu options
    options = [
        "Profundidad", "Anchura", "Profundidad iterativa",
        "Costo uniforme", "Búsqueda Greedy", "Algoritmo A*"
    ]
    # datatype of menu text
    valor = tk.StringVar(root)
    # initial menu text
    valor.set("Seleccione algoritmo")

    def seleccionAlg(opcion):
        opcion = valor.get()
        if opcion == "Profundidad":
            Profundidad._profundidad(gl.agent_pos,gl.goal_pos,gl.matrix,gl.canvas)
        elif opcion == "Anchura":
             Anchura.Anchura(gl.canvas)
        elif opcion == "Profundidad iterativa":
             P_I._profundidad(gl.agent_pos,gl.goal_pos,gl.matrix,gl.canvas)
        elif opcion == "Costo uniforme":
             C_U.Costo_uniforme()
        elif opcion == "Busqueda Greedy":
             Greedy.Greedy()
        elif opcion == "Algoritmo A*":
             Astar.Astar()
        # Create Dropdown menu
    valor_ = tk.OptionMenu(
        select_algo,
        valor,
        *options,
        command=seleccionAlg
    )

    valor_.pack(side=tk.BOTTOM, fill="x")
    valor_.config(font= ('Helvetica 15'))
    valor_.config(bg='#5B77AF')



class Menu(tk.Tk):

    #inicializa el menu principal
    def __init__(self):
        global widthScreen
        global heightScreen

        super().__init__()
        self.title("Maze Solver")
        widthScreen = self.winfo_screenwidth()
        heightScreen = self.winfo_screenheight()
        self.configure(background='#5B77AF')
        self.geometry("%dx%d" %(widthScreen/2.3,heightScreen/1.9))

        title = tk.Label(self, text = "Maze Solver",font=('Arial 90 bold'),height=2)
        title.configure(background="#5B77AF")
        title.pack(side=tk.TOP)
        num1 = tk.Label(self, text = "Sofia Salinas Rico",font=('Helvetica 20 italic'))
        num1.configure(background="#5B77AF")
        num1.pack(side=tk.TOP)
        num2 = tk.Label(self, text = "Andres Tarapues Cuaical",font=('Helvetica 20 italic'))
        num2.configure(background="#5B77AF")
        num2.pack(side=tk.TOP)
        num3 = tk.Label(self, text = "Nicole Bermudez Santa",font=('Helvetica 20 italic'))
        num3.configure(background="#5B77AF")
        num3.pack(side=tk.TOP)
        
        self._load_maze()
        self._maze_menu()

    #cargamos laberintos externos
    def _load_maze(self):
        loadMaze = tk.Frame(master=self)
        loadMaze.pack(side=tk.BOTTOM,fill=tk.X)

        def open_loadMaze():
            global maze
            #nos da el directorio completo del archivo
            archivo = filedialog.askopenfilename(title="Seleccione laberinto")
            maze=archivo
            self.destroy()
            MazeSolverBoard()

        load = tk.Button(master=loadMaze,
                          highlightbackground="#5B77AF",
                          text='Cargar laberinto externo',
                          font= ('Helvetica 15'),
                          command=open_loadMaze)
        load.pack(side=tk.BOTTOM,fill=tk.X)
        load.config(height=2)

    def _maze_menu(self):
        
        menu_frame = tk.Frame(master=self)
        menu_frame.pack(side=tk.BOTTOM,fill=tk.X)
        # Dropdown menu options
        options = [
            "Laberinto 5x5", "Laberinto 10x10", "Laberinto 50x50",
            "Laberinto 100x100"
        ]

        # datatype of menu text
        self.clicked = tk.StringVar()

        # initial menu text
        self.clicked.set("Seleccione Laberinto")

        #200 para el de 10
        #300 para el de 50  con height=300 y width=300
        #500 para el de 100 con height=500 y width=500

        def seleccionMaze(opcion):
            global maze

            opcion = self.clicked.get()
            if opcion == "Laberinto 5x5":
                maze = "Mazes/maze_5x5.csv"
            elif opcion == "Laberinto 10x10":
                maze = "Mazes/maze_10x10.csv"
            elif opcion == "Laberinto 50x50":
                maze = "Mazes/maze_50x50.csv"
            else: 
                maze = "Mazes/maze_100x100.csv"
            self.destroy()
            gl.matrix = _lectura_maze()
            MazeSolverBoard()

        # Create Dropdown menu
        self.drop = tk.OptionMenu(
            menu_frame,
            self.clicked,
            *options,
            command=seleccionMaze
        )
        self.drop.pack(side=tk.BOTTOM, fill="x")
        self.drop.config(font= ('Helvetica 15'))
        self.drop.config(bg='#5B77AF')

def main():

        """Create the game's board and run its main loop."""
        Menu().mainloop()

if __name__ == "__main__":
    main()
