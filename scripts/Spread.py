import os

A4 = 595, 842

class Image(object):
    def __init__(self, path, x, y, w, h):
        self.path = path
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
    def draw(self, page):
        if os.path.exists(self.path):
            image(self.path, (self.x, self.y))
        else:
            # Create random image color
            fill(random(), random(), random())
            stroke(None) # No frame around image
            # For now, draw the image as a random color
            rect(page.padding+self.x, page.padding+self.y, 
                self.w, self.h )    
                 
    
class Text(object):
    
    def __init__(self, s, x, y):
        self.s = s
        self.x = x
        self.y = y
        
    def draw(self, page):
                # Headline
        fill(0.8)
        stroke(None)
        rect(page.padding+self.x, page.padding+self.y,
             page.w-2*page.padding, 20 )    
        fontSize(32)
        font('Verdana')
        fill(0)
        text(self.s, (page.padding+self.x, page.padding+self.y))
         
class Page(object):
    
    def __init__(self, w, h, title=None, padding=None):
        self.w = w
        self.h = h
        self.title = title or 'Untitled'
        self.padding = padding or 40
        self.elements = []
        
    def __repr__(self):
        return '%s(w=%d,h=%d,%s)' % (self.__class__.__name__, self.w, self.h, self.title)
    
    def draw(self):
        newPage(self.w, self.h) # Create a DrawPage in the right size
        stroke(0.5) # Set stroke to 50% gray
        fill(None) # No fill
        # rect(x, y, w, h)
        # x = left side of page to left of padding
        # y = bottom side of page to bottom of padding
        # w = width of the page - left padding - right padding
        # h = height of the page - bottom padding - top padding
        rect(self.padding, self.padding, 
            self.w-2*self.padding, self.h-2*self.padding)
        
        for element in self.elements:
            element.draw(self)
       
# ---------------------------------------------------
# Application

Gutter = 16
W, H = A4
page = Page(W, H, 'MySpread')
page.elements.append(Image('Type@Cooper.pdf', 0, 0, 330, 608))
page.elements.append(Text('Hello world and other', 0, 728))
page.elements.append(Text('Another text', 0, 458))
page.elements.append(Image('aaa', 0, 536, 516, 174))
page.elements.append(Image('aaa', 0, 394, 50, 50))
page.elements.append(Image('aaa', -10, 162, 268, 120))
page.elements.append(Image('aaa', 246, 248, 50, 50))
page.draw()

saveImage('SpreadExample.pdf')