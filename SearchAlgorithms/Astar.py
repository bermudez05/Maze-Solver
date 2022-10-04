from profile import Profile
from sortedcontainers import SortedList
from . import globals as gl
from memory_profiler import profile

open=SortedList()
class Vecino(object):
    def __init__(self,post,dstart,parent):
        self.post = post #positino en la matrix
        self.dinit= dstart
        self.dgoal= self.findDistance(gl.goal_pos)
        self.parent = parent
    def getdinit(self):
        return self.dinit
    def getCost(self):
        return self.dinit+self.dgoal
    def __eq__(self, other):
        return self.getCost() == other.getCost()
    def __lt__(self, other):
        return self.getCost() > other.getCost() # asi al hacer pop() se tiene el menor
    def findDistance(self,target):
        return abs(self.post[0]-target[0])+abs(self.post[1]-target[1])
    def close(self,num):
        gl.matrix[self.post[0]][self.post[1]]=num

#@gl.mide_tiempo
@profile
def Astar():
    Profile()
    global open
    agent = Vecino(gl.agent_pos,0,None) #convierte el inicio en un objeto vecino
    open.add(agent) # la estructura esta provada
    #para la proxima podremos usar un arbol rojinegro, por ahora una lista sorteada bien ejecutada
    current=""
    while open.__len__()!=0:
        current = open.pop()
        if current.post == list(gl.goal_pos):
            gl.color_maze()
            SolutionTrace(current)
            break
        open.update(SeekAround(current)) #pone el la lista de prioridad los nodos
        current.close(2)

def SeekAround(current):
    post=current.post
    dstart=current.dinit
    accions = [[0,1],[1,0],[-1,0],[0,-1]]
    posibles=[]
    for mov in accions:
        if(post[0]+mov[0]>=0) and (post[0]+mov[0]< len(gl.matrix)) and (post[1]+mov[1]>=0) and (post[1]+mov[1]< len(gl.matrix[0])):
         #si esta dentro de los limites & es casilla virgen
            if (gl.matrix[post[0]+mov[0]][post[1]+mov[1]]==1):
                posible_mov=[post[0]+mov[0] ,post[1]+mov[1]]
                a=True
                for x in open: # si encuentra que ya era vecino actualiza el 
                    if x.post == posible_mov: 
                        if x.dinit > (dstart+1) : 
                            x.dinit= dstart+1
                            x.parent = current
                            a=False
                if a: posibles.append(Vecino(posible_mov,dstart+1,current)) 
    
    return posibles
def SolutionTrace(current):
  while current.dinit != 0:
        current.close(3)
        current=current.parent
        #pintar los cuadritos del color 3 
  gl.color_maze()       
  print("Maze resolved Astar")
  return  
