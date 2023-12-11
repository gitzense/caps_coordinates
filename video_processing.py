import cv2 as cv
import math
import numpy as np
from datetime import datetime as dt
from os import mkdir

folderName = f'{dt.now().day}.{dt.now().month}.{dt.now().year} {dt.now().hour}_{dt.now().minute}_{dt.now().second}'
mkdir(f'imgs/{folderName}')

i = 0
k = 0
cap = cv.VideoCapture(0)
screenCheck = False

while True:
    try:
        if screenCheck == False:
            while True:
                ret, frame = cap.read()

                # dim = (int(frame.shape[1]*0.7), int(frame.shape[0]*0.7))
                # frame = cv.resize(frame, dim)
                
                cv.imshow('Video', frame)

                if cv.waitKey(1) & 0xFF==ord('s'):
                    screenPath = f'imgs/{folderName}/screen{i}.png'
                    cv.imwrite(screenPath, frame)
                    screenCheck = True
                    i += 1
                    cv.destroyWindow('Video')
                    break

                if cv.waitKey(1) & 0xFF == ord('e'):
                    screenCheck = None
                    break

        elif screenCheck == True:
            cv.namedWindow('Coordinates finder')
            img = cv.imread(screenPath, cv.IMREAD_GRAYSCALE)

            def nothing(x):
                pass

            cv.createTrackbar('MinDist', 'Coordinates finder', 1, 100, nothing)
            cv.createTrackbar('Param1', 'Coordinates finder', 10, 100, nothing)
            cv.createTrackbar('Param2', 'Coordinates finder', 10, 100, nothing)
            cv.createTrackbar('MinRadius', 'Coordinates finder', 0, 100, nothing)

            cv.setTrackbarPos('MinDist', 'Coordinates finder', 20)
            cv.setTrackbarPos('Param1', 'Coordinates finder', 50)
            cv.setTrackbarPos('Param2', 'Coordinates finder', 50)
            cv.setTrackbarPos('MinRadius', 'Coordinates finder', 0)

            minDist = param1 = param2 = minRadius = 0

            while True:
                try: 
                    minDist = cv.getTrackbarPos('MinDist', 'Coordinates finder')
                    param1 = cv.getTrackbarPos('Param1', 'Coordinates finder')
                    param2 = cv.getTrackbarPos('Param2', 'Coordinates finder')
                    minRadius = cv.getTrackbarPos('MinRadius', 'Coordinates finder')

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
                            print(f'X{n}: {x1}, Y{n}: {y1}, R{n}: {dist}')
                            n += 1

                    cv.imshow('Coordinates finder', cimg)
                    
                except TypeError:
                    print('Упс! Ошибочка вышла, не перебарщивайте с параметрами!')

                if cv.waitKey(1) & 0xFF==ord('s'):
                    cv.imwrite(f'imgs/{folderName}/circle_screen{k}.png', cimg)
                    k += 1
            
                if cv.waitKey(1) & 0xFF == ord('c'):
                    screenPath = None
                    screenCheck = False
                    cv.destroyWindow('Coordinates finder')
                    break

                if cv.waitKey(1) & 0xFF == ord('e'):
                    screenCheck = None
                    break
        
        elif screenCheck == None:
            break

    except KeyboardInterrupt:
        print('\nЗавершение работы программы\n')
        break

cv.destroyAllWindows()
                
    


