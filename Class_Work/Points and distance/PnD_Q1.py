# Problem 
# we are given 2D coordinates of following points (0,1), (2,4), (3,6), and (7,7).
# 1.Store following data in python and write a function to determint distance between two points.
# 2.Write a function to estimate polar coordinate of any point.
# 3.Write a function that moves point and determines new position when movement is given
##########################################################################################################
# p1=(0,1)
# p2=(2,4)

# def distance(p1,p2):
#     x1= p1[0]
#     x2= p2[0]
#     y1= p1[1]
#     y2= p2[1]
#     dist=((x2-x1)^2+(y2-y1)^2)**(1/2)
#     return dist

# print(distance(p1,p2))

###########################################################################################################

p1 ={"x":0,"y":1}
p2 ={"x":2,"y":4}
p3 ={"x":3,"y":6}
p4 ={"x":7,"y":7}


def distance(p1 , p2):
    x1=p1["x"]
    x2=p2["x"]
    y1=p1["y"]
    y2=p2["y"]

    dist=((x2-x1)^2+(y2-y1)^2)**(1/2)
    return dist

def polar(p1):
    x=p1["x"]
    y=p1["y"]

    return (r,phi)
print(distance(p3,p1))