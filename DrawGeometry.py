#Minecraft Java 1.12.x
#McFunction
import math,os
as_module = False

def straightline(x1,y1,z1,x2,y2,z2,absmode=True,block='stone',player='@p'):
    s = (math.floor(x1),math.floor(y1),math.floor(z1))
    e = (math.floor(x2),math.floor(y2),math.floor(z2))
    d = math.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
    commands = []
    if (s[0]==e[0] and s[1]==e[1]) or (s[0]==e[0] and s[2]==e[2]) or (s[1]==e[1] and s[2]==e[2]):
        if absmode:
            commands.append(f'fill {s[0]} {s[1]} {s[2]} {e[0]} {e[1]} {e[2]} {block}')
        else:
            commands.append(f'execute {player} ~ ~ ~ fill ~{s[0]} ~{s[1]} ~{s[2]} ~{e[0]} ~{e[1]} ~{e[2]} {block}')
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
            if absmode:
                commands.append(f'setblock {coor[0]} {coor[1]} {coor[2]} {block}')
            else:
                commands.append(f'execute {player} ~{coor[0]} ~{coor[1]} ~{coor[2]} setblock ~ ~ ~ {block}')
        print_('33.3%',end='')
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
            if absmode:
                commands.append(f'setblock {coor[0]} {coor[1]} {coor[2]} {block}')
            else:
                commands.append(f'execute {player} ~{coor[0]} ~{coor[1]} ~{coor[2]} setblock ~ ~ ~ {block}')
        print_('\r66.6%',end='')
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
            if absmode:
                commands.append(f'setblock {coor[0]} {coor[1]} {coor[2]} {block}')
            else:
                commands.append(f'execute {player} ~{coor[0]} ~{coor[1]} ~{coor[2]} setblock ~ ~ ~ {block}')
        print_('\r100.0%')
    print_('StraightLine Done.')
    head = []
    return head+list(set(commands))

def ball(a,b,c,r,absmode=True,block='stone',player='@p'):
    a,b,c,r = (math.floor(a),math.floor(b),math.floor(c),math.floor(r))
    commands = []
    counter = 0
    for x in range(0-r,0+r+1):
        for y in range(0-r,0+r+1):
            try:
                delta = r**2-x**2-y**2
                z = math.sqrt(delta)
            except:
                continue
            else:
                if absmode:
                    commands.append(f'setblock {int(x+a)} {int(y+b)} {int(z+c)} {block}')
                    commands.append(f'setblock {int(0-x+a)} {int(0-y+b)} {int(0-z+c)} {block}')
                else:
                    commands.append(f'execute {player} ~{int(x+a)} ~{int(y+b)} ~{int(z+c)} setblock ~ ~ ~ {block}')
                    commands.append(f'execute {player} ~{int(0-x+a)} ~{int(0-y+b)} ~{int(0-z+c)} setblock ~ ~ ~ {block}')
            finally:
                counter += 1
                print_('\rLoop%s'%(counter),end='')
    print_('\nLoopFinished.')
    counter = 0
    for x in range(0-r,r+1):
        for z in range(0-r,r+1):
            try:
                delta = r**2-x**2-z**2
                y = math.sqrt(delta)
            except:
                continue
            else:
                if absmode:
                    commands.append(f'setblock {int(x+a)} {int(y+b)} {int(z+c)} {block}')
                    commands.append(f'setblock {int(0-x+a)} {int(0-y+b)} {int(0-z+c)} {block}')
                else:
                    commands.append(f'execute {player} ~{int(x+a)} ~{int(y+b)} ~{int(z+c)} setblock ~ ~ ~ {block}')
                    commands.append(f'execute {player} ~{int(0-x+a)} ~{int(0-y+b)} ~{int(0-z+c)} setblock ~ ~ ~ {block}')
            finally:
                counter += 1
                print_('\rLoop%s'%(counter),end='')
    counter = 0
    print_('\nLoopFinished.')
    for y in range(0-r,r+1):
        for z in range(0-r,r+1):
            try:
                delta = r**2-y**2-z**2
                x = math.sqrt(delta)
            except:
                continue
            else:
                if absmode:
                    commands.append(f'setblock {int(x+a)} {int(y+b)} {int(z+c)} {block}')
                    commands.append(f'setblock {int(0-x+a)} {int(0-y+b)} {int(0-z+c)} {block}')
                else:
                    commands.append(f'execute {player} ~{int(x+a)} ~{int(y+b)} ~{int(z+c)} setblock ~ ~ ~ {block}')
                    commands.append(f'execute {player} ~{int(0-x+a)} ~{int(0-y+b)} ~{int(0-z+c)} setblock ~ ~ ~ {block}')
            finally:
                counter += 1
                print_('\rLoop%s'%(counter),end='')
    counter = 0
    print_('\nLoopFinished.\nBall Done.')
    head = [
        f'#Ball({a},{b},{c})~{r},with {block},by {player}',
        ]
    return head+list(set(commands))

