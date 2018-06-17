
W, H = 595, 842 # This is rounded A4, root of 2
PM = 70 # Margin around the page
Padding = 40

for pn in range(20):
    newPage(W+2*PM, H+2*PM)
    # Draw the page background and frame
    fill(0.95, 0.90, 0.92)
    stroke(0)
    strokeWidth(0.5)
    rect(PM, PM, W, H)
    # Headline of the page
    # x = Margin left (PM) + padding inside page
    # y = Margin bottom (PM) + height - top padding
    fs = FormattedString('Hello world', fontSize=60, fill=0, stroke=None)
    tw, th = textSize(fs)
    text(fs, (PM+W/2-tw/2, PM+H-Padding-th))
    # Draw a number of squares in random (x,y)
    # and random color
    for n in range(54):
        stroke(None)
        fill(random(), random(), random(), 0.5)
        rect(random()*294+146, random()*276+180,
         176, 200)

saveImage('MyExamplePage.pdf')
saveImage('MyExamplePage.gif')
