#!/usr/bin/python
v0=20
t=19
g=9.81
for t in range(1, 20):
    y=(v0*t)-(g*(t**2)/2)
    print "Pēc "+ str(t) +" sekundēm bumba būs "+str(y)+" metri virs zemes."

from numpy import linspace,array
x=linspace(0,1,19)   #massiivs
y=(v0*t)-(g*(x**2)/2)#massiivs

from matplotlib import pyplot as p
p.plot(x,y,color="#ff0000", label="super")
p.legend()
p.show()
