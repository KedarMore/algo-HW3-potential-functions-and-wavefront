import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

def is_inside(polygon,point):
    """
    docstring
    """
    addx=0
    addy=0
    centroid=[0,0]
    for i in range(len(polygon)):
        addx=addx+polygon[i][0]
        addy=addy+polygon[i][1]
        pass
    centroid[0]=addx/len(polygon)
    centroid[1]=addy/len(polygon)

    polygon=np.vstack((polygon,polygon[0]))

    for i in range(len(polygon)-1):
        a=np.sign(((point[1]-polygon[i][1])/(polygon[i+1][1]-polygon[i][1]))-((point[0]-polygon[i][0])/(polygon[i+1][0]-polygon[i][0])))
        b=np.sign(((centroid[1]-polygon[i][1])/(polygon[i+1][1]-polygon[i][1]))-((centroid[0]-polygon[i][0])/(polygon[i+1][0]-polygon[i][0])))
        if a!=b:
            return 0 #outside
        pass
    return 1 #inside

def param_line(point1,point2):
    """
    docstring
    """
    x=np.linspace(point1[0],point2[0],10)
    y=np.linspace(point1[1],point2[1],10)
    ans=np.vstack((x,y))
    return np.transpose(ans)

def print_input():
    """
    docstring
    """
    a0=float(input("\nEnter the Length of first link: "))
    a1=float(input("\nEnter the Length of second link: "))
    lines=[a0,a1]
    noofobstacles=int(input("\nNumber of Obstacles?"))
    obstacles=[]
    for i in range(noofobstacles):
        vertex=int(input("\nNumber of Vertices on obstacle "+str(i+1)+"?"))
        v1=[]
        for j in range(vertex):
            v2=[]
            v2.append(float(input("\nx Coordinates of vertex "+str(j+1)+"?")))
            v2.append(float(input("\ny Coordinates of vertex "+str(j+1)+"?")))
            v1.append(v2)
            pass
        obstacles.append(v1)
        pass
    return lines, obstacles

def assign_values_nonrectangle(xdegs,ydegs,qgoal):
    """
    assigns initial values to the grid
    """
    # grid=np.zeros((int(360/m1)+1,int(360/m2)+1))
    grid=np.zeros((len(xspace)+1,len(yspace)+1))
    grid[int(qgoal[0]/m1)][int(qgoal[1]/m2)]=2
    for i in range(len(xdegs)):
        grid[(int(xdegs[i]/m1))][(int(ydegs[i]/m2))]=1
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
                    if grid[(i+1)%len(xspace)][j]==0:
                        grid[(i+1)%len(xspace)][j]=number+1
                    if grid[(i-1)%len(xspace)][j]==0:
                        grid[(i-1)%len(xspace)][j]=number+1
                    if grid[i][(j+1)%len(yspace)]==0:
                        grid[i][(j+1)%len(yspace)]=number+1
                    if grid[i][(j-1)%len(yspace)]==0:
                        grid[i][(j-1)%len(yspace)]=number+1
                    pass
                pass
            pass
        pass
    ax.cla()
    plt.imshow(grid.T)
    plt.pause(0.01)
    return grid

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
    snapx=np.array([])
    snapy=np.array([])
    while number>2:
        if grid[(i+1)%len(xspace)][j]==number-1:
            ax.cla()
            i=(i+1)%len(xspace)
            snapx=np.append(snapx,i)
            snapy=np.append(snapy,j)
            distance=distance+gridsizex
            grid[(i)][j]=pathcolour
            plt.imshow(grid.T)
            plt.pause(0.01)
            number=number-1
            continue
        if grid[(i-1)%len(xspace)][j]==number-1:
            ax.cla()
            i=(i-1)%len(xspace)
            snapx=np.append(snapx,i)
            snapy=np.append(snapy,j)
            distance=distance+gridsizex
            grid[(i)][j]=pathcolour
            plt.imshow(grid.T)
            plt.pause(0.01)
            number=number-1
            continue
        if grid[(i)][(j+1)%len(yspace)]==number-1:
            ax.cla()
            j=(j+1)%len(yspace)
            snapx=np.append(snapx,i)
            snapy=np.append(snapy,j)
            distance=distance+gridsizey
            grid[(i)][j]=pathcolour
            plt.imshow(grid.T)
            plt.pause(0.01)
            number=number-1
            continue
        if grid[(i)][(j-1)%len(yspace)]==number-1:
            ax.cla()
            j=(j-1)%len(yspace)
            snapx=np.append(snapx,i)
            snapy=np.append(snapy,j)
            distance=distance+gridsizey
            grid[(i)][j]=pathcolour
            plt.imshow(grid.T)
            plt.pause(0.01)
            number=number-1
            continue
        pass
    return snapx,snapy

