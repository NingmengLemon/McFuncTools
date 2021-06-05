import math,os
import img,geometry,mesh

def _union_points(pointset):
    pointset = list(set(pointset))
    xzdict = {}
    for p in pointset:
        if (p[0],p[2]) in xzdict.keys():
            xzdict[(p[0],p[2])] += [p[1]]
        else:
            xzdict[(p[0],p[2])] = [p[1]]
    xzs = xzdict.keys()
    for xz in xzs:
        ys = sorted(xzdict[xz])
        groups = []
        tmp = []
        for y in ys:
            if tmp == []:
                tmp += [y]
                continue
            if y-1 == tmp[-1]:
                tmp += [y]
            else:
                groups += [tmp]
                tmp = [y]
        if tmp:
            groups += [tmp]
        tmp = []
        for group in groups:
            tmp += [(max(group),min(group))]
        xzdict[xz] = tmp
    return xzdict

def _make_commands(source,block,data_type=dict,player='@p',absmode=True):
    commands = []
    if data_type == dict:
        for key in source.keys():
            x,z = key
            for item in source[key]:
                y1,y2 = item
                if absmode:
                    commands += [f'fill {x} {y1} {z} {x} {y2} {z} {block}']
                else:
                    commands += [f'execute {player} ~ ~ ~ fill {x} {y1} {z} {x} {y2} {z} {block}']
    else:
        source = list(set(source))
        for coor in source:
            x,y,z = coor
            if absmode:
                commands += [f'setblock {x} {y} {z} {block}']
            else:
                commands += [f'execute {player} ~ ~ ~ setblock {x} {y} {z} {block}']
    return commands

def save(filename,commands,path='./Mcfunctions/'):#不需要文件名后缀
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
    i = input('(1.Img)(2.Mesh):')
    if i == '1':
        f = input('Img File:')
        c = img.main(f)
        save(input('Save File:'),c)
    elif i == '2':
        f = input('Obj File:')
        p,f = mesh.readData(f)
        c = _make_commands(_union_points(mesh.mesh(p,f)),'concrete')
        save(input('Save File:'),c)
