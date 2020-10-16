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
            if inside_obstacle((xspace[x],yspace[y]),obstacles)==1:
                func[x][y]=100000
                pass
            else:
                if dist<=dstar:
                    func[x][y]=(1/2)*scale*dist**2
                    pass
                else:
                    func[x][y]=dstar*scale*dist-(1/2)*scale*dstar**2
                    pass
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
    scale=500
    for x in range(len(xspace)):
        for y in range(len(yspace)):
            dist,obs=leastdist_from_obstacle(xspace[x],yspace[y],obstacles)
            if inside_obstacle((xspace[x],yspace[y]),obstacles)==1:
                func[x][y]=1000
                pass
            else:
                if qstar[obs]>dist:
                    func[x][y]=(scale/2)*((1/qstar[obs])-(1/dist))**2
                    # func[x][y]=scale*round(dist,2)
                    # func[x][y]=100
                    pass
                pass
            pass
        pass
    return func

def centriod_repulsive(obstacles,xlimits,ylimits):
    """
    trial
    """
    xspace=np.linspace(xlimits[0],xlimits[1],grid)
    yspace=np.linspace(ylimits[0],ylimits[1],grid)
    func=np.zeros((len(xspace),len(yspace)))
    scale=500
    for x in range(len(xspace)):
        for y in range(len(yspace)):
            if inside_obstacle((xspace[x],yspace[y]),obstacles)==1:
                func[x][y]=1000
                pass
            else:
                for obs in obstacles:
                    centroid=np.average(obs,axis=1)
                    dist=np.sqrt((xspace[x]-centroid[0])**2+(yspace[y]-centroid[1])**2)
                    if dist<=2.6:
                        func[x][y]=scale/dist**2
                        pass
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
    mindist=float('inf')
    for i,points in enumerate(listofpoints):
        dist=np.sqrt((x-points[0])**2+(y-points[1])**2)
        if dist<mindist:
            mindist=dist
            obs=int(i/80)
            pass
        pass
    return mindist,obs

def plot_gradient(gradient):
    """
    plots the entire potential function
    """
    shape=np.shape(gradient[0])
    for i in range(shape[0]):
        for j in range(shape[1]):
            theta=np.arctan2(gradient[1][i][j],gradient[0][i][j])
            # if (theta<=np.radians(0.1) and theta>=np.radians(0)) or (theta<=np.radians(0) and theta>=np.radians(-0.1)) or (theta<=np.radians(90+0.1) and theta>=np.radians(90-0.1)) or (theta<=np.radians(180) and theta>=np.radians(180-0.1)) or (theta>=np.radians(-180) and theta<=np.radians(-180+0.1)) or (theta>=np.radians(-90-0.1) and theta<=np.radians(-90+0.1)):
            if theta!=0 and theta!=np.radians(90) and theta!=np.radians(180) and theta!=np.radians(-90):
                plt.arrow(xlinspace[i],ylinspace[j],0.09*np.cos(theta),0.09*np.sin(theta),head_width=0.09)
                # plt.arrow(xlinspace[i],ylinspace[j],0.009*gradient[0][i][j],0.009*gradient[1][i][j],head_width=0.09)
                pass
            # else:
            #     plt.arrow(xlinspace[i],ylinspace[j],0.09*np.cos(theta),0.09*np.sin(theta),head_width=0.09)
            #     pass
            pass
        pass
    pass

def inside_obstacle(point,obstacle):
    """
    returns 1 if the point is inside any obstacles
    0 otherwise
    """
    for obs in obstacle:
        # if point[0]>obs[0][0]-qstar/4 and point[0]<obs[0][2]+qstar/4 and point[1]>obs[1][0]-qstar/4 and point[1]<obs[1][2]+qstar/4:
        if point[0]>obs[0][0] and point[0]<obs[0][2] and point[1]>obs[1][0] and point[1]<obs[1][2]:
            return 1
    return 0

