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
video.release()
cv2.destroyAllWindows()


