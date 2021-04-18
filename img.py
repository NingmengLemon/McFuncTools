import os,math
from PIL import Image
#Minecraft 1.12.2 Only.

colors = {
    (206, 211, 212):'concrete 0',
    (221, 95, 0):'concrete 1',
    (168, 49, 158):'concrete 2',
    (35, 135, 197):'concrete 3',
    (239, 174, 22):'concrete 4',
    (93, 167, 24):'concrete 5',
    (211, 101, 142):'concrete 6',
    (54, 57, 61):'concrete 7',
    (125, 125, 115):'concrete 8',
    (21, 118, 134):'concrete 9',
    (99, 31, 154):'concrete 10',
    (45, 47, 142):'concrete 11',
    (96, 59, 33):'concrete 12',
    (72, 90, 36):'concrete 13',
    (141, 33, 33):'concrete 14',
    (8, 10, 15):'concrete 15'
    }
def convertRGB(r,g,b):
    tmp = []
    rgbs = list(colors.keys())
    for example in rgbs:
        tmp.append(colorDistance((r,g,b),example))
    tmp_ = min(tmp)
    index = tmp.index(tmp_)
    rgb = rgbs[index]
    block = colors[rgb]
    return block,rgb

def colorDistance(rgb_1,rgb_2):
     R_1,G_1,B_1 = rgb_1
     R_2,G_2,B_2 = rgb_2
     rmean = (R_1 +R_2 ) / 2
     R = R_1 - R_2
     G = G_1 - G_2
     B = B_1 - B_2
     return math.sqrt((2+rmean/256)*(R**2)+4*(G**2)+(2+(255-rmean)/256)*(B**2))

def RGBtoHSV(r,g,b):
    r /= 255
    g /= 255
    b /= 255
    cmax = max(r,g,b)
    cmin = min(r,g,b)
    delta = cmax - cmin
    #H
    if delta == 0:
        h = 0
    elif cmax == r:
        h = 60*((g-b)/delta+0)
    elif cmax == g:
        h = 60*((b-r)/delta+2)
    elif cmax == b:
        h = 60*((r-g)/delta+4)
    #S
    if cmax == 0:
        s = 0
    else:
        s = delta/cmax
    #V
    v = cmax
    return h,s,v

def resize(img,maxwh=200):
    size = img.size
    if size[0] > maxwh:
        t = maxwh/size[0]
        w = int(maxwh)
        h = int(size[1]*t)
        img = img.resize((w,h),Image.ANTIALIAS)
    if size[1] > maxwh:
        t = maxwh/size[1]
        w = int(size[0]*t)
        h = int(maxwh)
        img = img.resize((w,h),Image.ANTIALIAS)
    return img

def main(inputfile,maxwh=600,absmode=True,coor=(0,5,0),player='@p'):
    img = resize(Image.open(inputfile).convert('RGBA'),maxwh)
    img_array = img.load()
    img_size = img.size
    counter = 0
    counter_ = 1
    commands = []
    for x in range(0,img_size[0]):
        for y in range(0,img_size[1]):
            rgba = img_array[x,y]
            if rgba[3] < 5:
                if absmode:
                    commands.append(f'fill {coor[0]+x} {coor[1]} {coor[2]+y} {coor[0]+x} {coor[1]} {coor[2]+y} air')
                else:
                    commands.append(f'execute {player} ~{coor[0]+x} ~{coor[1]} ~{coor[2]+y} fill ~ ~ ~ ~ ~ ~ air')
            else:
                block = convertRGB(rgba[0],rgba[1],rgba[2])[0]
                if absmode:
                    commands.append(f'fill {coor[0]+x} {coor[1]} {coor[2]+y} {coor[0]+x} {coor[1]} {coor[2]+y} {block}')
                else:
                    commands.append(f'execute {player} ~{coor[0]+x} ~{coor[1]} ~{coor[2]+y} fill ~ ~ ~ ~ ~ ~ {block}')
            counter += 1
            if counter%100 == 0:
                print(f'\rLoop{counter}',end='')
    print('\nDone.')
    return commands

def _save(filename,commands,path='./McfunctionPictures/'):#不需要文件名后缀
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
        if counter%100 == 0:
            print('\rLoop%s'%counter,end='')
    f.close()
    print('\nSave Completed.')

if __name__ == '__main__':
    _save(input('OutFilename:'),main(input('File:'),maxwh=int(input('Max Height&Width:'))))
