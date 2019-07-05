import cv2

img = cv2.imread("ibises.jpg", 0) # 1 means Read as Colored Image, 0 as B/W

shape = img.shape
print(shape)
resizedImg = cv2.resize(img, (shape[0]//2, shape[1]//2))

cv2.imshow("Title", resizedImg)

cv2.imwrite("MyIbises.jpg", resizedImg)

cv2.waitKey(0)
cv2.destroyAllWindows()