from Rectangle import Rectangle


class TextBox(Rectangle):
    def __init__(self, rect=Rectangle(), s='', textcolor=(0,0,0)):
        self.rect = Rectangle()
        self.s = s
        self.col = textcolor
        

    def update(self, s):
        self.s += s

    def draw(self):
        print self.ft
        textFont(self.ft, 24)
        fill(self.col)
        text(self.s, self.x, self.y)
        print self.s, self.x, self.y

    def collides(self, x, y):
        return (self.x - x)**2 + (self.y - y)**2 <= 400  # whatever
