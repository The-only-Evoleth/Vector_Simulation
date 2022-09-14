from utils import *

a = Point(Point.conv_to_unitv(np.array([[0,0,1]])))
b = Point(Point.conv_to_unitv(np.array([[-1,1,2]])))
c = Point(Point.conv_to_unitv(np.array([[3,-2,0]])))
#d = Point(conv_to_unitv(np.array([[-1,-2,-9]])))
#e = Point(conv_to_unitv(np.array([[1,1,0]])))


for i in range(100): #here range depicts how many times the sim will run. More points may take more steps to reach stable state
    b.nextpos(1)
    c.nextpos(1)
 #   d.nextpos(1)
 #   e.nextpos(1)
#'a' is kept stable while other points move around a. This is to keep the end shape look better

#prints out the final state after the simulation
print(Point.prettyfier(a.pos), "a")
print(Point.prettyfier(b.pos), "b")
print(Point.prettyfier(c.pos), "c")
#print(prettyfier(d.pos), "d")
#print(prettyfier(e.pos), "e")




