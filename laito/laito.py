from cliConverter import cliConverter
import sys
import cv2
import time

img = cv2.imread(sys.argv[1])
cliConv = cliConverter()
tImage = cliConv.imageToTerminalImage(img)
print(cliConv.terminalImageToStr(tImage))
time.sleep(5)
cliConv.clearConsole()
