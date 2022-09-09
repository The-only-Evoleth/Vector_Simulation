from utils import *

a = Point(conv_to_unitv(np.array([[0,0,1]])))
b = Point(conv_to_unitv(np.array([[-1,1,2]])))
c = Point(conv_to_unitv(np.array([[3,-2,0]])))
d = Point(conv_to_unitv(np.array([[-1,-2,-9]])))
e = Point(conv_to_unitv(np.array([[1,1,0]])))


for i in range(100): #here range depicts how many times the sim will run. More points may take more steps to reach stable state
    b.pos = newpos(b,1)
    c.pos = newpos(c,1)
    d.pos = newpos(d,1)
    e.pos = newpos(e,1)
#'a' is kept stable while other points move around a. This is to keep the end shape look better

#prints out the final state after the simulation
print(prettyfier(a.pos), "a")
print(prettyfier(b.pos), "b")
print(prettyfier(c.pos), "c")
print(prettyfier(d.pos), "d")
print(prettyfier(e.pos), "e")