def plot(a0,t0,a1,t1):
    """
    Plots the kinematic chain
    """
    x=[a0*(np.cos(t0)),a1*(np.cos(t0+t1))]
    y=[a0*(np.sin(t0)),a1*(np.sin(t0+t1))]

    plt.plot([0,x[0],x[0]+x[1]],[0,y[0],y[0]+y[1]],'bo',alpha=0.5)

    plt.plot([0,x[0],x[0]+x[1]],[0,y[0],y[0]+y[1]],'r-',alpha=0.5)
    
    pass

if __name__ == "__main__":
    # lines,obstacles=print_input()
    m1=10
    m2=10
    lines=[1,1]
    obstacles=[[[0.25, 0.25], [0, 0.75], [-0.25, 0.25]]]
    # obstacles=[[[-0.25, 1.1],[-0.25, 2], [0.25, 2], [0.25, 1.1]],[[-2, -2], [-2, -1.8], [2, -1.8], [2,-2]]]
    # obstacles=[[[-0.25, 1.1], [-0.25, 2], [0.25, 2], [0.25, 1.1]],[[-2, -0.5], [-2, -0.3], [2, -0.3], [2,-0.5]]]
    points=np.array([0,0])
    scatx=np.array([])
    scaty=np.array([])
    for theta1 in tqdm(range(int(360/m1)+1)):
        if theta1*m1==0:
            np.seterr(divide='ignore')
            np.seterr(invalid='ignore')
            px1,py1=lines[0]*(np.cos(np.radians(theta1*m1))),lines[0]*(np.sin(np.radians(theta1*m1)))
            points=np.vstack((points,[px1,py1]))
            pass
        else:
            np.seterr(divide='ignore')
            np.seterr(invalid='ignore')
            points=np.delete(points,-1,0)
            px1,py1=lines[0]*(np.cos(np.radians(theta1*m1))),lines[0]*(np.sin(np.radians(theta1*m1)))
            points=np.vstack((points,[px1,py1]))
            pass
        for theta2 in range(int(360/m2)+1):
            if theta2*m2==0:
                np.seterr(divide='ignore')
                np.seterr(invalid='ignore')
                px2,py2=px1+lines[1]*(np.cos(np.radians(theta1*m1+theta2*m2))),py1+lines[1]*(np.sin(np.radians(theta1*m1+theta2*m2)))
                points=np.vstack((points,[px2,py2]))
                pass
            else:
                np.seterr(divide='ignore')
                np.seterr(invalid='ignore')
                points=np.delete(points,-1,0)
                px2,py2=px1+lines[1]*(np.cos(np.radians(theta1*m1+theta2*m2))),py1+lines[1]*(np.sin(np.radians(theta1*m1+theta2*m2)))
                points=np.vstack((points,[px2,py2]))
                pass
            for o in obstacles:
                inpoints=[0,0]
                for p in range(len(points)-1):
                    inpoints=np.vstack((inpoints,param_line(points[p],points[p+1])))
                    pass
                for ip in inpoints:
                    if is_inside(o,ip)!=0:#inside
                        scatx=np.append(scatx,theta1*m1)
                        scaty=np.append(scaty,theta2*m2)
                        break
                    pass
                pass
            pass
        points=np.delete(points,-1,0)
        pass
    eps=0.1
    qstart=(0,0)
    qgoal=(180,0)
    xlimits=(0,360)
    ylimits=(0,360)
    gridsizex=m1
    gridsizey=m2
    xspace=np.arange(xlimits[0],xlimits[1]+eps,gridsizex)
    yspace=np.arange(ylimits[1],ylimits[0]-eps,-gridsizey)
    grid=assign_values_nonrectangle(scatx,scaty,qgoal)
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
    snap=find_path(grid,number)
    plt.imshow(grid.T)
    plt.close()
    delete=np.arange(0,len(snap[0]),1.5).astype(int)
    snapx=np.delete(snap[0],delete)
    snapy=np.delete(snap[1],delete)
    plt.plot([0,1,2],[0,0,0],'bo')
    plt.plot([0,1,2],[0,0,0],'r-')
    for i in obstacles:
        plt.fill(np.transpose(i)[0],np.transpose(i)[1],color='blue')
        pass
    for i in range(len(snapx)):
        plot(lines[0],np.radians(snapx[i]*10),lines[1],np.radians(snapy[i]*10))
        pass
    plt.plot([0,-1,-2],[0,0,0],'bo')
    plt.plot([0,-1,-2],[0,0,0],'r-')
    plt.show()
    pass