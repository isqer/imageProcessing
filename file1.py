#nazwie się później
#INFORMACJE

############
#IMPORT
############

import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np

############
#
############

#wrzuci się do klasy później - musimy to omówić

def grayscaleNTSC(picture):
    output=np.zeros((picture.shape[0],picture.shape[1]))
    for x in range(0,picture.shape[0]):
        for y in range(0,picture.shape[1]):
            output[x,y]=0.299*picture[x,y,0]+0.587*picture[x,y,1]+0.114*picture[x,y,2]
    plt.imshow(output, cmap='gray')
    plt.show()

def grayscaleHDTV(picture):
    output=np.zeros((picture.shape[0],picture.shape[1]))
    for x in range(0,picture.shape[0]):
        for y in range(0,picture.shape[1]):
            output[x,y]=0.2126*picture[x,y,0]+0.7152*picture[x,y,1]+0.0722*picture[x,y,2]
    plt.imshow(output, cmap='gray')
    plt.show()

def grayscaleHDR(picture):
    output=np.zeros((picture.shape[0],picture.shape[1]))
    for x in range(0,picture.shape[0]):
        for y in range(0,picture.shape[1]):
            output[x,y]=0.2627*picture[x,y,0]+0.6780*picture[x,y,1]+0.0593*picture[x,y,2]
    plt.imshow(output, cmap='gray')
    plt.show()

grayscaleNTSC(img.imread("laura.tif"))