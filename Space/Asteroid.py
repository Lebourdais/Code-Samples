from threading import Thread
from random import *
import time
class Asteroid(Thread):
    """docstring for Asteroid."""
    def __init__(self, space):
        super(Asteroid, self).__init__()
        self.space = space
        self.x = randrange(50,500)
        self.y = 0
        self.width = randrange(40,100)
        self.abort = False
        self.speed = randrange(50,230,50)
    def run(self):
        while not(self.abort):
            for i in range(0,self.speed):
                self.y=i*500/(self.speed)
                time.sleep(0.05)
                if self.abort:
                    return
                self.space.update()
            self.space.setScore(10)
            self.width = randrange(40,100)
            self.x = randrange(50,500-self.width)
            self.speed = randrange(50,230,50)


    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getWidth(self):
        return self.width
    def abortTheMission(self):
        self.abort=True
        try:
            self.join()
        except RuntimeError as e:
            return
