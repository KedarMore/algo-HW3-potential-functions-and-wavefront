import numpy as np
import matplotlib.pyplot as plt

def assign_values(qgoal,xlimits,ylimits):
    """
    assigns initial values to the grid
    """
    grid=np.zeros((len(xspace),len(yspace)))
    for i in range(len(xspace)):
        for j in range(len(yspace)):
            if xspace[i]==qgoal[0] and yspace[j]==qgoal[1]:
                grid[i][j]=2
                pass
            if inside_obstacle((xspace[i],yspace[j]),obstacles)==1:
                grid[i][j]=1
                pass
            pass
        pass
    return grid

def update(grid,number):
    """
    updates the grid to number+1
    """
    for i in range(len(xspace)):
        for j in range(len(yspace)):
            if grid[i][j]==number:
                if xspace[i]==qstart[0] and yspace[j]==qstart[1]:
                    return grid,number
                else:
                    if grid[(i+1)%len(xspace)][j]==0 and i+1<len(xspace):
                        grid[i+1][j]=number+1
                    if grid[max((i-1),0)][j]==0 and i-1>0:
                        grid[i-1][j]=number+1
                    if grid[i][(j+1)%len(yspace)]==0 and j+1<len(yspace):
                        grid[i][j+1]=number+1
                    if grid[i][max((j-1),0)]==0 and j-1>0:
                        grid[i][j-1]=number+1
                    pass
                pass
            pass
        pass
    ax.cla()
    plt.imshow(grid.T)
    plt.pause(0.01)
    return grid

def inside_obstacle(point,obstacle):
    """
    returns 1 if the point is inside any obstacles
    0 otherwise
    """
    for obs in obstacle:
        if point[0]>=obs[0][0] and point[0]<=obs[0][2] and point[1]>=obs[1][0] and point[1]<=obs[1][2]:
            return 1
    return 0

def find_path(grid,number):
    """
    plots a path from qgoal to qstart
    """
    pathcolour=number+10
    i=np.where(xspace==qstart[0])
    i=i[0][0]
    j=np.where(yspace==qstart[1])
    j=j[0][0]
    grid[(i)][j]=pathcolour
    distance=0
    while number>2:
        if grid[(i+1)][j]==number-1:
            ax.cla()
            i=i+1
            distance=distance+gridsize
            grid[(i)][j]=pathcolour
            plt.imshow(grid.T)
            plt.pause(0.01)
            number=number-1
            continue
        elif grid[(i-1)][j]==number-1:
            ax.cla()
            i=i-1
            distance=distance+gridsize
            grid[(i)][j]=pathcolour
            plt.imshow(grid.T)
            plt.pause(0.01)
            number=number-1
            continue
        elif grid[(i)][j+1]==number-1:
            ax.cla()
            j=j+1
            distance=distance+gridsize
            grid[(i)][j]=pathcolour
            plt.imshow(grid.T)
            plt.pause(0.01)
            number=number-1
            continue
        elif grid[(i)][j-1]==number-1:
            ax.cla()
            j=j-1
            distance=distance+gridsize
            grid[(i)][j]=pathcolour
            plt.imshow(grid.T)
            plt.pause(0.01)
            number=number-1
            continue
        pass
    return distance


if __name__ == "__main__":

    xlimits=(-2,12)
    ylimits=(-5,5)
    qstart=(0,0)
    qgoal=(10,0)
    obstacles=[[(3.5,4.5,4.5,3.5),(0.5,0.5,1.5,1.5)],
               [(6.5,7.5,7.5,6.5),(-1.5,-1.5,-0.5,-0.5)]]

    # xlimits=(-2,15)
    # ylimits=(-2,15)
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
    # obstacles=[[(-6,25,25,-6),(-6,-6,-5,-5)],
    #            [(-6,30,30,-6),(5,5,6,6)],
    #            [(-6,-5,-5,-6),(-5,-5,5,5)],
    #            [(4,5,5,4),(-5,-5,1,1)],
    #            [(9,10,10,9),(0,0,5,5)],
    #            [(14,15,15,14),(-5,-5,1,1)],
    #            [(19,20,20,19),(0,0,5,5)],
    #            [(24,25,25,24),(-5,-5,1,1)],
    #            [(29,30,30,29),(0,0,5,5)]]

    gridsize=0.5

    xspace=np.arange(xlimits[0],xlimits[1],gridsize)
    yspace=np.arange(ylimits[1],ylimits[0],-gridsize)
    grid=assign_values(qgoal,xlimits,ylimits)
    fig,ax=plt.subplots()
    number=2
    while True:
        newgrid=update(grid,number)
        if len(newgrid)==2:
            grid,number=newgrid
            print("found qstart")
            break
        else:
            grid=newgrid
            number=number+1
            pass
    dist=find_path(grid,number)
    print("Total distace of the path is:",dist)
    plt.imshow(grid.T)
    plt.show()
    pass