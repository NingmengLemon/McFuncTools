import os,math
from PIL import Image
#Minecraft 1.12.2 Only.

woolcolor = [
    (241, 241, 246),
    (234, 115, 22),
    (181, 64, 174),
    (53, 168, 211),
    (243, 203, 51),
    (104, 174, 24),
    (229, 125, 160),
    (61, 66, 71),
    (137, 138, 134),
    (20, 137, 145),
    (120, 40, 170),
    (56, 60, 161),
    (107, 67, 38),
    (87, 113, 22),
    (152, 36, 32),
    (12, 14, 19)
    ]
def convertRGB(r,g,b):
    tmp = []
    for example in woolcolor:
        tmp.append(colorDistance((r,g,b),example))
    tmp_ = min(tmp)
    index = tmp.index(tmp_)
    return index,woolcolor[index]

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

def main(inputfile,outfilename,path='./McfunctionPictures/',maxwh=600,absmode=True,coor=(0,5,0),player='@p'):
    img = resize(Image.open(inputfile).convert('RGB'),maxwh)
    img_array = img.load()
    img_size = img.size
    counter = 0
    counter_ = 1
    if not os.path.exists(path):
        os.mkdir(path)
    f = open(path+outfilename+'.mcfunction','w+',encoding='utf-8')
    for x in range(0,img_size[0]):
        for y in range(0,img_size[1]):
            if counter > 65535:
                counter = 0
                print('\nLoopFinished.')
                f.close()
                f = open(path+outfilename+'_%s.mcfunction'%counter_,'w+',encoding='utf-8')
                counter_ += 1
            rgb = img_array[x,y]
            wool = convertRGB(rgb[0],rgb[1],rgb[2])[0]
            if absmode:
                f.write(f'fill {coor[0]+x} {coor[1]} {coor[2]+y} {coor[0]+x} {coor[1]} {coor[2]+y} wool {wool}\n')
            else:
                f.write(f'execute {player} ~{coor[0]+x} ~{coor[1]} ~{coor[2]+y} fill ~ ~ ~ ~ ~ ~ wool {wool}\n')
            counter += 1
            print(f'\rLoop{counter}',end='')
    print('\nDone.')

if __name__ == '__main__':
    main(input('File:'),input('OutFilename:'))
