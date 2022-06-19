from PIL import Image
from importlib import resources
import cv2
import os

class Load:
    def get_captcha_text(self, imgPath):
        skeleton = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z']
        captchaText=""

        for j in range(0, 6):
            image = Image.open(imgPath).convert('L')
            croppedImg = image.crop((j*30, 0, (j+1)*30, 45))
            pixelMatrix = croppedImg.load()
            for col in range(0, croppedImg.height):
                for row in range(0, croppedImg.width):
                    if pixelMatrix[row, col] != 0:
                        pixelMatrix[row, col] = 255

            imgPathSplit = imgPath.split("/")
            binDir = ""
            for i in range (0, len(imgPathSplit)-1):
                binDir = binDir + imgPathSplit[i]+"/"
        
            croppedImg.save(binDir + "captcha" + "_" + str(j) + ".png")

        tempDic = {}
        for i in range(0,6):
            img1 = cv2.imread(binDir + "captcha" + "_" + str(i) + ".png")
            for bone in skeleton:
                with resources.open_binary('captcha_crack', bone+".png") as fp:
                    img2 = cv2.imread(fp.name)

                errorL2 = cv2.norm(img1, img2, cv2.NORM_L2)
                similarity = 1 - errorL2 / (45 * 30)

                tempDic[bone] = similarity
            captchaText = captchaText + max(tempDic, key=tempDic.get)

        
        for i in range(0,6):
            os.remove(binDir + "captcha" + "_" + str(i) + ".png")
         
        return captchaText