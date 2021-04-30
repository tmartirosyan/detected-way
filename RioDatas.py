shopsWithCoordinates1Stage = {
    "CTY": [(160, 210), (180, 230)],
    "MAGUS": [(390, 350), (410, 370)],
    "GOODS HOUSE": [(760, 350), (780, 370)],
    "NATALI PHARM": [(560, 125), (580, 145)],
    "GLOBAL BEAUTY": [(455, 125), (475, 145)],
    "ASCONA": [(760, 100), (780, 120)],
    "BOOKINIST": [(1010, 220), (1030, 240)],
}
# shopsWithCoordinates2Stage = {}
# shopsWithCoordinates3Stage = {}
pointsInFrontOfShops = {
    "CTY": [0,1,2],
    "MAGUS": [2],
    "GLOABL BEAUTY": [2,3,4],
    "NATALI PHARM": [4],
    "GOODS HOUSE": [4,5,6],
    "ASCONA": [5,6],
    "BOOKINIST": [6],
}
pointRectanglesWayFirstStage = [
    [(420, 40), (440, 60)],
    [(360, 110), (380, 130)],
    [(360, 220), (380, 240)],
    [(560, 220), (580, 240)],
    [(740, 220), (760, 240)],
    [(940, 220), (960, 240)]
]


PATH = "1.png"
RIO = {
    # key: stage, value: shops directory
    1: shopsWithCoordinates1Stage
}