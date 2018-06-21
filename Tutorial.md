
# 2018-06-18 PageBot Workshop

_Live blog style notes by @davelab6_

Petr: So now you have a document design for a PDF to print, but what if you instead want the document to be an animation with a voice-over audio that lays out the document slowly in time and explains why you put things where. Well you need to do it all again in a different 'motion design' application. Now lets jump in to using DrawBot to show how that works in 1 hour. 

I have a design workshop, 6 hours split 50/50, or 6 weeks. Try to do design then coding? Wont work. First week, do it all. Start with a width and weight. Whole thing. Then do it again. Then you can NEVER miss a 'final' presentation, because you are just increasing the level of detail in each week. 

We will skip the part of installing it on your your machine. I will make a public git repo for what we do today; it helps typing with me, if you type yourself, it helps you to learn... but may you get a syntax error, then you can copy from the reference material. 

This is a film plot and now we are back to french grammar :) We will try to get there again, in a short time :)

So open DrawBot. It presents Python code in the top right, the output graphics on the left, and any 'REPL' output on the bottom right. It is designed to make it as easy as possible for a graphic designer to start writing programs that produce graphics. 

Top right is a programming area, where the code lives. Type

    print()

and you see the text `print` becomes blue, which helps you to understand what you are typing. Then the parens contain the arguments, and then inside them we add a text string, delimited in quotes. 

    print("Hello world")

Congrats, your first python program, it works!

You you can run

    print("Hello world" * 10)

and this is already saving you time. It saved you some copy and paste. 

Dividing by 10 would not make sense and will produce a `TypeError`. 

    print("Hello world" / 10)

Python is somewhat intuitive, you see how something works and likely you can reapply the ideas in a future thing. 

You can multiply and divide numbers of course. 

    print(123123 * 123123123)

This is the core of programming. You have verbs  or  methods or functions, like this `print()`, the actions; and arguments, attributes or variables, which are the nouns, the things the actions apply to/from.

The reason DrawBot was made is that if I have a text file and output HTML, I only deal with text. From a programmer, that is fine. But for a designer, who wants to make images, this is not sufficient. 

And images are not built into Python. So DrawBot is made to explain Python to explain programming to designers quickly, with the things you need built in. So when you load DrawBot, you can code

    draw()

and you'll see this remains black, not blue, because it is not part of the core Python language, and it gives an error that tells you what to do. It says you need 4 positional arguments, x y w and h. The x and y are the bottom left of the page - which is different from the web, but is like a mathematical cartesian model where y goes up and x goes right - but pages of text start for Latin text on the top left, and work across and down. Just chose to stick with the mathematical origin position. So, x and y is the starting location from the origin. Then w and h are width and height. 

    rect(0, 0, 595, 842)

This works, and you see the canvas is drawn as a square, and then a black rectangle is drawn like that. We see those canvas and that color and stroke are defaults. 

DrawBot has a fun part that is hidden: you have new text on the bottom right when you hit Cmd-R to run. Like HTML/CSS, you change CSS and reload. I think a neat thing that Just and Frederik did. Just started it and Frederick took on the development, and DrawBot is part of RoboFont which he makes. It is all volunteers and no big companies are behind it. 

So the fun thing Frederick added is that you can hold down the cmd key and draw the rectable and you see the origin x and y values changing. This is direct feedbck. I can estimate where I want this, and then edit the values to 70 70 and then I have a nice margin, and re-run to see it. 

Next, we can change the color. 

    fill()

will do this. You see the error, and you want to add RGB values. 

    fill(0.95, 0, 0)

0.95 is almost pure red, and no blue or green. 

    fill(0.95, 0.90, 0.92)

this is a light pink. The function is like dipping your pen, it sets a color for subsequent use with the pen. Similarly there is

    stroke(0)

which sets the stroke color black. 

And to make a stroke painted, we set the width of the stroke:

    strokeWidth (0.5)

So now you have a nice small program that draws something. You can finally save the design as a output. 

    saveImage()

without any arguments this will save in the same folder as your file. So lets now save your program, such as with the filename `ExamplePage.py`, where `.py` shows it is a python program. 

If you set the filename and extension, the extension will set the file format. So to make a PDF, add to the end of the program and run:

    saveImage('MyExamplePage.pdf')

PDF is a complex format. It would be very complex to make a PDF part by part. So there is a method behind the scenes that knows all the complexity and presents it very simply to you.

Now lets add more into the page design after the above `rect()`

    rect(200, 200, 200, 50)

Now when I run with Cmd-R, then you see the PDF is already updated. And when I hold Cmd and grad our new box around, the PDF is updated live too, because each time I update the numbers by dragging, the whole program is re-run, including the PDF generation. 

