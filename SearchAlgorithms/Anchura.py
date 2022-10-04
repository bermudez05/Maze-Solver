# pseudo codigo
# obtener acciones disponibles ( y posibles de realizar SeekAround)
# ponerlas en orden de anchura (fifo)
#mover el agente (agent_post)
#repetir
import collections as cll
from . import globals as gl
def Anchura(canvas):
  cola = cll.deque(gl.agent_post) 
  # Queue implicito dequeue=popleft()
  while gl.agent_pos != gl.goal_pos and not(cola.empty()):
    gl.agent_pos = cola.popleft() # posicion justo ahora
    #-----ojo con como se define la marcha,  no se esta moviendo el agente en tiempo real 
    if gl.agent_pos == gl.goal_pos:
      SolutionTrace()
      break
    gl.matrix[gl.agent_pos[0]][gl.agent_pos[1]]==2 # lo marca en la matriz como visto
    map (lambda x: cola.append(x),SeekAround(gl.agent_pos,gl.matrix)) # si el vecino es valido entonces entra en la cola
  return    
def SeekAround(post,matrix):
  accions = [[0,1],[1,0],[-1,0],[0,-1]]
  posibles=[]
  for mov in accions:
        if(post[0]+mov[0]>=0) and (post[0]+mov[0]< len(gl.matrix)) and (post[1]+mov[1]>=0) and (post[1]+mov[1]< len(gl.matrix[0])):
          if (gl.matrix[post[0]+mov[0]][post[1]+mov[1]]==1):
            posibles.append([post[0]+mov[0],post[1]+mov[1]])
      #si esta dentro de los limites & es casilla virgen
  return posibles
def SolutionTrace():
  # crear el arbol de soluciones
  #MARCAR RECORRIDO HACIA ATRAS ---
  #mensaje feliz! :D
  print("Maze resolved") 
