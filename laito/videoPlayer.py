import numpy as np
import cv2
import sys
import time
import os
from cliConverter import cliConverter
import concurrent.futures

cap = cv2.VideoCapture(sys.argv[1])
videoFps = cap.get(cv2.CAP_PROP_FPS)
cliConv = cliConverter()
isVideoFinish = False
frame = [0]


def readFrame(cap):
    global frame
    global isVideoFinish

    while True:
        ret, frame = cap.read()
        if not ret:
            isVideoFinish = True
            break

    frame = []


def terminalImagePrinter():
    global isVideoFinish

    while not isVideoFinish:
        terminalImage = cliConv.imageToTerminalImage(frame, margin=2)
        terminalImageStr = cliConv.terminalImageToStr(terminalImage)
        print(terminalImageStr)


executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
frameIdx = 0
startTime = time.time()

while True:
    ret, frame = cap.read()

    if frameIdx == 0:
        executor.submit(terminalImagePrinter)

    if not ret:
        isVideoFinish = True
        break

    frameIdx += 1
    time.sleep(1 / videoFps)

elapsedSec = int(time.time() - startTime)
time.sleep(1)

cliConv.clearConsole()
print("{}秒".format(elapsedSec))
cap.release()
cv2.destroyAllWindows()
