import cv2, datetime

video = cv2.VideoCapture(0)

frames = 0

while True:

    frames = frames + 1

    check, frame = video.read()
    print(frame) # numpy nd array
    cv2.imshow("MyVideo", frame)

    key = cv2.waitKey(1) # 1 is 1 milli sec

    # Press q to quit the program
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

print(">> Total Frames Captured:", frames)

# Assignment:
# 1. Save the frames as a video | API
# 2. Create a program on motion detection


# Link to further explore OpenCV :)
# https://opencv.org/
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
# https://docs.opencv.org/master/d9/df8/tutorial_root.html