Now, I can also hold Cmd and drag the number in the code area itself. So I can change the color of the 2nd box by adding a new fill line before that 2nd rect:

    `fill(0,0,0)

and then highlight the first red value and drag it up. 

So lets drag that red box in the drawing area and make it at the top like a headline area. 

THen copy and paste these fill and rect lines, change the color to blue, and move it to be in the position of the text column, and change its w and h values. 

But we don't need to copy and paste all the time to create more cols. 

In Python there is a random number generator

    random()

You can run

    print(random())

and you see the output tray gives a random number between 0 and 1. 

You can put that in the fill method's values too, to get random colors. 

    fill(random(), random(), random())

Now we want to add lots of boxes. For this we add a major new programming idea, loops. Here is the head of the loop that defines it in Python:

    for n in range(50):

Most programming languages use parens of some kind to delimit the loop's body from its head. But Python uses the typography of the code, the white space. This means as programmers in Python you can not be sloppy with your code's typography, and it means the code looks the same between different people, which helps you to read another's code. 

    for n in range(50):
      fill(random(), random(), random())
      rect(random()*100+50, 450, 176, -190)

This is way of saying a minimum value of 50, and a maximum of 100, or a random value between. We can make the floor and ceiling 200 and 150, so there is more room for it to play in. If you rerun a few times now you see it jump around. 

And I can cmd-drag the y value of 450, and you see this is a kind of animation. 

I can cmd-drag the range(50) and you see how many boxes we haev. 

This is already programming design, parametric design. You can modify these values. 

But we are only outputting one page. It is 1000 x 1000 units. But what if we want more than one page? Or several pages as animation frames?

So now we remove any playful lines and make the program only do what we need. 

Now we put the whole thing in a loop:

```py


fill(0.95,0.90,0.92)
stroke(0)
strokeWidth(0.5)
rect(70, 70, 595, 842)

fill(0.2, 0.2, 0.92)
rect(136, 780,458,50)

for n in range(50):
  fill(random(), random(), random())
  rect(random()*200+150, random()*270+180, 176, 200)

saveImage("MyExamplePage.pdf")
```

Then at the top of this on line 1, we add 

    for pn in range(20):

and then select everything and press Tab, to indent it all. 

Then in the second line of the document, the first line of the loop body:

    newPage()

this will now make 20 pages. 

At the very top, lets start to make this program more parametric. 

Add 3 lines to the top of the doc, and on line 2 add

    W, H = 595, 842

And then it took us time to find these values [ discussed before I started note taking ] so we can add a comment. In Python that is any text after a `#`. 

    W, H = 595, 842 # This is rounded A4, root of 2

We also want some page margins. 

    PM = 70 # Marin around the page

Now we can make our first `rect()` which defines the page use these variables instead of the direct values

    rect(PM, PM, W, H) 

And add a comment after `newPage()` for explaining the next few lines:

    # draw the page background and frame

Naming variables is half the work! Not too long, not too generic, and say exactly what you will understand them to be. 

Now when we run this, `newPage()` gives an error. 

The page of our document is larger than our canvas, so we want to add a width plus room for 2 margins, and same for height:

    newPage(W+2*PM, H+2*PM)

Now we have a 20 page document, similar in some respects, and a different illsutration. 

This is parametric design. 

Now we look at the PDF, and you can flip through it and think of this as a 10 page InDesign document output as a PDF. But it was made by a program. 

Now we can make it look better. 

The random colors can have 3 or even 4 values. RGB, and transparency. Maybe we don't like the black stroke here. Then we set the stroke to `None` which is a special Python value that means "no object." 


```py
for n in range(50):
  stroke(None) # no stroke
  fill(random(), random(), random(), 0.5) # transparency
```

Now, instead of making a PDF, chagne the final line to 

    saveImage('MyExamplePage.gif')

And now you see an animating GIF in your folder! Not another hour of work to do it again in another application. 

[ 12:20 ]

## FormattedString

THis was a straightforward program. So far we have this placeholder of text. Let's change that. 

`FormattedString` is build into DrawBot and allows you to make rich text. 

When you work with an app, you need backups. Text documents are very small, but app native files are binary and very large, and easily corrupted. If this is broken, you can open it and read it and fix it.

A good programming practice is that values startig with a capital will not change, and usually are defined at the top of the program document. 

We have margins, now we can add padding at the top under that. 

   Padding = 40

Then after our first `rect()` for the page, we can add text, and we need 3 things; the text string, then its x and y position, in a "tuple" or pair of values for x and y. 

