import numpy as np
a = np.array([[1, 1, -1]])
b = np.array([[-1, 1, 2]])

class Point:
    all = []
    def __init__(self, pos, initvel=np.array([[0,0,0]])):
        self.pos = pos
        self.initvel = initvel
        Point.all.append(self)
a = Point(a)
b = Point(b)
#print(c.initvel)
print(Point.all)

def distance(pos_1, pos_2):
    d = np.matmul(pos_1-pos_2, np.transpose(pos_1-pos_2))
    return d ** 0.5


def frc(pt): #pt as position
    f = np.array([[0,0,0]])
    for i in Point.all:
        d = distance(pt, i.pos)
        if d != np.array([[0]]):
            f = f + ((pt-i.pos)/d )*(1/d**2)
    return f

#fa = frc(a)
#print(fa)

def dot(a, b): #2 position vectors
    r = np.matmul((a*b),np.ones([3,1]))
    return r

#print(dot(a,b))

def tang_frc(pt):
    f = frc(pt)
    r = f - ((pt* dot(pt, f)) / (distance(pt, [[0,0,0]]))**2 ) 
    return r
#print(frc(a))
#print(tang_frc(a))

def acc(pt):
    a = tang_frc(pt)/1
    return a
#print(acc(a))

def newpos(pt, t): #a,u are vectors; t is a scaler
    pos = pt.pos
    u = pt.initvel
    a = acc(pt.pos)

    s = (u*t) + ((a*(t**2))/2)
    v = (u + (a*t))
    pt.initvel = v
    newpos = (pos + s) * distance(pos, [[0,0,0]])/distance((pos+s), [[0,0,0]])    
    return newpos

#print(b.initvel)
#b.pos = newpos(b,1)
#print(b.pos)
#print(b.initvel)

#print(distance(b.pos, np.array([[0,0,0]])))
for i in range(8000):
    a.pos = newpos(a,1)
    print(a.pos, a.initvel, acc(a.pos))

