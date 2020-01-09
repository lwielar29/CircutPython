# CircuitPython
### My circuit python assignments
2019-2020 // Engineering 3 // All pictures are from [Tim Wiessman's github page](https://github.com/tweissm35) 



## TABLE OF CONTENTS
* [TABLE OF CONTENTS](#TABLE-OF-CONTENTS)
* [LED FADE](#LED-FADE)
* [LED BLINK](#LED-BLINK)
* [SERVO](#SERVO)
* [LCD PRESSES](#LCD-PRESSES)
* [PHOTOINTERRUPTER](#PHOTOINTERRUPTER)
* [DISTANCE SENSOR](#DISTANCE-SENSOR)
* [CLASSES, OBJECTS, AND MODULES](#CLASSES-OBJECTS-AND-MODULES)
* [HELLO VS CODE](#HELLO-VS-CODE)
* [FANCY LED](#FANCY-LED)


  


 ## LED FADE
 
Using CirciutPython I developed code to make an led light slowly get brighter and then to slowly face back until it is very dim. To do this I had to utilize PWM, pulse width modification, and dutycycle which control the amount of energy/pulse/voltage that is sent to the the LED making it fade.  

<img src="https://github.com/tweissm35/CircuitPython/blob/master/media/fade.jpg" width="350">

Fritzing from [Tim Wiessman's github page](https://github.com/tweissm35/CircuitPython) 

### Lessons Learned
I learned the basics of Circuitpython and its differences from arduino coding. Specifically, I learned how to import libraries into Circuitpython by writing at the top of your code "import *library*". I also gained an understanding of dutycycle, the part of the code that controls the amount of time the led is ON compared to the time it taks to complete the cycle. This caused the LED to fade. [More info for PWM](https://learn.adafruit.com/circuitpython-essentials/circuitpython-pwm)
 

  


## LED BLINK

Similarly to LED FADE, I used CircuitPython to make my led turn on and off repeatedly. Although it is a simple assignment using CircuitPython instead of arduino required me to learn a new language of code to read the state of an LED, control it, and use my serial monitor. 

<img src="https://github.com/tweissm35/CircuitPython/blob/master/media/fade.jpg" width="350">

Fritzing from [Tim Wiessman's github page](https://github.com/tweissm35/CircuitPython) 

### Lessons Learned
At first, I had a hard time figuring out if I would need to use the While True in my code. I learned that with such a simple code I didn't need to as there were no parameters needed for it to blink. I also learned how to read an LED in circuitpython. Instead of using digitalread and digitalwrite as we used in arduino I used ".value" The LED is still read as being True (on) or False (off). 

  


## SERVO
 
For this assignment, I learned how to make a servo spin back and forth 180 degrees using CircuitPython code. The servo would spin in one direction when I touched one wire and would spin in the other direction when I touched the other wire. To enable this I had to download and import the touchio library. 

<img src="https://github.com/tweissm35/CircuitPython/blob/master/media/servo.jpg" width="400">

Fritzing from [Tim Wiessman's github page](https://github.com/tweissm35/CircuitPython) 

### Lessons Learned
I found it interesting to gain a deeper understanding of how the metro board can sense that the wire has been touched through the disruption of electrons. A difficult part of this assignment was constructing my code so that when I touched the wire it did not move to the position but would only move slowly towards the position when I was touching the wire. I had to use "angle += 5" to make this happen instead of just telling the servo to move to one position or "angle."



  

## LCD PRESSES

I wired and coded an LCD screen to print the number of times I pressed a button through CircuitPython. I had to add a lot of new libraries to CIRCUITROPY in order to use my LCD screen and had to read my button as variable rather than a state. This assignment mirrored a difficult assignment last year, but we used Circuitpython code instead. Using my code from last year as a base for constructing this new code, the assignment highlighted the differences and also similarities between Arduino code and circuit python. 


<img src="https://github.com/tweissm35/CircuitPython/blob/master/media/lcdcount.jpg" width="400">

Fritzing from [Tim Wiessman's github page](https://github.com/tweissm35/CircuitPython) 

### Lessons Learned
I learned it was more simple to upload only certain parts of the library that I would be using my phrasing my code like this, "from digitalio import DigitalInOut, Direction, Pull."

  



## PHOTOINTERRUPTER

This assignment required me to wire a photointerrupter and code so that it would count how many times something had passed between the photointerrupter legs. The tricky part was then that my serial monitor had to print how many times something had passed within my photointerrupter every 4 seconds. To do this I had to create values that represented the 4 seconds. I made a variable, "max" and made it equal 4. Then in my code I used the variable "remaining" and the current time since the program had been running "time.time" to construct a code that would only print every 4 seconds. 

<img src="https://github.com/tweissm35/CircuitPython/blob/master/media/photointerrupter.jpg" width="350">

Fritzing from [Tim Wiessman's github page](https://github.com/tweissm35/CircuitPython) 

### Lessons Learned
I gained a deeper understanding of the time libraries that are available other than time.sleep(). In this assignment I used the function time.time() to make the serial monitor only print after 4 seconds had elapsed. I learned that time.time() is used to measure the time since the board and code have started running and can be used when you need to manipulate the timing in your code.  




  
## DISTANCE SENSOR

Having already used a distance sensor, this assignment had an added twist. We created code to read the distance of an object from the sensor. An led built into the metroboard would then change colors corresponding to how far away the object was from the distance sensor. The closer the distance the color was red. It then transitioned to blues and then greens on a color fading scale. 

<img src="https://github.com/tweissm35/CircuitPython/blob/master/media/ultrasonicsensor.jpg" width="350">

Fritzing from [Tim Wiessman's github page](https://github.com/tweissm35/CircuitPython) 

### Lessons Learned
A hard part of the assignment was figuring out how to make the led a certain color. I had to google how an led works and the pixel coding for it to be a certain color. I learned that the code for coloring is an amount from 0-250 and is a combination of red, green, blue in that order. For example the combination to color and RGB led fully red would be (255, 0, 0).   



  
## CLASSES, OBJECTS, AND MODULES

This assignment took coloring a RGB led to a whole new level. We had to make two rgb leds transition through 6 colors of the rainbow each at a different point in the cycle, utilizing the already assigned code. To make this code worked we had to create a class that created variables and functions that would enable the code to work. 

<img src="https://github.com/tweissm35/CircuitPython/blob/master/media/rgb.jpg" width="350">

Fritzing from [Tim Wiessman's github page](https://github.com/tweissm35/CircuitPython) 

### Lessons Learned
It was hard to create a class and know what I needed to put in the def __ init __ and what needed to be made its own function. I learned that the code in def ___ init __ would always need to be true and always be running. In this case I used def__ init__ to set the output and the pins for the LEDs. Another part of def__ init__ is that it is run automatically and therefore will always need to be true. 

  


## HELLO VS CODE

For this assignment I used the code writing program VS Code to write code and upload it to my metroboard and then upload my code to my github with clicks of a few buttons straight from the program. I wrote a simple code that would print "hello" on the serial monitor and then sent it to my github right from where I wrote my code! 

### Lessons Learned
The tricky part of this assignment was installing all of the files needed to run VS Code and learning how to git add and git commit on VS Code. I learned how to access the github part of VS Code and click the "+" to gitadd my code, then "ctrl enter" with a comment to commit my code, and finally to click push to push my changes/new codes to my github repository. 


  

## FANCY LED

This assignment combined the hello vs. code assignment and the classes, objects, and modules assignment. In this assignment we wired 6 leds that would blink in a specific pattern - alternate, blink, chase, and sparkle. We decided in our code what these four patterns would entail. We were given a set code and had to make a class in VS Code that would make it work. In my code alternate alternated the blinking of the outside LEDs with the inside LEDS, blink made all the LEDs turn off and on together, chase caused each LED to blink on and off in a wave pattern, and sparkle made the LEDs blink in a random pattern. 

<img src="https://github.com/tweissm35/CircuitPython/blob/master/media/fancyLED.jpg" width="350">

Fritzing from [Tim Wiessman's github page](https://github.com/tweissm35/CircuitPython) 

### Lessons Learned
I learned how to use a for loop as I needed to repeat areas of my code, but didn't want the hassle of writing it out and wanted to condense my code. I learned to structure a for statement like this: for i in range(0,5):. "i" can be any sort of variable and the range dictates how many times it will repeat. I learned a For loop is a great way to randomize a pattern when used with if statements and to repeat areas of code.  


