import cv2

path = "leaf.jpg"

img = cv2.imread(path)
print(img.shape)

width ,height =200 ,200
imgResize = cv2.resize(img,(width,height))
print(imgResize.shape)

imgCropped = img[300:540,0:900]
#imgCropped = img[0:900,300:540]
imgCropped = img[300:540,320:350]
imgCropResize = cv2.resize(imgCropped,(img.shape[1],img.shape[0]))
                        

cv2.imshow("leaf",img)
cv2.imshow("leaf Resize",imgResize)
cv2.imshow("leaf cropped",imgCropped)
cv2.imshow("leaf cropresize",imgCropResize)                           




cv2.imshow("leaf",img)
#cv2.waitkey(0)

