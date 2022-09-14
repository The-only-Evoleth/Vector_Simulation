import numpy as np

class Point: #to make position vectors aka points have its properties 
    all = []
    def __init__(self, pos, initvel=np.array([[0,0,0]])):
        self.pos = pos
        self.initvel = initvel
        Point.all.append(self)

    def test(self,t):
        print(f"{self.pos} > Ima-live {t}")

    @staticmethod
    def distance(pos_1, pos_2): #distance between 2 points
        d = np.matmul(pos_1-pos_2, np.transpose(pos_1-pos_2))
        return d ** 0.5

    def frc(self): #the force felt at a certain point or position
        f = np.array([[0,0,0]])
        for i in Point.all:
            d = Point.distance(self.pos, i.pos)
            if d != np.array([[0]]):
                f = f + ((self.pos-i.pos)/d )*(1/d**2)
        return f

    @staticmethod
    def dot(a, b): #dot product of 2 position vectors
        r = np.matmul((a*b),np.ones([3,1]))
        return r

    def tang_frc(self): #This is the force(tangent force) that will move the point 
        f = self.frc()
        r = f - ((self.pos* Point.dot(self.pos, f)) / (Point.distance(self.pos, [[0,0,0]]))**2 ) 
        return r

    def acc(self): #accelaretion
        a = self.tang_frc()/1
        return a

    def nextpos(self, t): #next position of a point after a certain time(t)  
        pos = self.pos
        u = self.initvel
        a = self.acc()

        s = (u*t) + ((a*(t**2))/2)
        v = (u + (a*t))
        self.initvel = v
        newpos = (pos + s) * Point.distance(pos, [[0,0,0]])/Point.distance((pos+s), [[0,0,0]])    
        self.pos = newpos
        
    @staticmethod
    def conv_to_unitv(pos): #converts any vector to unit vector
        r = pos/Point.distance(pos, [[0,0,0]])
        return r

    @staticmethod
    def prettyfier(pos): # [[1,2,4]] -> {1,2,4}  
        x = str(pos)[2:-2].split()
        xf = ""
        for i in x:
            xf += ","+ i
        xf = "{"+ xf[1:] +"}"
        return xf