from Drawable import Drawable

class Eraser(Drawable):
    def __init__(self):
        self.x = -100
        self.y = -100
    
    def update(self, x, y):
        self.x = x
        self.y = y
        
    def draw(self):
        stroke(0)
        x=self.x
        y=self.y
        line(x-15, y, x+15, y)
        line(x, y-15, x, y+15)
        
    def collides(self, x, y):
        return False