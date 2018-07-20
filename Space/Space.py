from tkinter import *
from Spaceship import *
from Asteroid import *
from tkinter.font import Font
import time
import threading
class Space(object):
    """docstring for Space."""
    def __init__(self,root):
        super(Space, self).__init__()
        self.root = root
        self.widscore = Label(text="0")
        self.widscore.pack(side=TOP)
        self.canvas = Canvas(self.root,bg='#000015',height=500,width=500)
        self.canvas.pack()
        self.life = Label(text="Vie : ♥ ♥ ♥")
        self.life.pack()
        self.widscore.pack(side=TOP)
        quitter = Button(self.root,text="Quitter",command=quit)
        quitter.pack()
        self.score = 0
        self.spaceship = SpaceShip(self)
        self.lastposShip=[]
        self.lastposShip.append(self.spaceship.getX())
        self.lastposShip.append(self.spaceship.getY())
        self.asteroids=[]
        self.asteroids.append(Asteroid(self))
        self.asteroids.append(Asteroid(self))
        self.asteroids.append(Asteroid(self))
        self.asteroids.append(Asteroid(self))
        for aster in self.asteroids:
            aster.setDaemon(True)
            aster.start()
        self.objects = {}
        self.semaphore = threading.BoundedSemaphore()
        self.objects["ship"]=self.canvas.create_image(self.spaceship.getX(), self.spaceship.getY(), image=self.spaceship.getSprite())
        self.objects["asteroid0"]=self.canvas.create_oval(self.asteroids[0].getX(),self.asteroids[0].getY(),self.asteroids[0].getX()+self.asteroids[0].getWidth(),self.asteroids[0].getY()+self.asteroids[0].getWidth(),fill="#805650")
        self.objects["asteroid1"]=self.canvas.create_oval(self.asteroids[1].getX(),self.asteroids[1].getY(),self.asteroids[1].getX()+self.asteroids[1].getWidth(),self.asteroids[1].getY()+self.asteroids[1].getWidth(),fill="#805650")
        self.objects["asteroid2"]=self.canvas.create_oval(self.asteroids[2].getX(),self.asteroids[2].getY(),self.asteroids[2].getX()+self.asteroids[2].getWidth(),self.asteroids[2].getY()+self.asteroids[2].getWidth(),fill="#805650")
        self.objects["asteroid3"]=self.canvas.create_oval(self.asteroids[3].getX(),self.asteroids[3].getY(),self.asteroids[3].getX()+self.asteroids[3].getWidth(),self.asteroids[3].getY()+self.asteroids[3].getWidth(),fill="#805650")

        self.root.bind('<q>',self.spaceship.moveLeft)
        self.root.bind('<d>',self.spaceship.moveRight)
        self.root.bind('<z>',self.spaceship.moveUp)
        self.root.bind('<s>',self.spaceship.moveDown)

    def update(self):
        if self.spaceship.getHp()==0:
            self.quit()
        # self.event.clear()
        self.semaphore.acquire()
        self.canvas.delete(self.objects["asteroid0"])
        for aster in self.asteroids:
            if self.spaceship.collide(aster.getX(),aster.getY(),aster.getWidth()):
                self.spaceship.looseHp()
                if self.spaceship.getHp() == 2:
                    self.life['text']= "Vie : ♥ ♥"
                if self.spaceship.getHp() == 1:
                    self.life['text']= "Vie : ♥"
                if self.spaceship.getHp() == 0:
                    self.life['text']= "Vie : "
                    self.quit()
                aster.abortTheMission()
                if self.spaceship.getHp()>0:
                    newaster = Asteroid(self)
                    newaster.setDaemon(True)
                    newaster.start()
                    self.asteroids[self.asteroids.index(aster)]=newaster

        self.canvas.delete(self.objects["asteroid0"])
        self.objects["asteroid0"]=self.canvas.create_oval(self.asteroids[0].getX(),self.asteroids[0].getY(),self.asteroids[0].getX()+self.asteroids[0].getWidth(),self.asteroids[0].getY()+self.asteroids[0].getWidth(),fill="#805650")
        self.canvas.delete(self.objects["asteroid1"])
        self.objects["asteroid1"]=self.canvas.create_oval(self.asteroids[1].getX(),self.asteroids[1].getY(),self.asteroids[1].getX()+self.asteroids[1].getWidth(),self.asteroids[1].getY()+self.asteroids[1].getWidth(),fill="#805650")
        self.canvas.delete(self.objects["asteroid2"])
        self.objects["asteroid2"]=self.canvas.create_oval(self.asteroids[2].getX(),self.asteroids[2].getY(),self.asteroids[2].getX()+self.asteroids[2].getWidth(),self.asteroids[2].getY()+self.asteroids[2].getWidth(),fill="#805650")
        self.canvas.delete(self.objects["asteroid3"])
        self.objects["asteroid3"]=self.canvas.create_oval(self.asteroids[3].getX(),self.asteroids[3].getY(),self.asteroids[3].getX()+self.asteroids[3].getWidth(),self.asteroids[3].getY()+self.asteroids[3].getWidth(),fill="#805650")
        if (self.spaceship.getX()!=self.lastposShip[0] or self.spaceship.getY()!=self.lastposShip[1]):
            self.canvas.delete(self.objects["ship"])
            self.objects["ship"]=self.canvas.create_image(self.spaceship.getX(), self.spaceship.getY(), image=self.spaceship.getSprite())
        self.canvas.update()
        self.lastposShip=[self.spaceship.getX(),self.spaceship.getY()]
        self.semaphore.release()
        # self.event.set()
    def quit(self):
        for aster in self.asteroids:
            aster.abortTheMission()
        font = Font(family='Liberation Serif', size=100)
        self.canvas.create_text(100,100,text="Perdu",anchor='w',font=font,fill='red')
        self.canvas.update()
        time.sleep(5)

        print(threading.active_count())
        self.root.unbind('<q>')
        self.root.unbind('<s>')
        self.root.unbind('<d>')
        self.root.unbind('<z>')
        self.root.destroy()
    def setScore(self,score):
        self.score=score+self.score
        self.widscore['text']="Score = "+str(self.score)
    def getAsteroids(ast):
        return self.asteroids[ast]
root = Tk()
space = Space(root)
root.mainloop()
root.destroy()
