import cv2, time
# import time

video = cv2.VideoCapture(0)

check, frame = video.read()

print("==check==")
print(check)

print("==frame==")
print(frame)

# Sleep main thread for 3 secs
time.sleep(3)

cv2.imshow("VideoCapture", frame)
cv2.waitKey(0)

video.release()
cv2.destroyAllWindows()


