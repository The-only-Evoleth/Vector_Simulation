import numpy as np

class Point: #to make position vectors aka points have its properties 
    all = []
    def __init__(self, pos, initvel=np.array([[0,0,0]])):
        self.pos = pos
        self.initvel = initvel
        Point.all.append(self)



def distance(pos_1, pos_2): #distance between 2 points
    d = np.matmul(pos_1-pos_2, np.transpose(pos_1-pos_2))
    return d ** 0.5

def frc(pt): #the force felt at a certain point or position
    f = np.array([[0,0,0]])
    for i in Point.all:
        d = distance(pt, i.pos)
        if d != np.array([[0]]):
            f = f + ((pt-i.pos)/d )*(1/d**2)
    return f

def dot(a, b): #dot product of 2 position vectors
    r = np.matmul((a*b),np.ones([3,1]))
    return r

def tang_frc(pt): #This is the force(tangent force) that will move the point 
    f = frc(pt)
    r = f - ((pt* dot(pt, f)) / (distance(pt, [[0,0,0]]))**2 ) 
    return r

def acc(pt): #accelaretion
    a = tang_frc(pt)/1
    return a

def newpos(pt, t): #next position of a point after a certain time(t)  
    pos = pt.pos
    u = pt.initvel
    a = acc(pt.pos)

    s = (u*t) + ((a*(t**2))/2)
    v = (u + (a*t))
    pt.initvel = v
    newpos = (pos + s) * distance(pos, [[0,0,0]])/distance((pos+s), [[0,0,0]])    
    return newpos


def conv_to_unitv(pos): #converts any vector to unit vector
    r = pos/distance(pos, [[0,0,0]])
    return r

def prettyfier(pos): # [[1,2,4]] -> {1,2,4}  
    x = str(pos)[2:-2].split()
    xf = ""
    for i in x:
        xf += ","+ i
    xf = "{"+ xf[1:] +"}"
    return xf