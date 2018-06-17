
W, H = 595, 842 # This is rounded A4, root of 2
PM = 70 # Margin around the page
Padding = 40
Frames = 40

for pn in range(Frames):
    newPage(W+2*PM, H+2*PM)
    # Draw the page background and frame
    fill(0)
    stroke(0,0,1)
    strokeWidth(0.5)
    rect(PM, PM, W, H)

    # Draw a number of squares in random (x,y)
    # and random color
    for n in range(54):
        stroke(None)
        fill(random(), random(), random(), 0.5)
        rect(random()*294+146, random()*276+180,
         176, 200)
    # Headline of the page
    # x = Margin left (PM) + padding inside page
    # y = Margin bottom (PM) + height - top padding
    # Calculate the "angle" stepping through 360 degrees by frames
    angle = pn/Frames*180
    # Calculate the sin value of the angle and scale vertical
    # by 50% and move up, so min equals 0 and max equals 1
    # Make fonts size between range of 30 and 80
    angleCos = cos(radians(angle))*0.5+0.5
    fontSize = (1-angleCos)*300+50
    textFill = (1-angleCos, angleCos, 1, angleCos)
    fs = FormattedString('Hello world', fontSize=fontSize, fill=textFill, stroke=None)
    tw, th = textSize(fs)
    text(fs, (PM+W/2-tw/2, PM+H-Padding-th))

saveImage('MyExamplePageBlackZoom.pdf')
saveImage('MyExamplePageBlackZoom.gif')
