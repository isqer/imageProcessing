import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np

############
# MISC
############

# wrzuci się do klasy później - musimy to omówić
def showImage(picture):
    if picture.ndim == 2:
        plt.imshow(picture, cmap='gray')
    else:
        plt.imshow(picture, cmap=None)  # dzięki temu nie musisz wybierać między cmap gray a None

############
# FILTERS
############
class Filters:
    def __init__(self):
        pass  # jakis init musi byc

    def grayScaleNTSC(self, picture):  # zawsze musisz dac self
        output = np.zeros((picture.shape[0], picture.shape[1]))  # czy z tego funkcje?
        for x in range(0, picture.shape[0]):
            for y in range(0, picture.shape[1]):
                output[x, y] = 0.299 * picture[x, y, 0] + 0.587 * picture[x, y, 1] + 0.114 * picture[x, y, 2]
        return output

    def grayScaleHDTV(self, picture):
        output = np.zeros((picture.shape[0], picture.shape[1]))  # czy z tego funkcje?
        for x in range(0, picture.shape[0]):
            for y in range(0, picture.shape[1]):
                output[x, y] = 0.2126 * picture[x, y, 0] + 0.7152 * picture[x, y, 1] + 0.0722 * picture[x, y, 2]
        return output

    def grayScaleHDR(self, picture):
        output = np.zeros((picture.shape[0], picture.shape[1]))  # czy z tego funkcje?
        for x in range(0, picture.shape[0]):
            for y in range(0, picture.shape[1]):
                output[x, y] = 0.2627 * picture[x, y, 0] + 0.6780 * picture[x, y, 1] + 0.0593 * picture[x, y, 2]
        return output

    def negativeFilter(self, picture):
        output = 0
        if picture.ndim == 2:
            output = 255 - picture[:, :]
        else:
            output = 255 - picture[:, :, :]
        return output

    def brightness(self, picture, value):
        if picture.ndim == 2:
            out = np.zeros_like(picture, dtype='int16')
            for x in range(0, picture.shape[0]):
                for y in range(0, picture.shape[1]):
                    out[x, y] = picture[x, y] + value
            np.clip(out, 0, 255)
            out = np.uint8(np.clip(out, 0, 255))
            return out
        elif picture.ndim == 3:
            out = np.zeros_like(picture, dtype=np.uint8)
            for x in range(0, picture.shape[2]):
                out[:, :, x] = self.brightness(picture[:, :, x], value)
            return out

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