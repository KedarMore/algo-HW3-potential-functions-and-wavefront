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

if __name__ == "__main__":
    # lines,obstacles=print_input()
    m1=10
    m2=10
    lines=[1,1]
    # obstacles=[[[0.25, 0.25], [0, 0.75], [-0.25, 0.25]]]
    # obstacles=[[[-0.25, 1.1],[-0.25, 2], [0.25, 2], [0.25, 1.1]],[[-2, -2], [-2, -1.8], [2, -1.8], [2,-2]]]
    obstacles=[[[-0.25, 1.1], [-0.25, 2], [0.25, 2], [0.25, 1.1]],[[-2, -0.5], [-2, -0.3], [2, -0.3], [2,-0.5]]]
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
    print(scatx,scaty)
    ax=plt.subplot(1,2,1)
    plt.title("Obstacles")
    plt.xlabel("X")
    plt.ylabel("Y")
    for i in obstacles:
        ax.fill(np.transpose(i)[0],np.transpose(i)[1],color='blue')
        pass
    ay=plt.subplot(1,2,2)
    plt.title("C-Space")
    plt.xlabel("Theta 1")
    plt.ylabel("Theta 2")
    ay.scatter(scatx,scaty,s=90,color='blue')
    plt.xlim(0,360)
    plt.ylim(0,360)
    plt.show()
    pass