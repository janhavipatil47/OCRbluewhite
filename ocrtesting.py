import pytesseract
import cv2
import numpy as np
import re
img=cv2.imread("ocr9.jpeg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,bwimg = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
imgbit=cv2.bitwise_not(bwimg)
kernel=np.ones((2,2),np.uint8)
imgdilate=cv2.erode(imgbit,kernel,iterations=3)
imgdilate=cv2.bitwise_not(imgdilate)

imgdilate=cv2.bitwise_not(imgdilate)
cv2.imshow("Image",imgdilate)
cv2.waitKey(0)
cv2.destroyAllWindows()
ocrres=pytesseract.image_to_string(imgdilate)
regex1='^\d\d.\d'
regex2='^\d.\d'
regex3='^\d.\d'
regex4='^\d\d\d.\d'
regex5='^. \d\d\d\d'
ocrres1=re.search(regex1,ocrres)
ocrres2=re.search(regex2,ocrres)
ocrres3=re.search(regex3,ocrres)
ocrres4=re.search(regex4,ocrres)
ocrres5=re.search(regex5,ocrres)

if(ocrres1):
  print(ocrres1.group())
elif(ocrres2):
  print(ocrres2.group())
elif(ocrres3):
  print(ocrres3.group())
elif(ocrres4):
  print(ocrres4.group())
elif(ocrres5):
  print(ocrres5.group())