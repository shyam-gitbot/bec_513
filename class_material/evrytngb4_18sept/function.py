import math

def areaofsquare(side):
    return side**2

def areaofcircle(r):
    return math.pi*r*r

def areaofrectangle(l,w):
    return l*w

def areaoftriangle(b,h):
    return 0.5*b*h

def areaofcirclewithr(r=5):
    a = math.pi*r*r
    return "\t".join(map(str,[r,a]))

