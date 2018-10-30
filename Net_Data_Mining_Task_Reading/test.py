import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import sys
from scipy import misc
import scipy
sys.path.append(r'D:\Algorithms\Net_Data_Mining_Task_Reading\NMF')
import NMF


def Jpg2BlackWrite(img):
    """
        turn jpg to black-or write image
    """
    width = len(img)
    height = len(img[0])
    answer = [[0 for j in range(height)] for i in range(width)]
    print width,height
    fazhi = 25
    for x in range(width):
        for y in range(height):
            if (img[x][y][0] < fazhi) | (img[x][y][1] < fazhi) | (img[x][y][2] < fazhi):
                answer[x][y] = 0
            else:
                answer[x][y] = 255
    return answer


def main():
    haha = misc.imread(r'Net_Data_Mining_Task_Reading\image\ucas.jpg')
    
    print haha.shape
    #haha = [[haha[i][j] for j in range(len(haha[0]))] for i in range(len(haha))]
    img1 = haha[:,:,0]
    print img1.shape
    [V, H, dis] = NMF.NMF(haha, r = 5)
    
    
    plt.subplot(1,3,1)
    plt.gray()
    plt.imshow(img1)
    plt.subplot(1,3,2)
    plt.gray()
    plt.imshow(V)
    plt.subplot(1,3,3)
    plt.gray()
    plt.imshow(H)
    plt.show()

  



if __name__ == '__main__':
    main()
