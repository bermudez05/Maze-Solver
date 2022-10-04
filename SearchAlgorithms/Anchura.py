# pseudo codigo
# obtener acciones disponibles ( y posibles de realizar SeekAround)
# ponerlas en orden de anchura (fifo)
#mover el agente (agent_post)
#repetir
import collections as cll
from . import globals as gl
from memory_profiler import profile
cola =cll.deque()

#@profile
@gl.mide_tiempo
def Anchura(canvas):
  cola.append(list(gl.agent_pos)) 
  # Queue implicito dequeue=popleft()
  while len(cola) != 0:
    gl.agent_pos = cola.popleft() # posicion justo ahora
    #-----ojo con como se define la marcha,  no se esta moviendo el agente en tiempo real 
    if gl.agent_pos == list(gl.goal_pos):
      SolutionTrace()
      break
    SeekAround(gl.agent_pos)
    gl.matrix[gl.agent_pos[0]][gl.agent_pos[1]]=2# lo marca en la matriz como visto

  return    
def SeekAround(post):
  accions = [[0,1],[1,0],[-1,0],[0,-1]]
  for mov in accions:
        if(post[0]+mov[0]>=0) and (post[0]+mov[0]< len(gl.matrix)) and (post[1]+mov[1]>=0) and (post[1]+mov[1]< len(gl.matrix[0])):
          if (gl.matrix[post[0]+mov[0]][post[1]+mov[1]]==1):
            cola.append([post[0]+mov[0],post[1]+mov[1]])
      #si esta dentro de los limites & es casilla virgen

def SolutionTrace():
  gl.matrix[gl.goal_pos[0]][gl.goal_pos[1]]=3
  gl.color_maze()
  print("Maze resolved")
