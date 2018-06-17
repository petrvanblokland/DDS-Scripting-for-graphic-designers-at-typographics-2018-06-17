
for n in range(20):
    newPage(500, 500)
    for m in range(400):
        fill(random(), random(), 1)
        if random() < 0.5:
            rect(50+random()*362, 50+random()*354, 20+random()*40, 20+random()*40)
        else:
            oval(50+random()*362, 50+random()*354, 20+random()*40, 20+random()*40)

saveImage('DemoManeSquares.gif')
