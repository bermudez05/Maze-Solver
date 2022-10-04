from sortedcontainers import SortedList
from . import globals as gl
prioridad = 0
class Vecino(object):
    def __init__(self,post,dinit,parent):
        self.post = post #positino en la matrix
        self.dinit= dinit
        self.parent = parent
    def __eq__(self, other):
        return self.dinit == other.dinit
    def __lt__(self, other):
        return self.dinit > other.dinit # asi al hacer pop() se tiene el menor
    def getdinit(self):
        return self.dinit  
    def close(self,num):
        gl.matrix[self.post[0]][self.post[1]]=num     

def Costo_uniforme():
        global prioridad
        #SEEK AROUND (ACCIONES POSIBLES ) Y PONERLA EN COLA DE PRIORIDAD DE MENOR DISTANCIA
        agent = Vecino(gl.agent_pos,0,None)
        prioridad = SortedList([agent])
        current =""
        while prioridad.__len__()!=0:
                current = prioridad.pop()
                if current.post == list(gl.goal_pos):
                        gl.color_maze()
                        SolutionTrace(current)
                        break
                prioridad.update(SeekAround(current)) #pone el la lista de prioridad los nodos  
                current.close(2)
        #MOVERSE A DONDE CUESTE MENOS
        #REPETIR
        return
def SeekAround(current):
        post=current.post
        dstart=current.dinit
        accions = [[0,1],[1,0],[-1,0],[0,-1]]
        posibles=[]
        for mov in accions:
            if(post[0]+mov[0]>=0) and (post[0]+mov[0]< len(gl.matrix)) and (post[1]+mov[1]>=0) and (post[1]+mov[1]< len(gl.matrix[0])):         #si esta dentro de los limites & es casilla virgen
                    if (gl.matrix[post[0]+mov[0]][post[1]+mov[1]]==1):
                        posible_mov=[post[0]+mov[0] ,post[1]+mov[1]]
                        posibles.append(Vecino(posible_mov,dstart+1,current)) # posicion del vecino,posicion de padre,movimiento realizado
        return posibles
def SolutionTrace(current):
  while current.dinit != 0:
        current.close(3)
        current=current.parent
  gl.color_maze() 
  print("Maze resolved")