def circle(a,b,c,r,towards='x',absmode=True,block='stone',player='@p'):#towards = x / y / z
    commands = []
    if towards == 'x':
        for y in range(0-r,r+1):
            z = math.sqrt(r**2-(y)**2)
            if absmode:
                commands.append(f'setblock {int(a)} {int(y+b)} {int(z+c)} {block}')
                commands.append(f'setblock {int(a)} {int(0-y+b)} {int(0-z+c)} {block}')
            else:
                commands.append(f'execute {player} ~{int(a)} ~{int(y+b)} ~{int(z+c)} setblock ~ ~ ~ {block}')
                commands.append(f'execute {player} ~{int(a)} ~{int(0-y+b)} ~{int(0-z+c)} setblock ~ ~ ~ {block}')
        for z in range(0-r,r+1):
            y = math.sqrt(r**2-(z)**2)
            if absmode:
                commands.append(f'setblock {int(a)} {int(y+b)} {int(z+c)} {block}')
                commands.append(f'setblock {int(a)} {int(0-y+b)} {int(0-z+c)} {block}')
            else:
                commands.append(f'execute {player} ~{int(a)} ~{int(y+b)} ~{int(z+c)} setblock ~ ~ ~ {block}')
                commands.append(f'execute {player} ~{int(a)} ~{int(0-y+b)} ~{int(0-z+c)} setblock ~ ~ ~ {block}')
    elif towards == 'y':
        for x in range(0-r,r+1):
            z = math.sqrt(r**2-(x)**2)
            if absmode:
                commands.append(f'setblock {int(x+a)} {int(b)} {int(z+c)} {block}')
                commands.append(f'setblock {int(0-x+a)} {int(b)} {int(0-z+c)} {block}')
            else:
                commands.append(f'execute {player} ~{int(x+a)} ~{int(b)} ~{int(z+c)} setblock ~ ~ ~ {block}')
                commands.append(f'execute {player} ~{int(0-x+a)} ~{int(b)} ~{int(0-z+c)} setblock ~ ~ ~ {block}')
        for z in range(0-r,r+1):
            x = math.sqrt(r**2-(z)**2)
            if absmode:
                commands.append(f'setblock {int(x+a)} {int(b)} {int(z+c)} {block}')
                commands.append(f'setblock {int(0-x+a)} {int(b)} {int(0-z+c)} {block}')
            else:
                commands.append(f'execute {player} ~{int(x+a)} ~{int(b)} ~{int(z+c)} setblock ~ ~ ~ {block}')
                commands.append(f'execute {player} ~{int(0-x+a)} ~{int(b)} ~{int(0-z+c)} setblock ~ ~ ~ {block}')
    elif towards == 'z':
        for x in range(0-r,r+1):
            y = math.sqrt(r**2-(x)**2)
            if absmode:
                commands.append(f'setblock {int(x+a)} {int(y+b)} {int(c)} {block}')
                commands.append(f'setblock {int(0-x+a)} {int(0-y+b)} {int(c)} {block}')
            else:
                commands.append(f'execute {player} ~{int(x+a)} ~{int(y+b)} ~{int(c)} setblock ~ ~ ~ {block}')
                commands.append(f'execute {player} ~{int(0-x+a)} ~{int(0-y+b)} ~{int(c)} setblock ~ ~ ~ {block}')
        for y in range(0-r,r+1):
            x = math.sqrt(r**2-(y)**2)
            if absmode:
                commands.append(f'setblock {int(x+a)} {int(y+b)} {int(c)} {block}')
                commands.append(f'setblock {int(0-x+a)} {int(0-y+b)} {int(c)} {block}')
            else:
                commands.append(f'execute {player} ~{int(x+a)} ~{int(y+b)} ~{int(c)} setblock ~ ~ ~ {block}')
                commands.append(f'execute {player} ~{int(0-x+a)} ~{int(0-y+b)} ~{int(c)} setblock ~ ~ ~ {block}')
    print_('Circle Done.')
    head = []
    return head+list(set(commands))

