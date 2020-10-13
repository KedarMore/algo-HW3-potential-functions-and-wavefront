import numpy as np
import matplotlib.pyplot as plt

def assign_values(qgoal,xlimits,ylimits):
    """
    assigns initial values to the grid
    """
    xspace=np.arange(xlimits[0],xlimits[1],0.25)
    yspace=np.arange(ylimits[0],ylimits[1],0.25)
    grid=np.zeros((len(xspace),len(yspace)))
    for i in range(len(xspace)):
        for j in range(len(yspace)):
            if xspace[i]==qgoal[0] and yspace[len(yspace)-1-j]==qgoal[1]:
                grid[j][i]=2
                pass
            if inside_obstacle((xspace[i],yspace[len(yspace)-1-j]),obstacles)==1:
                grid[j][i]=1
                pass
            pass
        pass
    grid=grid
    # plt.imshow(grid)
    # plt.show()
    return grid

def update(grid,number):
    """
    updates the grid to number+1
    """
    xspace=np.arange(xlimits[0],xlimits[1],0.25)
    yspace=np.arange(ylimits[0],ylimits[1],0.25)
    for i in range(len(xspace)):
        for j in range(len(yspace)):
            if grid[i][j]==number:
                if grid[(i+1)%len(xspace)][j]==0 and i+1<len(xspace):
                    grid[i+1][j]=number+1
                    pass
                if grid[max((i-1),0)][j]==0 and i-1>0:
                    grid[i-1][j]=number+1
                    pass
                if grid[i][(j+1)%len(yspace)]==0 and j+1<len(yspace):
                    grid[i][j+1]=number+1
                    pass
                if grid[i][max((j-1),0)]==0 and j-1>0:
                    grid[i][j-1]=number+1
                    pass
                pass
            pass
        pass
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

if __name__ == "__main__":

    xlimits=(-2,15)
    ylimits=(-2,15)
    qstart=(0,0)
    qgoal=(10,10)
    obstacles=[[(1,2,2,1),(1,1,5,5)],
               [(3,4,4,3),(4,4,12,12)],
               [(3,12,12,3),(12,12,13,13)],
               [(12,13,13,12),(5,5,13,13)],
               [(6,12,12,6),(5,5,6,6)]]

    

    grid=assign_values(qgoal,xlimits,ylimits)
    for i in range(2,150):
        grid=update(grid,i)
        pass
    plt.imshow(grid)
    plt.show()
    pass