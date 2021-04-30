import cv2
from matplotlib import pyplot as plt
import numpy as np
import RioDatas as RD
import functionality as functional

img = cv2.imread(RD.PATH)
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thrash = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    area = img.shape[0] * img.shape[1]
    coordinates = approx.ravel()
    cooeds_area = (coordinates[0] - coordinates[-2]) * (coordinates[1] - coordinates[-1])
    if len(approx.ravel()) == 8 and cooeds_area > area - 100:  # or cooeds_area < 30:
        print(approx.ravel())
        continue
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 2)
    x = approx.ravel()[0]
    y = approx.ravel()[1]

index = 1
for point in RD.pointRectanglesWayFirstStage:#range(len(point_rectangles_way)):
    functional.drawRect(img,point[0],point[1],(0,255,0))
    cv2.putText(img,str(index),point[0],cv2.FONT_HERSHEY_SIMPLEX,1,(0, 102, 255),1,cv2.LINE_AA)
    index += 1

for point in RD.shopsWithCoordinates1Stage.values():#range(len(point_rectangles_way)):
    functional.drawRect(img,point[0],point[1],(255,0,0))


# functional.imgShow("window",img)
detetctedFirstAndLastPoints = functional.detetctFirstAndLastPoints()
functional.drawRect(img,detetctedFirstAndLastPoints["start"][0],detetctedFirstAndLastPoints["start"][1],(0,0,255))
functional.drawRect(img,detetctedFirstAndLastPoints["finish"][0],detetctedFirstAndLastPoints["finish"][1],(0,0,255))
print(functional.detectWay(detetctedFirstAndLastPoints))
functional.imgShow("window",img)