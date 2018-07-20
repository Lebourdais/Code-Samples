from tkinter import *
class SpaceShip(object):
    """docstring for SpaceShip."""
    def __init__(self,space):
        super (SpaceShip, self).__init__()
        self.hp = 3
        self.posx = 250
        self.posy = 480
        self.space = space
        self.sprite = PhotoImage(file="ship.gif")

    def looseHp(self):
        self.hp = self.hp-1

    def moveRight(self,event):
        self.posx += 5
    def moveLeft(self,event):
        self.posx -= 5
    def moveUp(self,event):
        self.posy -= 5
    def moveDown(self,event):
        self.posy += 5

    def getX(self):
        return self.posx
    def getY(self):
        return self.posy
    def getSprite(self):
        return self.sprite
    def getHp(self):
        return self.hp
    def collide(self,x,y,width):
        if self.posx< x+width and self.posy>y and self.posy<y+width and self.posx>x :
            return True
        return False