We want the x value to be the margins and padding, and the y value to be the page margin and the height of the page up and then the padding down. This can be written using this variable arithmatic with the variables we already have. They are a little cryptic so we can add a comment before to explain them:

    # Headline of the paeg
    # x = Margin left (PM) + padding inside page
    # y = Margin bottom (PM) + height of the page (H) - top padding
    text("hello world", (PM + Padding, PM + H - Padding))

Oh no! This has outline, and color, and the typeface is a default, Lucida. 

So before that `text()` we can set those things directly:

   fontSize(90)
   fill(0)
   stroke(None)
   
That will do it. But that is not parametric. It is like setting things by hand, one by one, in InDesign. 

USing InDesign, you set type styles, and then apply the named styles to your page elements. 

We can do similar now, using FormattedString. It is easier to set all these attributes of the text, as arguments to the function. 

Before the fontSize(), add a new line,

    fs = FormattedString()

Now we fill inside the parens a new thing here, "keyword arguments." We can use the function names directly, and remove them:

    fs = FormattedString('Hello world', fontSize=90, fill=0, stroke=None)
    text = (fs,  (PM + Padding, PM + H - Padding))

But this is still not parametric enough, it just moved syntax around.

Since we have an `fs` object, we can ask it things like "How big are you now?" and get the text width and text height, and set those to `th` and `tw` variables:

    fs = FormattedString('Hello world', fontSize=90, fill=0, stroke=None)
    tw, th = textSize(fs)

And now change

    text = (fs,  (PM + Padding, PM + H - Padding))

to

    text = (fs,  (PM + Padding, PM + H - Padding - th))

If we want to start from the middle of the page, we take the page width (W) and divide by 2. 

    text = (fs,  (PM + W/2 - tw/2, PM + H - Padding))

Now our text is centered, and we can change the fontSize keyword vlaue, and it remains in the center, because the position is always relative to the page size vlaue and the font size value. 

We are now getting into where DrawBot ends. In PageBot, the extended library, there is more functionality to dive into the text. Where is teh stem starting? the minimum pixel box around a text, not the emSquare box? 

Alright, we have made an animation, a poster, or a model or a poster, and we didn't make 1, we have made 100s. 

We can add more text. We can change the colors. Make the text pure white and the page bill pure black and the colors are transparent. 

We are going to review your school math. 

Imagine the rotation of a wheel with a hole and a pin, running across a horizontal bar, so that a sine wave is drawn as the wheel rolls along: the pin goes quickly up or down in the middle and slower when its at the top and bottom. 

So you have a function for this. The angle goes from 0 to 90 to 360 and resets. 

    sin(angle)

If we want to draw this, in 10 steps, we dividew 360 by the number of frames we have, it can be 20 or 22, inceasing filesize and smoothness. WE can easily cahnge the number of frames. 

    frames = 10
    360 / frames

We have radians for angles too. 

So this is math, but only one line! :) 

In our formatting string, we have the fontSize keyword. This is hard set to 60. 

And we can add at the top of our main loop,

   print(pn)

and you'll see that it starts at 0 and goes to 19, as we have a range of 20. 

We can use this an index for our angle. We'll make a new top level variable at the top of the document,

   Frames = 20

and then set the range to Frames,

   for n in range(Frames):

and then on a new line before our `fs =` assignment, we can set the step angle

    angle = Frames / 360

and then make it a ratio based on page number

    angle = pn * Frames / 360

We want to know the value related to it. 

    fontSize = sin(radians(angle))

And since a sine wave goes from -1 to 1, the total height is 2. So we need to halve the height of the sine wave, so that its total height is 1, but that is still -0.5 to 0.5. So we then move it up a bit, adding 0.5. 

    fontSize = sin(radians(angle)) * 0.5 + 0.5

