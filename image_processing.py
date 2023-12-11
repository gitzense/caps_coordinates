import math
import numpy as np
import cv2 as cv
from datetime import datetime as dt

print ('\nВаше изображение должно находиться в папке imgs\n')
while True:
    try:
        imgName = input('Введите название файла c расширением: ')
        img = cv.imread(f'imgs/{imgName}', cv.IMREAD_GRAYSCALE)
        img = cv.resize(img, (int(img.shape[1]*0.7), int(img.shape[0]*0.7)))
        break
    except AttributeError:
        print('\nЧто-то пошло не так, попробуйте снова \n')
    except KeyboardInterrupt:
        print('\nЗавершение выполнения программы\n')
        break

cv.namedWindow('Coordinates finder')    

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
        r0 = math.hypot(int(cimg.shape[1]), int(cimg.shape[0]))
        for i in circles[0, :]:
            # draw the outer circle
            cv.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 1)
            # draw the center of the circle
            cv.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
            if r0 > math.hypot(int(i[0]), (int(i[1])-int(cimg.shape[0]))):
                x0 = i[0]
                y0 = i[1]
                r0 = math.hypot(int(i[0]), (int(i[1])-int(cimg.shape[0])))

        n = 1
        for i in circles[0, :]:
            if i[0] != x0 and i[1] != y0:
                cv.line(cimg, (x0, y0), (i[0], i[1]), (0, 0, 0), 1)
                x1 = int(i[0]) - int(x0)
                y1 = int(y0) - int(i[1])
                dist = math.hypot(x1, y1)

                if int(i[0])-50 < 0 and int(i[1])-15 > 0:
                    cv.putText(cimg, f'X{n}:{x1}, Y{n}: {y1}', (i[0], i[1]-10), cv.FONT_HERSHEY_SIMPLEX , 0.4, (255, 0, 0), 1, cv.LINE_AA)
                elif int(i[0])-50 < 0 and int(i[1])-15 < 0:
                    cv.putText(cimg, f'X{n}:{x1}, Y{n}: {y1}', (i[0], i[1]+15), cv.FONT_HERSHEY_SIMPLEX , 0.4, (255, 0, 0), 1, cv.LINE_AA)
                elif int(i[0])+100 > cimg.shape[1] and int(i[1])-15 < 0:
                    cv.putText(cimg, f'X{n}:{x1}, Y{n}: {y1}', (i[0]-100, i[1]+15), cv.FONT_HERSHEY_SIMPLEX , 0.4, (255, 0, 0), 1, cv.LINE_AA)
                elif int(i[0])+150 > cimg.shape[1]:
                    cv.putText(cimg, f'X{n}:{x1}, Y{n}: {y1}', (i[0]-100, i[1]-10), cv.FONT_HERSHEY_SIMPLEX , 0.4, (255, 0, 0), 1, cv.LINE_AA)
                else:
                    cv.putText(cimg, f'X{n}:{x1}, Y{n}: {y1}', (i[0]-50, i[1]-10), cv.FONT_HERSHEY_SIMPLEX , 0.4, (255, 0, 0), 1, cv.LINE_AA) 
                
                print(f'X{n}: {x1}, Y{n}: {y1}, R{n}: {dist}')
                n += 1
        print('\n')

        cv.imshow('Coordinates finder', cimg)

    except TypeError:
        print('Упс! Ошибочка вышла, не перебарщивайте с параметрами!')

    except NameError:
        break

    except KeyboardInterrupt:
        print('\nЗавершение работы программы\n')
        break
        
    try:
        if cv.waitKey(1) & 0xFF == ord('s'):
            cv.imwrite(f'imgs/circle_screen_{dt.now().hour}_{dt.now().minute}_{dt.now().second}.jpg', cimg)

        if cv.waitKey(1) & 0xFF == ord('e'):
            print('\nЗавершение работы программы\n')
            break

    except KeyboardInterrupt:
        print('\nЗавершение работы программы\n')
        break

cv.destroyAllWindows()
