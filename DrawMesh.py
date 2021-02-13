import os
from DrawGeometry import straightline,flat
#For OBJ File Only.
world_max_height = 255


def readData(path):
    with open(path) as file:
        lines = file.read().split('\n')
    #Point
    points = []
    for line in lines:
        if not line:
            continue
        strs = line.split(" ")
        if strs[0] == "v":
            points.append([float(strs[1]), float(strs[2]), float(strs[3])])
        else:
            continue
    print(len(points),'Points')
    #Face
    faces = []
    for line in lines:
        if not line:
            continue
        strs = line.split(' ')
        if strs[0] != 'f':
            continue
        strs = strs[1:]
        t = []
        for s in strs:
            t.append(int(s.split('/')[0])-1)
        faces.append(t)
    print(len(faces),'Faces')
                
    return points,faces

def mesh(points,faces=None,a=0,c=0,height=world_max_height,block='stone'):
    commands = []
    xs = ys = zs = []
    for tmp in points:
        xs.append(tmp[0])
        ys.append(tmp[1])
        zs.append(tmp[2])
    xmax = max(xs)
    ymax = max(ys)
    zmax = max(zs)
    xmin = min(xs)
    ymin = min(ys)
    zmin = min(zs)
    print('Ymax:',ymax)
    print('Ymin:',ymin)
    t = (ymax-ymin)/height #计算比例
    print('Proportion:',t)
    for i in range(len(points)):
        points[i][1] -= ymin #y坐标归正
        points[i][1] /= t #等比缩放
        points[i][0] /= t
        points[i][2] /= t
    for tmp in points:
        commands.append(f'setblock {int(tmp[0])+a} {int(tmp[1])} {int(tmp[2])+c} {block}')
    print('Points Done.')
    if not faces == None:
        for i in range(len(faces)):
            for o in range(len(faces[i])):
                faces[i][o] = points[faces[i][o]] #读取索引
        for tmp in faces:
            x1,y1,z1 = tmp[0] #读取点坐标
            x2,y2,z2 = tmp[1]
            x3,y3,z3 = tmp[2]
            if len(tmp) == 4:
                x4,y4,z4 = tmp[3]
            commands += straightline(x1+a,y1,z1+c,x2+a,y2,z2+c) #连接点
            commands += straightline(x2+a,y2,z2+c,x3+a,y3,z3+c)
            commands += straightline(x1+a,y1,z1+c,x3+a,y3,z3+c)
            #commands += flat(tmp[0],tmp[1],tmp[2])
            if len(tmp) == 4:
                commands += straightline(x1+a,y1,z1+c,x4+a,y4,z4+c)
                commands += straightline(x2+a,y2,z2+c,x4+a,y4,z4+c)
                commands += straightline(x3+a,y3,z3+c,x4+a,y4,z4+c)
                #commands += flat(tmp[0],tmp[2],tmp[3])
                #commands += flat(tmp[1],tmp[2],tmp[3])
                #commands += flat(tmp[0],tmp[1],tmp[3])
        print('Faces Done.')
    commands = list(set(commands)) #去重
    return commands

def save(filename,commands,path='./MeshMcfunctions/'): #不需要文件名后缀
    if not os.path.exists(path):
        os.mkdir(path)
    if not path.endswith('\\') and not path.endswith('/'):
        path = path+'/'
    print('Saving...')
    f = open(path+'%s.mcfunction'%filename,'w+',encoding='utf-8')
    counter = 0
    counter_ = 1
    for command in commands:
        if counter > 65535:
            f.close()
            f = open(path+'%s_%s.mcfunction'%(filename,counter_),'w+',encoding='utf-8')
            counter_ += 1
            counter = 0
            print('\nLoop Finished.')
        f.write(command+'\n')
        counter += 1
        print('\rLoop%s'%counter,end='')
    f.close()
    print('\nSave Completed.')
        
if __name__ == '__main__':
    d = readData(input('File:'))
    save('test',mesh(d[0],d[1]))