AmstelvarAlpha_Optical size.gif`

On the left you see a fixed and large pt size, showing the actual shapes; on the right you see pt size changing with the opsz. And the right is left aligned and the left is right aligned. You can see the jump in smaller sizes; the jump from 36 to 38 is not as dramatic as 10 to 12. 

So when the customer says, change the height, the speed, and the typeface, then sure, its just values. 

`Decovar_Decovar.gif` shows the axis the way they are meant to be used; they are never intended to be used all together as you can do on www.axis-praxis.org

It like a radio with 'play all stations at the same time' - not a good idea. Or a swiss army knife where you open all the knifes and sissors and saws at the same time. You turn then on one by one or maybe 2 at a time. 

This wave-animating shows the axes moving nicely, one at a time. A simple loop. 

Here is DJR's fit, and you can see one frame, two frames and three frames, each filled by the letters, and its a small jump from 1 to 2 to 3. 

Here you see 4 axes working at the same time. 

What is the new definitoin of proofing a variable font? 6,000 pages? or a GIF that gives an impression of thing working together. 

You see how close these real wroking jobs are to what we did in the last 90 minutes. 

Here is `AmstelvarBanner.py`, and you see it is a similar amount of code. 

[ 13:10 ] 

Time for lunch! 20 mins

[ 13:30 ]

## Classes

Petr: Okay, lets review some code examples in the PageBot repo.

`SierpinskySquare3.py` introduces flow control, with if/else statements, and also recursion. 

We can control STEPS value and see how that changes the whole thing. Since it is exponential, 5 will take longer to calculate. 

WE can save this as a PDF, change STEPS back to 4 to save some time. 

So we have a PDF and you can zoom in, and see this is vector graphics. We can open it in Adobe Illustrator. 

You have a lot of design options you would not think of because it is so much work. 

I made PageBot open source, and you can find our work today in <https://github.com/petrvanblokland/DDS-Scripting-for-graphic-designers-at-typographics-2018-06-17>

When you use Python, you are using an object orientated language, that is dynamic. Older languages were not OO, and had to be compiled to machine code before they could run. 

In C programming, you write code to do this and that, and the actor is the programmer. In our example with the fractal square, we saw 'classes'. 

This is not exactly like classes in CSS, but has some similarities. 

I want to explain the idea of Object Orientated Programming to you, with the example of physical objects: Automobiles. 

Again I advise you to type with me, but the reference file is `CarWithComments.py` and it is part of the Github repo. 

Say we are dealing with cars. Here is the most simple class we can have:

    class Car():
      pass

This is a defintion. It is not the same part of the process as where it is being used. So lets add a dividing comment after that

    # ----------------------------------------

Under that, lets use the class we made

    myCar = Car()
    print(myCar)

And when we run this, we see this output:

    <__main__.Car object at 0x10f8870b8>

The class by itself does nothing. It is a factory generating cars, but does nothing right now. 

**While it is CALLED "Car()", it is not a car itself, it is an object that outputs car objects.**

Each output is called an 'instance.' 

So we could add this comment

    # Factory of Cars --> generates cars (which are Instances)

The fact that the factory is itself an object, means you can have factories of factories. Physical factories that make things are buildings, that are made. 

The 'root' object is a python object `object`; deep inside Python is the thing that is creating factories. 

So, when I buy a car, the first thing I want to do is drive it. That would work like this:

    myCar = Car()
    myCar.drive

But this errors because the factory did not make cars that can drive. We need to tell the car what to do with that instruction. Lets return the car to the factory and redesign the car making process so it outputs cars that undersatnd what drive means. In python this is done with a `def` to **def**ine the function's functionality. 

    class Car():

      def drive(self):
        print("I am driving")

    # -----------------

    myCar = Car()
    myCar.drive

and this now works, and you see "I am driving" in the DrawBot output tray. 

Now we want more from driving, it doesn't just go forwards and that is it. We want to be able to at least say if the amount of driving should be 0 or a positive amount, and probably we need some limit. 

    myCar.drive(0)
    myCar.drive(30)
    myCar.drive(100)

What does the `self` do in the definition of `drive`?

    def drive(self, speed):
      print("I am driving", speed, "m/hr")

Now those 3 drives will work, showing the speed. 

But we can go 45,000,000 miles an hour. Can we limit the speed, so that even if you ask for that speed, you don't get it? Yes. We need a value in the factory's scheme for the max speed.

Again, we add this as an all caps variable before our definition, a convention that tells you something about the variable. My class has an initial cap so you reognise it as a class name, and my methods/functions start with lowercase, and constants, things that do not change, are all caps. 

And then we use the python `min` function to get the minomum value between two values, so that if the speed provided is greater than MAX_SPEED, we get the latter. 


    class Car():

      MAX_SPEED = 120
      def drive(self, speed):
        print("I am driving", min(speed, self.MAX_SPEED), "m/hour")

    #----------------

    myCar = Car()
    myCar.drive(500)

you see the output

    I am driving 120 m/hour

But this still works

    myCar.drive(-500)

Maybe that is the car going backwards?

So we need to add a min speed?

```py
class Car():

      MAX_SPEED = 120
      MIN_SPEED = -20
      def drive(self, speed):
          speed = min(speed, self.MAX_SPEED)
          speed = max(speed, self.MIN_SPEED)
          print("I am driving", speed, "m/hour")

#----------------

