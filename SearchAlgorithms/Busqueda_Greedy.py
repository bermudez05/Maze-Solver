from sortedcontainers import SortedList
from . import globals as gl
prioridad = 0
class Vecino(object):
    def __init__(self,post,parent):
        self.post = post #positino en la matrix
        self.dgoal= self.findDistance(gl.goal_pos)
        self.parent = parent
    def __eq__(self, other):
        return self.dgoal == other.dgoal
    def findDistance(self,target):
        return abs(self.post[0]-target[0])+abs(self.post[1]-target[1])
    def __lt__(self, other):
        return self.dgoal > other.dgoal # asi al hacer pop() se tiene el menor
    def getdgoal(self):
        return self.dgoal  
    def close(self,num):
        gl.matrix[self.post[0]][self.post[1]]=num 
def Greedy():
        print("greedy bitches")
        global prioridad
        #SEEK AROUND (ACCIONES POSIBLES ) Y PONERLA EN COLA DE PRIORIDAD DE MENOR DISTANCIA
        agent = Vecino(gl.agent_pos,None)
        prioridad = SortedList([agent])
        current =""
        while prioridad.__len__()!=0:
                current = prioridad.pop()
                if current.post == list(gl.goal_pos):
                        gl.color_maze()
                        SolutionTrace(current)
                        break
                prioridad= SortedList(SeekAround(current)) #pone el la lista de prioridad los nodos  
                current.close(2)
        #MOVERSE A DONDE CUESTE MENOS
        #REPETIR
        return
def SeekAround(current):
        post=current.post
        accions = [[0,1],[1,0],[-1,0],[0,-1]]
        posibles=[]
        for mov in accions:
                if(post[0]+mov[0]>=0) and (post[0]+mov[0]< len(gl.matrix)) and (post[1]+mov[1]>=0) and (post[1]+mov[1]< len(gl.matrix[0])):         #si esta dentro de los limites & es casilla virgen
                        if (gl.matrix[post[0]+mov[0]][post[1]+mov[1]]==1):
                                posible_mov=[post[0]+mov[0] ,post[1]+mov[1]]
                                posibles.append(Vecino(posible_mov,current)) # posicion del vecino,posicion de padre,movimiento realizado
        return posibles
def SolutionTrace(current):
  while current.dinit != 0:
        current.close(3)
        current=current.parent
  gl.matrix[gl.agent_pos[0]][gl.agent_pos[1]]=3     
  gl.matrix[gl.goal_pos[0]][gl.goal_pos[1]]=3     
  gl.color_maze() 
        #pintar los cuadritos del color 3 
  print("Maze resolved :D")