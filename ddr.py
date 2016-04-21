from threading import Thread
import random
import time
from gameView import DDRWindow
from Queue import Queue
from gameLogicHandler import GameLogicHandler

def main():
	arrowQueue = Queue()
	gameLogic = GameLogicHandler(arrowQueue)
	logicHandlerThread = Thread(target = gameLogic.threadInit)
	win = DDRWindow("DDR", 500, 500)
	logicHandlerThread.start()
	win.startGame(2, arrowQueue)


if __name__ =="__main__": main()


	
