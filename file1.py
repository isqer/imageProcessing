# nazwie się później
# INFORMACJE

############
# IMPORT
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

# wrzuci się do klasy później - musimy to omówić
def showImage(picture):
    if picture.ndim == 2:
        plt.imshow(newPic, cmap='gray')
    else:
        plt.imshow(newPic, cmap=None)  # dzięki temu nie musisz wybierać między cmap gray a None


############
# FILTERS
############
class Filters:
    def __init__(self):
        pass  # jakis init musi byc

    def arrayCreator(self, picture,param1,param2,param3):
        output = np.zeros((picture.shape[0], picture.shape[1]))  # czy z tego funkcje?
        for x in range(0, picture.shape[0]):
            for y in range(0, picture.shape[1]):
                output[x, y] = param1 * picture[x, y, 0] + param2 * picture[x, y, 1] + param3 * picture[x, y, 2]
        return output

    def grayScaleNTSC(self, picture):  # zawsze musisz dac self
        output=self.arrayCreator(picture,0.299,0.587,0.114)
        return output

    def grayScaleHDTV(self, picture):
        output=self.arrayCreator(picture,0.2126,0.7152,0.0722)
        return output

    def grayScaleHDR(self, picture):
        output=self.arrayCreator(picture,0.2627,0.6780,0.0593)
        return output

    def negativeFilter(self, picture):
        output = 0
        if picture.ndim == 2:
            output = 255 - picture[:, :]
        else:
            output = 255 - picture[:, :, :]
        return output


############
# OPERATIONS
############

class Operations:
    def __init__(self):
        pass

    def crop(self, picture, x1, y1, x2, y2):
        if picture.ndim == 2:
            return picture[x1:x2, y1:y2]
        else:
            return picture[x1:x2, y1:y2, :]

    def flipImageHorizontally(self, picture):
        if picture.ndim == 2:
            return picture[:, :0:-1]
        else:
            return picture[:, :0:-1, :]

    def flipImageVertical(self, picture):
        if picture.ndim == 2:
            return picture[:0:-1, :]
        else:
            return picture[:0:-1, :, :]

    def rotateLeft(self, picture):
        if picture.ndim == 2:
            result = picture[:, :]
            result = np.rot90(result)
            return result.astype("uint8")
        elif picture.ndim == 3:
            result = np.zeros((picture.shape[0], picture.shape[1], picture.shape[2]))
            result[:, :, 0] = self.rotateLeft(picture[:, :, 0])
            result[:, :, 1] = self.rotateLeft(picture[:, :, 1])
            result[:, :, 2] = self.rotateLeft(picture[:, :, 2])
            return result.astype("uint8")

    def rotateRight(self, picture):
        return self.rotateLeft(self.rotateLeft(self.rotateLeft(picture)))  # HEHEHE


############
# TESTS?
############


flt = Filters()
ops = Operations()
newPic=ops.flipImageVertical(flt.negativeFilter(flt.grayScaleHDR(img.imread("laura.tif"))))
# newPic=ops.rotateRight(img.imread("laura.tif"))
showImage(newPic)
plt.show()
