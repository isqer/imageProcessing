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
# FILTERS
############
class Filters:
    def __init__(self):
        pass        #jakis init musi byc

    def grayScaleNTSC(self, picture):   #zawsze musisz dac self
        output=np.zeros((picture.shape[0],picture.shape[1]))    # czy z tego funkcje?
        for x in range(0,picture.shape[0]):
            for y in range(0,picture.shape[1]):
                output[x,y]=0.299*picture[x,y,0]+0.587*picture[x,y,1]+0.114*picture[x,y,2]
        return output

    def grayScaleHDTV(self, picture):
        output=np.zeros((picture.shape[0],picture.shape[1]))     # czy z tego funkcje?
        for x in range(0,picture.shape[0]):
            for y in range(0,picture.shape[1]):
                output[x,y]=0.2126*picture[x,y,0]+0.7152*picture[x,y,1]+0.0722*picture[x,y,2]
        return output


    def grayScaleHDR(self, picture):
        output=np.zeros((picture.shape[0],picture.shape[1]))    # czy z tego funkcje?
        for x in range(0,picture.shape[0]):
            for y in range(0,picture.shape[1]):
                output[x,y]=0.2627*picture[x,y,0]+0.6780*picture[x,y,1]+0.0593*picture[x,y,2]
        return output

    def negativeFilter(self, picture):
        output=0
        if picture.ndim==2: output=255-picture[:,:]
        else: output=255-picture[:,:,:]
        return output


############
# OPERATIONS
############

class Operations:
    def __init__(self):
        pass

    def crop(self, picture, x1, y1, x2, y2):
        if picture.ndim==2:
            return picture[x1:x2,y1:y2]
        else:
            return picture[x1:x2,y1:y2,:]

        

############
# TESTS?
############


flt = Filters()
ops = Operations()
newPic=ops.crop(flt.negativeFilter(flt.grayScaleHDR(img.imread("laura.tif"))),100,100,500,250)
showImage(newPic)
plt.show()