def flat(coor1,coor2,coor3,block='stone',absmode=True,player='@p'):#不成熟
    x1,y1,z1 = coor1
    x2,y2,z2 = coor2
    x3,y3,z3 = coor3
    a = (y2-y1)*(z3-z1)-(y3-y1)*(z2-z1)
    b = (z2-z1)*(x3-x1)-(z3-z1)*(x2-x1)
    c = (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
    d = 0-a*x1-b*y1-c*z1
    commands = []
    #ax+by+cz+d=0
    for x in range(int(min(x1,x2,x3)),int(max(x1,x2,x3))):
        for y in range(int(min(y1,y2,y3)),int(max(y1,y2,y3))):
            if c == 0:
                z = (0-d-a*x-b*y)/1
            else:
                z = (0-d-a*x-b*y)/c
            if absmode:
                commands.append(f'setblock {int(x)} {int(y)} {int(z)} {block}')
            else:
                commands.append(f'execute {player} {int(x)} {int(y)} {int(z)} setblock ~ ~ ~ ~ ~ ~ {block}')
    for y in range(int(min(y1,y2,y3)),int(max(y1,y2,y3))):
        for z in range(int(min(z1,z2,z3)),int(max(z1,z2,z3))):
            if a == 0:
                x = (0-d-c*z-b*y)/1
            else:
                x = (0-d-c*z-b*y)/a
            if absmode:
                commands.append(f'setblock {int(x)} {int(y)} {int(z)} {block}')
            else:
                commands.append(f'execute {player} {int(x)} {int(y)} {int(z)} setblock ~ ~ ~ ~ ~ ~ {block}')
    for x in range(int(min(x1,x2,x3)),int(max(x1,x2,x3))):
        for z in range(int(min(z1,z2,z3)),int(max(z1,z2,z3))):
            if b == 0:
                y = (0-d-a*x-c*z)/1
            else:
                y = (0-d-a*x-c*z)/b
            if absmode:
                commands.append(f'setblock {int(x)} {int(y)} {int(z)} {block}')
            else:
                commands.append(f'execute {player} {int(x)} {int(y)} {int(z)} setblock ~ ~ ~ ~ ~ ~ {block}')
    print_('Flat Done.')
    return list(set(commands))

def print_(content,end='\n'):
    if not as_module:
        print(content,end=end)
            
def save(filename,commands,path='./GeometryMcfunctions/'):#不需要文件名后缀
    if not os.path.exists(path):
        os.mkdir(path)
    if not path.endswith('\\') and not path.endswith('/'):
        path = path+'/'
    print_('Saving...')
    f = open(path+'%s.mcfunction'%filename,'w+',encoding='utf-8')
    counter = 0
    counter_ = 1
    for command in commands:
        if counter > 65535:
            f.close()
            f = open(path+'%s_%s.mcfunction'%(filename,counter_),'w+',encoding='utf-8')
            counter += 1
            counter = 0
            print_('\nLoop Finished.')
        f.write(command+'\n')
        counter += 1
        print_('\rLoop%s'%counter,end='')
    f.close()
    print_('\nSave Completed.')

if __name__ == '__main__':
    save('test',flat((0,5,0),(10,10,10),(15,5,0)))
else:
    as_module = True
