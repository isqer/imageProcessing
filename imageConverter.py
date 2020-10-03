############
# SAVE/READ
############
class Write:
    def asBMP(self,numpyArr,outputName):
        array=list()
        padding=(numpyArr.shape[1]*3)%4
        for x in range(((numpyArr.shape[0])-1),-1,-1):
            for y in range(0,numpyArr.shape[1]):
                for z in range((numpyArr.shape[2]-1),-1,-1):
                    array.append(numpyArr[x,y,z])
                    
            for x in range (0,padding): #padding ma wyrownywac do 4 bitow
                array.append(0)

        arraysize=len(array)
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
