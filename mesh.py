import os
from geometry import straightline,flat
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

def ymaxmin(points):
    ys = []
    for tmp in points:
        ys.append(tmp[1])
    ymax = max(ys)
    ymin = min(ys)
    return ymax,ymin

def mesh(points,faces=None,a=0,c=0,height=world_max_height,show_progress=True):
    res = []
    ymax,ymin = ymaxmin(points)
    print('Ymax:',ymax)
    print('Ymin:',ymin)
    t = (ymax-ymin)/height #计算比例
    print('Proportion:',t)
    for i in range(len(points)):
        points[i][1] /= t #等比缩放
        points[i][0] /= t
        points[i][2] /= t
    ymin = ymaxmin(points)[1]
    for i in range(len(points)):
        points[i][1] -= ymin #y坐标归正
    for tmp in points:
        res.append((int(tmp[0])+a,int(tmp[1]),int(tmp[2])+c))
    if show_progress:
        print('Points Done.')
    if not faces == None:
        counter = 0
        length = len(faces)
        for i in range(len(faces)):
            for o in range(len(faces[i])):
                faces[i][o] = points[faces[i][o]] #读取索引
        for tmp in faces:
            x1,y1,z1 = tmp[0] #读取点坐标
            x2,y2,z2 = tmp[1]
            x3,y3,z3 = tmp[2]
            if len(tmp) == 4:
                x4,y4,z4 = tmp[3]
            res += flat((x1+a,y1,z1+c),(x2+a,y2,z2+c),(x3+a,y3,z3+c))
            if len(tmp) == 4:
                res += flat((x1+a,y1,z1+c),(x3+a,y3,z3+c),(x4+a,y4,z4+c))
                res += flat((x2+a,y2,z2+c),(x3+a,y3,z3+c),(x4+a,y4,z4+c))
                res += flat((x1+a,y1,z1+c),(x2+a,y2,z2+c),(x4+a,y4,z4+c))
            counter += 1
            if show_progress:
                print('\r%.2f%%'%(counter/length*100),end='')
        if show_progress:
            print('\rFaces Done.')
    res = list(set(res)) #去重
    return res
