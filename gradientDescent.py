import numpy as np


'''
possible functions

magnitude=attractive_function(x,y)

magnitude=repulsive_function(x,y)

potential_function(attractive_function,repulsive_function)

gradient

'''

dstar=1

def attractive_function(xgoal,ygoal,xlimits,ylimits):
    """
    returns a numpy-array of all the states (x,y)
    with the magnitude of the attractive potential function
    """
    xspace=np.linspace(xlimits[0],xlimits[1],10)
    yspace=np.linspace(ylimits[0],ylimits[1],10)
    func=np.zeros((len(xspace),len(yspace)))
    scale=2
    for x in range(len(xspace)):
        for y in range(len(yspace)):
            dist=np.sqrt((xspace[x]-xgoal)**2+(yspace[y]-ygoal)**2)
            if dist<=dstar:
                func[x,y]=round(((1/2)*scale*dist**2),3)
                pass
            else:
                func[x,y]=round((dstar*scale*dist-(1/2)*scale*dstar**2),3)
                pass
            pass
        pass
    return func.T

qstar=0.5

# dist measured from the point on obstacle nearest to the point 

def repulsive_function(obstacles,xlimits,ylimits):
    """
    returns a numpy-array of all states (x,y)
    with the magnitude of the attractive potential function
    """
    xspace=np.linspace(xlimits[1],xlimits[0],18)
    yspace=np.linspace(ylimits[1],ylimits[0],18)
    func=np.zeros((len(xspace),len(yspace)))
    scale=2
    for x in range(len(xspace)):
        for y in range(len(yspace)):
            dist=leastdistfromobstacle(xspace[x],yspace[y],obstacles)
            if qstar>dist:
                func[x][y]=round(((scale/2)*((1/qstar)-(1/dist))**2),1)
                # func[x][y]=round(dist,1)
                # func[x][y]=1
                pass
            pass
        pass
    return func.T

def pointsonobstacles(obstacles):
    """
    returns an np-array of all the points on the boundary obstacle
    """
    listofpointsx=np.array([])
    listofpointsy=np.array([])
    for obs in obstacles:
        obs=np.transpose(obs)
        for points in range(len(obs)):
            listofpointsx=np.append(listofpointsx,np.linspace(obs[points%len(obs)][0],obs[(points+1)%len(obs)][0],50))
            listofpointsy=np.append(listofpointsy,np.linspace(obs[points%len(obs)][1],obs[(points+1)%len(obs)][1],50))
            # stack=np.vstack((listofpointsx,listofpointsy))
            # stack=np.transpose(stack)
            # print(stack)
            # print(listofpoints)
            pass
        pass
    listofpoints=np.vstack((listofpointsx,listofpointsy))
    return listofpoints.T

def leastdistfromobstacle(x,y,obstacles):
    """
    returns the distance from the obstacle to the given point
    """
    listofpoints=pointsonobstacles(obstacles)
    # print(listofpoints)
    mindist=float('inf')
    for points in listofpoints:
        dist=np.sqrt((x-points[0])**2+(y-points[1])**2)
        if dist<mindist:
            mindist=dist
            pass
        pass
    return mindist

if __name__ == "__main__":
    # print(attractive_function(10,0,(-1,11),(-5,5)))
    obstacles=[[(3.5,4.5,4.5,3.5),(0.5,0.5,1.5,1.5)],
               [(6.5,7.5,7.5,6.5),(-1.5,-1.5,-0.5,-0.5)]]
    print(repulsive_function(obstacles,(0,10),(-5,5)))
    pass