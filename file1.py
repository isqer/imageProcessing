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
    if picture.ndim==2: plt.imshow(picture, cmap='gray')
    else: plt.imshow(picture, cmap=None) #dzięki temu nie musisz wybierać między cmap gray a None

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
    
    def flipImageHorizontally(self, picture):
        if picture.ndim==2: return picture[:,:0:-1]
        else: return picture[:,:0:-1,:]

    def flipImageVertical(self, picture):
        if picture.ndim==2: return picture[:0:-1,:]
        else: return picture[:0:-1,:,:]

    def rotateLeft(self,picture):
        if picture.ndim==2:
            result=picture[:,:]
            result=np.rot90(result)
            return result.astype("uint8")
        elif picture.ndim==3:
            result=np.zeros((picture.shape[0],picture.shape[1],picture.shape[2]))
            result[:,:,0]=self.rotateLeft(picture[:,:,0])
            result[:,:,1]=self.rotateLeft(picture[:,:,1])
            result[:,:,2]=self.rotateLeft(picture[:,:,2])
            return result.astype("uint8")

    def rotateRight(self,picture):
        return self.rotateLeft(self.rotateLeft(self.rotateLeft(picture)))   #HEHEHE




############
# SAVE/READ
############
class FileFormat:
    def saveAsBMP(self,numpyArr,outputName):
        array=list()
        padding=(numpyArr.shape[1]*3)%4
        for x in range(((numpyArr.shape[0])-1),-1,-1):
            for y in range(0,numpyArr.shape[1]):
                for z in range((numpyArr.shape[2]-1),-1,-1):
                    array.append(numpyArr[x,y,z])
                    
            #"""
            for x in range (0,padding): #padding ma wyrownywac do 4 bitow
                array.append(0)
            #"""

        #print(array)
        arraysize=len(array)
        #print(arraysize)
        filesize1=(arraysize+54)%256   #imgsize+54
        filesize2=((arraysize+54)>>8)%256
        filesize3=((arraysize+54)>>16)%256
        filesize4=((arraysize+54)>>24)%256
        imgwidth1=numpyArr.shape[1]%256
        imgwidth2=(numpyArr.shape[1]>>8)%256
        imgwidth3=(numpyArr.shape[1]>>16)%256
        imgwidth4=(numpyArr.shape[1]>>24)%256
        imgheight1=numpyArr.shape[0]%256
        imgheight2=(numpyArr.shape[0]>>8)%256
        imgheight3=(numpyArr.shape[0]>>16)%256
        imgheight4=(numpyArr.shape[0]>>24)%256
        imgsize1=arraysize%256    #liczba rzędów*kolumn+2*liczba rzedów
        imgsize2=(arraysize>>8)%256 
        imgsize3=(arraysize>>16)%256
        imgsize4=(arraysize>>24)%256

        fileheader=list([66, 77, filesize1, filesize2, filesize3, filesize4,0,0,0,0,54,0,0,0])

        infoheader=list([40,0,0,0,imgwidth1,imgwidth2,imgwidth3,imgwidth4,
        imgheight1,imgheight2,imgheight3,imgheight4,1,0,24,0,0,0,0,0,
        imgsize1,imgsize2,imgsize3,imgsize4,
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])               #24 - bity, kolejne 0 też

        out=bytearray()
        out.extend(fileheader)
        out.extend(infoheader)
        out.extend(array)

        f = open(outputName, "bw")
        f.write(out)
        f.close()

        

############
# TESTS?
############

sv=FileFormat()
flt = Filters()
ops = Operations()
#newPic=ops.flipImageVertical(flt.negativeFilter(flt.grayScaleHDR(img.imread("laura.tif"))))
#newPic=ops.rotateRight(img.imread("laura.tif"))
#showImage(newPic)
#plt.show()
sv.saveAsBMP(img.imread("laura.tif"), 'test.bmp')