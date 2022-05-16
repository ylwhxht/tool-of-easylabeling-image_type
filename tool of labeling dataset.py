%matplotlib inline
import os
from skimage import io
import cv2 
import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np
#文件夹源目录
path ='D:\\Study\\object detection\\waymo_jpg_part1'
txtpath='C:\\Users\\ylwhxht\\Desktop\\waymo.txt'
plt.figure()

#traverse all folders under the path
def get_filelist(dir):
    Filelist = []
    Filename = []
    for home, dirs, files in os.walk(path):
        for filename in files:
            Filelist.append(os.path.join(home, filename))
            break;
        Filename.append(dirs)
    #get the FileList and foldername
    return Filelist, Filename[0]
 
#显示图片，每个序列图像显示一帧
def showpic(file):
        f = mpimg.imread(file)
    im = cv2.imread(file, 1)	# load image as bgr
    im2 = im[:, :, :: -1] 	# transform image to rgb
    plt.imshow(im2)
    plt.show()

#write down the result in target txt
def save(label):
    #txt地址
    with open(txtpath, mode='a') as filename:
        filename.write(label)
        filename.write('\n') # 换行
    

if __name__ =="__main__":
    #0 小雨 1 大雨 2 大雾  3 不标记 default  停止
    Filelist, Filename = get_filelist(dir)
    label = ['light-rain', 'heavy-rain', 'fog']
    print("start at :")
    start= int(input())
    for i in  range (start, len(Filelist)) :
        print(Filename[i])
        print("1 小雨 2 大雨 3 大雾  4 不标记 default  停止")
        showpic(Filelist[i])
        a=int(input())
        if a>=5:
            print("stop at : " + str(i))
            break
        if a<=3:
            labels = str(Filename[i]) + '.tfrecord ' + str(label[a-1])
            save(labels)
    print("Congratulation！finished")
