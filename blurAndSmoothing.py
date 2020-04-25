import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([30, 150, 50]) #take red color
    upper_red = np.array([255, 255, 180])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    #apply a simple smoothing, where we do a sort of averaging per block of pixels.
    # do a 15 x 15 square, which means we have 225 total pixels.
    kernel = np.ones((15, 15), np.float32) / 225
    smoothed = cv2.filter2D(res, -1, kernel)

    # result sacrifices alot of granularity.
    # Gaussian Blurring

    blur = cv2.GaussianBlur(res, (15, 15), 0)
    cv2.imshow('Gaussian Blurring', blur)
    median = cv2.medianBlur(res, 15) #median blur
    cv2.imshow('Median Blur', median)
    bilateral = cv2.bilateralFilter(res, 15, 75, 75) #bilateral blur
    cv2.imshow('bilateral Blur', bilateral)
    cv2.imshow('Original', frame)
    cv2.imshow('Averaging', smoothed)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()