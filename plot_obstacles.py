import matplotlib.pyplot as plt

# obstacles represented in the following format
# 
# obstacles=[[(x coordinatinates),(y coordinatinates)] ,[(),()], ...]
#             obstacle1                                  obstacle2...


# Exercise 2 a

# qstart=(0,0)
# qgoal=(10,0)

# obstacles=[[(3.5,4.5,4.5,3.5),(0.5,0.5,1.5,1.5)],
#            [(6.5,7.5,7.5,6.5),(-1.5,-1.5,-0.5,-0.5)]]

# Exercise 2 b(1)

qstart=(0,0)
qgoal=(10,10)

obstacles=[[(1,2,2,1),(1,1,5,5)],
           [(3,4,4,12,12,6,6,13,13,3),(4,4,12,12,6,6,5,5,13,13)]]

# Exercise 2 b(2)

# qstart=(0,0)
# qgoal=(35,0)

# obstacles=[[(-6,25,25,24,24,15,15,14,14,5,5,4,4,-5,-5,9,9,10,10,19,19,20,20,29,29,30,30,-6),(-6,-6,1,1,-5,-5,1,1,-5,-5,1,1,-5,-5,5,5,0,0,5,5,0,0,5,5,0,0,6,6)]]


def plot(qstart,qgoal,obstacles):
    """
    plots the obstacles
    """
    for obs in obstacles:
        plt.fill(*obs,'k')

    plt.plot(qstart[0],qstart[1],'ro')

    plt.plot(qgoal[0],qgoal[1],'go')

    pass

if __name__ == "__main__":
    plot(qstart,qgoal,obstacles)
    plt.show()
    pass