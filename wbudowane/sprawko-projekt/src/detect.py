import numpy as np
import cv2
import cv2.aruco as aruco
import sys, time, math

aruco_dict  = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
parameters  = aruco.DetectorParameters_create()

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:

    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    corners, ids, rejected = aruco.detectMarkers(image=gray, dictionary=aruco_dict, parameters=parameters)

    if ids is not None:
        aruco.drawDetectedMarkers(frame, corners)
        for i in range(0, len(ids) ):
            corner = corners[i][0]
                x_sum = corner[0][0] + corner[1][0] + corner[2][0] + corner[3][0]
                x = x_sum / 4
                normalised = (x - 640) / 640
                print(ids[i][0], -normalised)

    cv2.imshow('frame', frame)

    # Nacisniecie klawisza q zatrzymuje program
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
