from utils import *

a = Point(conv_to_unitv(np.array([[0,0,1]])))
b = Point(conv_to_unitv(np.array([[-1,1,2]])))
c = Point(conv_to_unitv(np.array([[3,-2,0]])))
d = Point(conv_to_unitv(np.array([[-1,-2,-9]])))
e = Point(conv_to_unitv(np.array([[1,1,0]])))


for i in range(1000):
    b.pos = newpos(b,1)
    c.pos = newpos(c,1)
    d.pos = newpos(d,1)
    e.pos = newpos(e,1)

print(prettyfier(a.pos), "a")
print(prettyfier(b.pos), "b")
print(prettyfier(c.pos), "c")
print(prettyfier(d.pos), "d")
print(prettyfier(e.pos), "e")




