#Minecraft Java 1.12.x
#McFunction
import math,os

def _getPointsOnStraightLine(x1,y1,z1,x2,y2,z2):
    s = (math.floor(x1),math.floor(y1),math.floor(z1))
    e = (math.floor(x2),math.floor(y2),math.floor(z2))
    d = math.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
    points = []
    if s[0]==e[0] and s[1]==e[1] and s[2]==e[2]:
        points.append((s[0],s[1],s[2]))
    elif (s[0]==e[0] and s[1]==e[1]):
        for t in range(s[2],e[2]):
            points.append((s[0],s[1],t))
    elif (s[0]==e[0] and s[2]==e[2]):
        for t in range(s[1],e[1]):
            points.append((s[0],t,s[2]))
    elif (s[1]==e[1] and s[2]==e[2]):
        for t in range(s[0],e[0]):
            points.append((t,s[1],s[2]))
    else:
        if s[0] > e[0]:
            r = range(e[0],s[0]+1)
        else:
            r = range(s[0],e[0]+1)
        for x in r:
            try:
                coor = (x,math.floor((x-s[0])*(e[1]-s[1])/(e[0]-s[0])+s[1]),math.floor((x-s[0])*(e[2]-s[2])/(e[0]-s[0])+s[2]))
            except ZeroDivisionError:
                coor = (x,math.floor((x-s[0])*(e[1]-s[1])+s[1]),math.floor((x-s[0])*(e[2]-s[2])+s[2]))
            except:
                continue
            points.append(coor)
        if s[1] > e[1]:
            r = range(e[1],s[1]+1)
        else:
            r = range(s[1],e[1]+1)
        for y in r:
            try:
                coor = (math.floor((y-s[1])*(e[0]-s[0])/(e[1]-s[1])+s[0]),y,math.floor((y-s[1])*(e[2]-s[2])/(e[1]-s[1])+s[2]))
            except ZeroDivisionError:
                coor = (math.floor((y-s[1])*(e[0]-s[0])+s[0]),y,math.floor((y-s[1])*(e[2]-s[2])+s[2]))
            except:
                continue
            points.append(coor)
        if s[2] > e[2]:
            r = range(e[2],s[2]+1)
        else:
            r = range(s[2],e[2]+1)
        for z in r:
            try:
                coor = (math.floor((z-s[2])*(e[0]-s[0])/(e[2]-s[2])+s[0]),math.floor((z-s[2])*(e[1]-s[1])/(e[2]-s[2])+s[1]),z)
            except ZeroDivisionError:
                coor = (math.floor((z-s[2])*(e[0]-s[0])+s[0]),math.floor((z-s[2])*(e[1]-s[1])+s[1]),z)
            except:
                continue
            points.append(coor)
    return list(set(points))

def straightline(x1,y1,z1,x2,y2,z2):
    return _getPointsOnStraightLine(x1,y1,z1,x2,y2,z2)

def ball(a,b,c,r):
    a,b,c,r = (math.floor(a),math.floor(b),math.floor(c),math.floor(r))
    points = []
    counter = 0
    for x in range(0-r,0+r+1):
        for y in range(0-r,0+r+1):
            try:
                delta = r**2-x**2-y**2
                z = math.sqrt(delta)
            except:
                continue
            else:
                points.append((int(x+a),int(y+b),int(z+c)))
                points.append((int(0-x+a),int(0-y+b),int(0-z+c)))
            finally:
                counter += 1
    counter = 0
    for x in range(0-r,r+1):
        for z in range(0-r,r+1):
            try:
                delta = r**2-x**2-z**2
                y = math.sqrt(delta)
            except:
                continue
            else:
                points.append((int(x+a),int(y+b),int(z+c)))
                points.append((int(0-x+a),int(0-y+b),int(0-z+c)))
            finally:
                counter += 1
    counter = 0
    for y in range(0-r,r+1):
        for z in range(0-r,r+1):
            try:
                delta = r**2-y**2-z**2
                x = math.sqrt(delta)
            except:
                continue
            else:
                points.append((int(x+a),int(y+b),int(z+c)))
                points.append((int(0-x+a),int(0-y+b),int(0-z+c)))
            finally:
                counter += 1
    return list(set(points))

def circle(a,b,c,r,towards='x'):#towards = x / y / z
    points = []
    if towards == 'x':
        for y in range(0-r,r+1):
            z = math.sqrt(r**2-(y)**2)
            points.append((int(a),int(y+b),int(z+c)))
            points.append((int(a),int(0-y+b),int(0-z+c)))
        for z in range(0-r,r+1):
            y = math.sqrt(r**2-(z)**2)
            points.append((int(a),int(y+b),int(z+c)))
            points.append((int(a),int(0-y+b),int(0-z+c)))
    elif towards == 'y':
        for x in range(0-r,r+1):
            z = math.sqrt(r**2-(x)**2)
            points.append((int(x+a),int(b),int(z+c)))
            points.append((int(0-x+a),int(b),int(0-z+c)))
        for z in range(0-r,r+1):
            x = math.sqrt(r**2-(z)**2)
            points.append((int(x+a),int(b),int(z+c)))
            points.append((int(0-x+a),int(b),int(0-z+c)))
    elif towards == 'z':
        for x in range(0-r,r+1):
            y = math.sqrt(r**2-(x)**2)
            points.append((int(x+a),int(y+b),int(c)))
            points.append(int(0-x+a),int(0-y+b),int(c))
        for y in range(0-r,r+1):
            x = math.sqrt(r**2-(y)**2)
            points.append((int(x+a),int(y+b),int(c)))
            points.append(int(0-x+a),int(0-y+b),int(c))
    return list(set(points))

def flat(coor1,coor2,coor3):#不成熟
    x1,y1,z1 = coor1
    x2,y2,z2 = coor2
    x3,y3,z3 = coor3
    points = []
    line = _getPointsOnStraightLine(x1,y1,z1,x2,y2,z2)
    for coor in line:
        x,y,z = coor
        childp = _getPointsOnStraightLine(x,y,z,x3,y3,z3)
        points += childp
    line = _getPointsOnStraightLine(x1,y1,z1,x3,y3,z3)
    for coor in line:
        x,y,z = coor
        childp = _getPointsOnStraightLine(x,y,z,x2,y2,z2)
        points += childp
    line = _getPointsOnStraightLine(x2,y2,z2,x3,y3,z3)
    for coor in line:
        x,y,z = coor
        childp = _getPointsOnStraightLine(x,y,z,x1,y1,z1)
        points += childp
    return list(set(points))
