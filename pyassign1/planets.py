"""planets.py: simulation of how planets circle.

__author__ = "Bai Yuchen"
__pkuid__  = "1800011798"
__email__  = "1800011798@pku.edu.cn"
"""

import turtle
import math

sun=turtle.Pen()
mercury=turtle.Pen()
venus=turtle.Pen()
earth=turtle.Pen()
mars=turtle.Pen()
jupiter=turtle.Pen()
saturn=turtle.Pen()
anglea=0
angleb=0
anglec=0
angled=0
anglee=0
anglef=0

sun.up()
sun.shape('circle')
sun.color('purple')
sun.goto(100,0)

def start(a,c,who,whatcolor):
    who.shape('circle')
    who.speed(0)
    who.color(whatcolor)
    b=(a**2-c**2)**(1/2)
    who.up()
    who.goto(a+100-c,0)
    
def step(a,c,who,speed,angle):
    who.down()
    b=(a**2-c**2)**(1/2)
    angle=angle+speed
    x=a*math.cos(math.radians(angle))+100-c
    y=b*math.sin(math.radians(angle))
    who.goto(x,y)
    
start(50,10,mercury,'red')
start(70,20,venus,'blue')
start(110,40,earth,'black')
start(140,60,mars,'green')
start(190,90,jupiter,'yellow')
start(240,130,saturn,'orange')

for i in range(10000):
    step(50,10,mercury,16,anglea)
    step(70,20,venus,13,angleb)
    step(110,40,earth,10,anglec)
    step(140,60,mars,7,angled)
    step(190,90,jupiter,4,anglee)
    step(240,130,saturn,1,anglef)
    anglea=anglea+16
    angleb=angleb+13
    anglec=anglec+10
    angled=angled+7
    anglee=anglee+4
    anglef=anglef+1

if __name__ == '__main__':
    main()    