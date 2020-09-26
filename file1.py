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

############
# MISC
############

#wrzuci się do klasy później - musimy to omówić
def showImage(picture):
    if picture.ndim==2: plt.imshow(newPic, cmap='gray')
    else: plt.imshow(newPic, cmap=None) #dzięki temu nie musisz wybierać między cmap gray a None

############
#
############

def grayScaleNTSC(picture):
    output=np.zeros((picture.shape[0],picture.shape[1]))    # czy z tego funkcje?
    for x in range(0,picture.shape[0]):
        for y in range(0,picture.shape[1]):
            output[x,y]=0.299*picture[x,y,0]+0.587*picture[x,y,1]+0.114*picture[x,y,2]
    return output

def grayScaleHDTV(picture):
    output=np.zeros((picture.shape[0],picture.shape[1]))     # czy z tego funkcje?
    for x in range(0,picture.shape[0]):
        for y in range(0,picture.shape[1]):
            output[x,y]=0.2126*picture[x,y,0]+0.7152*picture[x,y,1]+0.0722*picture[x,y,2]
    return output


def grayScaleHDR(picture):
    output=np.zeros((picture.shape[0],picture.shape[1]))    # czy z tego funkcje?
    for x in range(0,picture.shape[0]):
        for y in range(0,picture.shape[1]):
            output[x,y]=0.2627*picture[x,y,0]+0.6780*picture[x,y,1]+0.0593*picture[x,y,2]
    return output

def negativeFilter(picture):
    output=0
    if picture.ndim==2: output=255-picture[:,:]
    else: output=255-picture[:,:,:]
    return output
############
# TESTS?
############

newPic=negativeFilter(img.imread("laura.tif"))
showImage(newPic)
plt.show()