def create_path(gradient,qstart):
    """
    generate a path from the input potential function
    """
    mindist=float('inf')
    for i in range(len(xlinspace)):
        for j in range(len(ylinspace)):
            dist=np.sqrt((xlinspace[i]-qstart[0])**2+(ylinspace[j]-qstart[1])**2)
            if dist<=mindist:
                mindist=dist
                imin=i
                jmin=j
                pass
            pass
        pass
    direction=np.array([np.radians(0),np.radians(45),np.radians(90),np.radians(135),np.radians(179.9),np.radians(-179.9),np.radians(-135),np.radians(-90),np.radians(-45)])
    newimin=imin
    newjmin=jmin
    for number in range(45):
    # while np.sqrt((qgoal[0]-xlinspace[newimin])**2+(qgoal[1]-ylinspace[newjmin])**2)>=1:
        adist=np.array([])
        angle=np.arctan2(gradient[1][imin][jmin],gradient[0][imin][jmin])
        for a in direction:
            adist=np.append(adist,np.absolute(angle-a))
            pass
        dirmin=np.argmin(adist)
        if dirmin==0:
            newimin=imin+1
            newjmin=jmin
            pass
        if dirmin==1:
            newimin=imin+1
            newjmin=jmin+1
            pass
        if dirmin==2:
            newimin=imin
            newjmin=jmin+1
            pass
        if dirmin==3:
            newimin=imin-1
            newjmin=jmin+1
            pass
        if dirmin==4:
            newimin=imin-1
            newjmin=jmin
            pass
        if dirmin==5:
            newimin=imin-1
            newjmin=jmin
            pass
        if dirmin==6:
            newimin=imin-1
            newjmin=jmin-1
            pass
        if dirmin==7:
            newimin=imin
            newjmin=jmin-1
            pass
        if dirmin==8:
            newimin=imin+1
            newjmin=jmin-1
            pass
        plt.plot((xlinspace[imin],xlinspace[newimin]),(ylinspace[jmin],ylinspace[newjmin]))
        imin=newimin
        jmin=newjmin
        pass
    pass

if __name__ == "__main__":

    # xlimits=(2,11)
    # ylimits=(-3,3)
    # qstart=(0,0)
    # qgoal=(10,0)
    # obstacles=[[(3.5,4.5,4.5,3.5),(0.5,0.5,1.5,1.5)],
    #            [(6.5,7.5,7.5,6.5),(-1.5,-1.5,-0.5,-0.5)]]

    xlimits=(-2,15)
    ylimits=(-2,15)
    qstart=(0,0)
    qgoal=(10,10)
    obstacles=[[(1,2,2,1),(1,1,5,5)],
               [(3,4,4,3),(4,4,12,12)],
               [(3,12,12,3),(12,12,13,13)],
               [(12,13,13,12),(5,5,13,13)],
               [(6,12,12,6),(5,5,6,6)]]
    qstar=[0.25,0.25,0.25,0.25,1.]

    # xlimits=(-10,40)
    # ylimits=(-8,8)
    # qstart=(0,0)
    # qgoal=(35,0)
    # obstacles=[[(-6,25,25,-6),(-6,-6,-5,-5)],
    #            [(-6,30,30,-6),(5,5,6,6)],
    #            [(-6,-5,-5,-6),(-5,-5,5,5)],
    #            [(4,5,5,4),(-5,-5,1,1)],
    #            [(9,10,10,9),(0,0,5,5)],
    #            [(14,15,15,14),(-5,-5,1,1)],
    #            [(19,20,20,19),(0,0,5,5)],
    #            [(24,25,25,24),(-5,-5,1,1)],
    #            [(29,30,30,29),(0,0,5,5)]]

    grid=50 # number of points on the workspace
    dstar=10
    # qstar=0.25

    xlinspace=np.linspace(xlimits[0],xlimits[1],grid)
    ylinspace=np.linspace(ylimits[0],ylimits[1],grid)

    a=attractive_function(qgoal[0],qgoal[1],xlimits,ylimits)
    r=repulsive_function(obstacles,xlimits,ylimits)
    c=centriod_repulsive(obstacles,xlimits,ylimits)
    total=a+r+c
    
    figure, axes = plt.subplots()
    gradient=np.gradient(-total)
    plot_gradient(gradient)
    # axes.add_artist(plt.Circle(qgoal,dstar/2,alpha=0.5))
    # for obs in obstacles:
    #     axes.add_artist(plt.Rectangle((obs[0][0],obs[1][0]),(obs[0][1]-obs[0][0]),(obs[1][2]-obs[1][0]),alpha=0.9))
    #     axes.add_artist(plt.Rectangle((obs[0][0]-qstar,obs[1][0]-qstar),(obs[0][1]-obs[0][0]+2*qstar),(obs[1][2]-obs[1][0]+2*qstar),alpha=0.5))
    #     pass
    # plt.figure(2)
    # figure, axes = plt.subplots()
    create_path(gradient,qstart)
    axes.add_artist(plt.Circle(qgoal,dstar/2,alpha=0.5))
    for i,obs in enumerate(obstacles):
        axes.add_artist(plt.Rectangle((obs[0][0],obs[1][0]),(obs[0][1]-obs[0][0]),(obs[1][2]-obs[1][0]),alpha=0.9))
        axes.add_artist(plt.Rectangle((obs[0][0]-qstar[i],obs[1][0]-qstar[i]),(obs[0][1]-obs[0][0]+2*qstar[i]),(obs[1][2]-obs[1][0]+2*qstar[i]),alpha=0.5))
        pass

    plt.show()