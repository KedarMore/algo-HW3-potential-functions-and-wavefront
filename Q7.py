import math
import matplotlib.pyplot as plt

def plot(a0,t0,a1,t1,a2,t2):
    """
    Plots the kinematic chain
    """
    x=[a0*(math.cos(t0)),a1*(math.cos(t0+t1)),a2*(math.cos(t0+t1+t2))]
    y=[a0*(math.sin(t0)),a1*(math.sin(t0+t1)),a2*(math.sin(t0+t1+t2))]

    plt.plot([0,x[0],x[0]+x[1],x[0]+x[1]+x[2]],[0,y[0],y[0]+y[1],y[0]+y[1]+y[2]],'bo')

    plt.plot([0,x[0],x[0]+x[1],x[0]+x[1]+x[2]],[0,y[0],y[0]+y[1],y[0]+y[1]+y[2]],'r-')
    
    return x,y

def forward():
    """
    docstring
    """
    try:
        a0=float(input("\nEnter the length of the first link: "))
        pass
    except:
        print("Enter valid value!!")
        raise SystemExit
    try:
        t0=math.radians(float(input("\nEnter its angle (degrees) wrt the ground: ")))
        pass
    except:
        print("Enter valid value!!")
        raise SystemExit
    try:
        a1=float(input("\nEnter the length of the first link: "))
        pass
    except:
        print("Enter valid value!!")
        raise SystemExit
    try:
        t1=math.radians(float(input("\nEnter its angle (degrees) wrt the previous link: ")))
        pass
    except:
        print("Enter valid value!!")
        raise SystemExit
    try:
        a2=float(input("\nEnter the length of the first link: "))
        pass
    except:
        print("Enter valid value!!")
        raise SystemExit
    try:
        t2=math.radians(float(input("\nEnter its angle (degrees) wrt the previous link: ")))
        pass
    except:
        print("Enter valid value!!")
        raise SystemExit
    
    x,y=plot(a0,t0,a1,t1,a2,t2)
    print("\nPoint 0 is: (0,0)")
    print("\nPoint 1 is: ("+str(round((x[0]),3))+","+str(round((y[0]),3))+")")
    print("\nPoint 2 is: ("+str(round((x[0]+x[1]),3))+","+str(round((y[0]+y[1]),3))+")")
    print("\nFinal position is: ("+str(round((x[0]+x[1]+x[2]),3))+","+str(round((y[0]+y[1]+y[2]),3))+")")

    plt.annotate("Start\n(0,0)",(0,0))
    plt.annotate("("+str(round((x[0]),3))+","+str(round((y[0]),3))+")",(x[0],y[0]))
    plt.annotate("("+str(round((x[0]+x[1]),3))+","+str(round((y[0]+y[1]),3))+")",(x[0]+x[1],y[0]+y[1]))
    plt.annotate("End effector\n("+str(round((x[0]+x[1]+x[2]),3))+","+str(round((y[0]+y[1]+y[2]),3))+")",(x[0]+x[1]+x[2],y[0]+y[1]+y[2]))
    plt.title("Q7 Forward Kinematics")
    plt.show()
    pass

def inverse():
    """
    docstring
    """
    try:
        a0=float(input("\nEnter the length of the first link: "))
        pass
    except:
        print("Enter valid value!!")
        raise SystemError
    try:
        a1=float(input("\nEnter the length of the second link: "))
        pass
    except:
        print("Enter valid value!!")
        raise SystemError
    try:
        a2=float(input("\nEnter the length of the third link: "))
        pass
    except:
        print("Enter valid value!!")
        raise SystemError

    try:
        x=float(input("\nEnter end-effector x value: "))
        pass
    except:
        print("Enter valid value!!")
        raise SystemError
    try:
        y=float(input("\nEnter end-effector y value: "))
        pass
    except:
        print("Enter valid value!!")
        raise SystemError
    
    minr=2*max(a0,a1,a2)-(a0+a1+a2)
    maxr=a0+a1+a2
    if minr<0:
        minr=0
    if math.sqrt(pow(x,2)+pow(y,2))<minr or maxr<math.sqrt(pow(x,2)+pow(y,2)):
        print("not possible")
        pass
    else:# put code here
        for t1 in range(360):
            for t2 in range(360):
                p1=(a0*math.cos(math.radians(t1)),a0*math.sin(math.radians(t1)))
                p2=(x+a2*math.cos(math.radians(t2)),y+a2*math.sin(math.radians(t2)))
                dist=math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
                if dist<(a1+0.001) and dist>(a1-0.001): # threshold
                    print("found")
                    theta1=math.radians(t1)
                    if math.atan2((p2[1]-p1[1]),(p2[0]-p1[0]))<0:
                        theta2=math.radians(360)+math.atan2((p2[1]-p1[1]),(p2[0]-p1[0]))-theta1
                        pass
                    else:
                        theta2=math.atan2((p2[1]-p1[1]),(p2[0]-p1[0]))-theta1
                        pass
                    theta3=math.radians(t2)-math.radians(180)-theta2-theta1
                pass
            pass
        plot(a0,theta1,a1,theta2,a2,theta3)
        plt.annotate("Start",(0,0))
        plt.annotate("End-effector ("+str(x)+","+str(y)+")",(x,y))
        print("One of the configuration is: ",round(math.degrees(theta1),2),round(math.degrees(theta2),2),round(math.degrees(theta3),2)," degrees")
        plt.title("Q7 Inverse Kinematics")
        plt.show()
        pass
    pass

if __name__ == "__main__":
    choice=input("\nForward or Inverse?")
    if choice=='Forward':
        forward()
        pass
    elif choice=='Inverse':
        inverse()
        pass
    else:
        print("Enter valid choice!!")
        pass
    pass