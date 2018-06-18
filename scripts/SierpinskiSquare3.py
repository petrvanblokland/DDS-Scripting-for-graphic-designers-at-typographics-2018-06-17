STEPS = 4.0

class SierpinskiSquare:
    
    def square(self, x, y, w, step):
        radius = w*3*random()
        oval(x + 20, y + 20, radius, radius)
        fill(1-step/STEPS, 1-step/STEPS, 1-step/STEPS)
        fill(random(), random(), random(), 0.7)
        rect(x + 20, y + 20, w, w)
        fill(random(), random(), random(), 0.7)
        rect(x + 20, y + 20, w, w)
          
    def draw(self, x, y, w, step):
        if step > STEPS:
            return
        w = w/3.0
        for px in range(0, 3):
            for py in range(0, 3):
                if px == 1 and py == 1:
                    self.square(x + w, y + w, w, step)
                else:
                    self.draw(x + px*w, y + py*w, w, step+1)    
                    
ssq = SierpinskiSquare()
ssq.draw(0, 0, 960, 0)
saveImage('SierpinsikySquare.pdf')
