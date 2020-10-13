import numpy as np
import matplotlib.pyplot as plt


'''
possible functions

magnitude=attractive_function(x,y)

magnitude=repulsive_function(x,y)

potential_function(attractive_function,repulsive_function)

gradient

'''

def attractive_function(xgoal,ygoal,xlimits,ylimits):
    """
    returns a numpy-array of all the states (x,y)
    with the magnitude of the attractive potential function
    """
    xspace=np.linspace(xlimits[0],xlimits[1],grid)
    yspace=np.linspace(ylimits[0],ylimits[1],grid)
    func=np.zeros((len(xspace),len(yspace)))
    scale=10
    for x in range(len(xspace)):
        for y in range(len(yspace)):
            dist=np.sqrt((xspace[x]-xgoal)**2+(yspace[y]-ygoal)**2)
            if dist<=dstar:
                func[x,y]=round(((1/2)*scale*dist**2),1)
                pass
            else:
                func[x,y]=round((dstar*scale*dist-(1/2)*scale*dstar**2),1)
                pass
            pass
        pass
    return func

# dist measured from the point on obstacle nearest to the point 

def repulsive_function(obstacles,xlimits,ylimits):
    """
    returns a numpy-array of all states (x,y)
    with the magnitude of the attractive potential function
    """
    xspace=np.linspace(xlimits[0],xlimits[1],grid)
    yspace=np.linspace(ylimits[0],ylimits[1],grid)
    func=np.zeros((len(xspace),len(yspace)))
    scale=100
    for x in range(len(xspace)):
        for y in range(len(yspace)):
            dist=leastdist_from_obstacle(xspace[x],yspace[y],obstacles)
            if inside_obstacle((xspace[x],yspace[y]),obstacles)==1:
                func[x][y]=500
                pass
            else:
                if qstar>dist:
                    func[x][y]=round(((scale/2)*((1/qstar)-(1/dist))**2),1)
                    # func[x][y]=scale*round(dist,2)
                    # func[x][y]=100
                    pass
                pass
            pass
        pass
    return func

def points_on_obstacles(obstacles):
    """
    returns an np-array of all the points on the boundary obstacle
    """
    listofpointsx=np.array([])
    listofpointsy=np.array([])
    for obs in obstacles:
        obs=np.transpose(obs)
        for points in range(len(obs)):
            listofpointsx=np.append(listofpointsx,np.linspace(obs[points%len(obs)][0],obs[(points+1)%len(obs)][0],20))
            listofpointsy=np.append(listofpointsy,np.linspace(obs[points%len(obs)][1],obs[(points+1)%len(obs)][1],20))
            pass
        pass
    listofpoints=np.vstack((listofpointsx,listofpointsy))
    return listofpoints.T

def leastdist_from_obstacle(x,y,obstacles):
    """
    returns the distance from the obstacle to the given point
    """
    listofpoints=points_on_obstacles(obstacles)
    # print(listofpoints)
    mindist=float('inf')
    for points in listofpoints:
        dist=np.sqrt((x-points[0])**2+(y-points[1])**2)
        if dist<mindist:
            mindist=dist
            pass
        pass
    return mindist

def plot_gradient(gradient):
    """
    plots the entire potential function
    """
    shape=np.shape(gradient[0])
    for i in range(shape[0]):
        for j in range(shape[1]):
            theta=np.arctan2(-gradient[1][i][j],-gradient[0][i][j])
            if theta!=0:
                plt.arrow(xlinspace[i],ylinspace[j],0.1*np.cos(theta),0.1*np.sin(theta),head_width=0.1)
                pass
            pass
        pass
    pass

def inside_obstacle(point,obstacle):
    """
    returns 1 if the point is inside any obstacles
    0 otherwise
    """
    for obs in obstacle:
        if point[0]>=obs[0][0] and point[0]<=obs[0][2] and point[1]>=obs[1][0] and point[1]<=obs[1][2]:
            return 1
    return 0

def create_path(gradient):
    """
    generate a path from the input potential function
    """

    pass

if __name__ == "__main__":

    xlimits=(1,11)
    ylimits=(-5,5)
    qstart=(0,0)
    qgoal=(10,0)
    obstacles=[[(3.5,4.5,4.5,3.5),(0.5,0.5,1.5,1.5)],
               [(6.5,7.5,7.5,6.5),(-1.5,-1.5,-0.5,-0.5)]]

    # xlimits=(-2,20)
    # ylimits=(-2,20)
    # qstart=(0,0)
    # qgoal=(10,10)
    # obstacles=[[(1,2,2,1),(1,1,5,5)],
    #            [(3,4,4,3),(4,4,12,12)],
    #            [(3,12,12,3),(12,12,13,13)],
    #            [(12,13,13,12),(5,5,13,13)],
    #            [(6,12,12,6),(5,5,6,6)]]

    # xlimits=(-10,40)
    # ylimits=(-8,8)
    # qstart=(0,0)
    # qgoal=(35,0)
    # obstacles=[[(-6,25,25,24,24,15,15,14,14,5,5,4,4,-5,-5,9,9,10,10,19,19,20,20,29,29,30,30,-6),(-6,-6,1,1,-5,-5,1,1,-5,-5,1,1,-5,-5,5,5,0,0,5,5,0,0,5,5,0,0,6,6)]]

    grid=50 # number of points on the workspace
    dstar=1
    qstar=0.5

    xlinspace=np.linspace(xlimits[0],xlimits[1],grid)
    ylinspace=np.linspace(ylimits[0],ylimits[1],grid)

    a=attractive_function(qgoal[0],qgoal[1],xlimits,ylimits)
    r=repulsive_function(obstacles,xlimits,ylimits)
    total=a+r

    gradient=np.gradient(total)
    plot_gradient(gradient)
    plt.show()