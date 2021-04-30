import cv2
from matplotlib import pyplot as plt
import numpy as np
import RioDatas as RD


def imgShow(windowName:str,img):
	cv2.imshow(windowName, img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def drawRect(path, coordsXY: tuple, coordsX1Y1: tuple, color: tuple, thickness: int=2):
    cv2.rectangle(path, coordsXY, coordsX1Y1, color, thickness)

def detetctFirstAndLastPoints():
	returnedDict = {}
	try:
		startPoint = int(input("vortex eq gtnvum : ")) # orinak 4
		finishPoint = input("vortex eq gnum : ") # orinak cty
		finishPoint = finishPoint.upper()
		for shopName in RD.shopsWithCoordinates1Stage.keys():
			if finishPoint == shopName:
				returnedDict["finishPointName"] = finishPoint
				finishPoint = RD.shopsWithCoordinates1Stage[shopName]
				break
		else: raise AttributeError
	except AttributeError:
		print("tvov nsheq vortex eq gtnvum, greq xanuti anun@ te vortex petq e gnaq")
		detetctFirstAndLastPoints()
	
	returnedDict["start"] = [
		RD.pointRectanglesWayFirstStage[startPoint-1][0],
		RD.pointRectanglesWayFirstStage[startPoint-1][1]
	]
	returnedDict["finish"] = [
		finishPoint[0],
		finishPoint[1]
	]
	returnedDict["startPointID"] = startPoint
	
	return returnedDict

def detectWay(firstAndLastPoints: dict):
	startX = [firstAndLastPoints["start"][0][0],firstAndLastPoints["start"][1][0]]
	startY = [firstAndLastPoints["start"][0][1],firstAndLastPoints["start"][1][1]]

	nearFinishPoint = RD.pointsInFrontOfShops[firstAndLastPoints["finishPointName"]]
	if len(nearFinishPoint) >= 3:
		finishPoint = nearFinishPoint[len(nearFinishPoint) // 2]
	startPoint = firstAndLastPoints["startPointID"]
	
	if startPoint < finishPoint:
		return [point for point in range(startPoint, finishPoint+1)]
	elif startPoint == finishPoint: 
                return [startPoint]
	return [point for point in range(finishPoint, startPoint+1)]


	
