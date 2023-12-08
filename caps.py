import math
import numpy as np
import cv2 as cv

imgName = input('Введите название файла: ')
img = cv.imread(f'imgs/{imgName}.jpg', cv.IMREAD_GRAYSCALE)
img = cv.resize(img, (int(img.shape[1]*0.7), int(img.shape[0]*0.7)))
cv.namedWindow('caps')

def nothing(x):
    pass

cv.createTrackbar('MinDist', 'caps', 1, 100, nothing)
cv.createTrackbar('Param1', 'caps', 10, 100, nothing)
cv.createTrackbar('Param2', 'caps', 10, 100, nothing)
cv.createTrackbar('MinRadius', 'caps', 0, 100, nothing)

cv.setTrackbarPos('MinDist', 'caps', 20)
cv.setTrackbarPos('Param1', 'caps', 50)
cv.setTrackbarPos('Param2', 'caps', 50)
cv.setTrackbarPos('MinRadius', 'caps', 0)

minDist = param1 = param2 = minRadius = 0
pminDist = pparam1 = pparam2 = pminRadius = 0

# img = cv.imread(f'imgs/12-1.jpg', cv.IMREAD_GRAYSCALE)

while True:

    minDist = cv.getTrackbarPos('MinDist', 'caps')
    param1 = cv.getTrackbarPos('Param1', 'caps')
    param2 = cv.getTrackbarPos('Param2', 'caps')
    minRadius = cv.getTrackbarPos('MinRadius', 'caps')

    img = cv.medianBlur(img, 5)
    cimg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
    circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT,
                              1.2, minDist=minDist,
                              param1=param1, param2=param2,
                              minRadius=minRadius, maxRadius=0)

    circles = np.uint16(np.around(circles))
    x0 = 0
    y0 = 0 
    r0 = math.hypot(int(img.shape[1]), int(img.shape[0]))
    print(img.shape[0])
    for i in circles[0, :]:
        # draw the outer circle
        cv.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
        if r0 > math.hypot(int(i[0]), (int(i[1])-int(img.shape[0]))):
            x0 = i[0]
            y0 = i[1]
            r0 = math.hypot(int(i[0]), (int(i[1])-int(img.shape[0])))

    n = 1
    for i in circles[0, :]:
        if i[0] != x0 and i[1] != y0:
            cv.line(cimg, (x0, y0), (i[0], i[1]), (255, 0, 0), 2)
            x1 = int(i[0]) - int(x0)
            y1 = int(y0) - int(i[1])
            dist = math.hypot(x1, y1)
            # print(f'X{n}: {x1}, Y{n}: {y1}, R{n}: {dist}')
            n += 1

    cv.imshow('caps', cimg)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