myCar = Car()
myCar.drive(500)
myCar.drive(-500)
```

Output:

    I am driving 120 m/hour
    I am driving -20 m/hour

...

Now we can add some defaults to the class. 

```py
class Car():

    MAX_SPEED = 120
    MIN_SPEED = -20

    def __init__(self, color):
        pass
    
    def drive(self, speed):
    # ...
#-------------
```

You can override or redefine these class defaults. 

The `__init__` is a special function name provided by Python. 

There is also ``__repr__`` which allows you to set what is returned by an object by default, such as when that object is printed:

``py
class Car():

    MAX_SPEED = 120
    MIN_SPEED = -20

    def __repr__(self):
    	return("I am a happy car")

    def __init__(self, color):
    	self.color = color # Paint the shell in the given color
        # TODO add engine, wheels, seat
        # Here the car is finished and sent to the dealer
    
    def drive(self, speed):
        speed = min(speed, self.MAX_SPEED)
        speed = max(speed, self.MIN_SPEED)
        print("I am driving", speed, "m/hour")

#----------------

myCar = Car('Blue')
print(myCar.color)
myCar.drive(500)
myCar.drive(-500)
print(myCar)
```

Output:

```
Blue
I am driving 120 m/hour
I am driving -20 m/hour
I am a happy car
```

[ Lots of context about Object Orientated Programming history ]

Books are great, but they are heavy and slow to look up information. So knowing what to look up, is powerful, and today I hope you have learned what to look up.

It is nice to have my studio in Delft, and have students join us. Once a month I have type[media students, and 5+ years ago they loved to borrow my books but now they snap a photo and instantly have a PDF from somewhere ;)

When you get a Moleskin notebook, and use it for sketches, and scan them, remember to get it out of the scanner! :) 

I encourage you to sketch on paper. 

I can draw 10 sketches of a website on paper in the time it takes someone to open Adobe Illustrator and make one. Students say that is not fair, but neither the paper sketch or the illustrator drawing is a website either :) 

I use ScanSnap Manager. I have a few sketchbooks so you can take a look at my process :)

...

The following was seen in my Robothon 2018 presentation:

Here is a 1995 Font Bureau Type Specimen from 1995, made with Quark XPress. We have that file, but we can no longer read it; the Quark software is long gone. 

I have Python programs from 1995, and I can still run them, and I can relatively quickly upgrade them to the latest Python 3 version to run in the latest version; either myself, or hire someone to do it. Because it is libre software and plain text data, that everyone can work with. 

So I scanned a page from the printed FB TS book, and drew guidelines, and measured them; its like a revival typeface, tracing outlines scanned in. 

Here is an inbetween stage, and this is the final reproduction. 

Another is `ATFVariableTypeSpecimen.py` and you can see this working with Bungee, and the various kinds of Bungee fonts, in a 1923 specimen layout. I think this is funny :)

...

We decided to move Font Bureau into Type Network, so that we could share the costs of running a foundry between type designers, and share tools, education, clients. 

Neville Brody joined in 2 days ago. My foundry is "Typetr" and I have published several faces there. There is a 'format' for a TypeNetwork foundry, where I can change my color but everythigng else is fixed. So I make my own typeface promotional websites with PageBot. Then I can change everything:

<http://upgrade.typenetwork.com>

The website contents is in MarkDown, there is no CMS, and I can give the MD files to an editor and they can pass them back to me and plug straight into a regenerated versino of the website. 

The GIFs all are linked to PDFs. The same source generates an optimal result for that medium. 

Since PageBot can see what is supported inside the font, the HTML/CSS is generated by PageBot that inspects the font. 

This Noordji Cube animation is also made with a PageBot script. 

Some things are hard to find out, like how to make a 3d cube image animate, but you only find it out once, and then put it in a function, and re-use it. 

[ More pagebot tutorial ]

PageBot was intended to replace InDesign, and today I have almost every element replicated. 

So you now have some ideas of how to program your design. If you work with developers, you maybe can better discuss your ideas with them. And to write your own programs is a life long journey. 

Q: Does it output HTML/CSS?

A: Yes, it is the weakest part of PageBot still. It is a huge front and we need more people to move it forwards. I am not an expert in knowing JS, nor InDesign. If I was, probably I would not make PageBot ;) There are areas that I can show you that export HTML/CSS and right now that was solved with existing tempaltes and we filled them in, instead of generating all the code. 

You can write scripts do make a cover and do the rest in InDesign, or do the cover in Illustrator and typeset the book in PageBot. I am not an InDesign user any more, but I still use applications for specific tasks. 

...

[ more pagebot example on `Spread.py` setting up a page and placing Text and Rect elements on it. 

...

If you have any questions, please contact me at <buro@petr.com>

[ had to leave at 16:00 ]
