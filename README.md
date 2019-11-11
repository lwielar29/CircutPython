# CircutPython
My circut python assignments
2019-2020
Engineering 3

LED FADE
 
Using CircutPython I developed code to make an led light slowly get brighter and then to slowly face back until it is very dim. I learned the basics on Circutpython and its differences from arduino coding. Specifically I learned how to import libraries into Circutpython and gained an understanding of dutycycle, the part of the code that makes the light fade a a certain rate.   

LED BLINK

Similary to LED FADE, I used CircutPython to make my led turn on and off. Although it is a simple assignment using CircutPython instead of arduino required me to learn an almost new language of code. This code was simplier and so I gained a deeper understanding of the code. At first, I had a hard time firguring out if I would need to use the While True in my code. I learned that with such a simple code I didn't need to as there were no parameters needed for it to blink. 

SERVO
 
For this assignment I learned how to make a servo spin back and forth using CircutPython code. The servo would spin in one direction when I touched one wire and would spin in the other direction when I touched the other wire. My favorite part of the assiignment was the touchio library. I found it interesting to gain a deeper understanding of how the metro board is able to sense that the wire has been touched through the disruption of electrons. A difficult part of this assignment was constructing my code so that when I touched the wire it did not move to the postion but would only move towards the position when I was touching the wire. I had to use "+= 5" to make this happen. 

LCD PRESSES

I wired and coded an LCD screen to print the number of times I pressed a button through CircutPython. I had to add a lot of new libraries to CIRCUTROPY in order to use my LCD screen. This assignment mirrored a difficult assignment last year, but we used Circutpython code instead. Using my code from last year as a base for constrcuting this new code, the assignment was too difficult and highlightened the differnces and also similarites between arduino code and circutpython. I learned it was more simple to upload only certain parts of the library that I would be using my phrasing my code like this, "from digitalio import DigitalInOut, Direction, Pull." 

PHOTOINTERRUPTER

This assignment required me to wire a photointerrupter and code so that it would count how many times something had passed between the photointerrupter legs. The tricky part was then that my serial monitor had to print how many times something had passed within my photointerrupter every 4 seconds. To do this I had to create values that represented the 4 seconds. I made a variable, "max" and made it equal 4. Then in my code I used the variable "remaining" and the current time since the program had been running "time.time" to construct a code that would only print every 4 seconds. 

DISTANCE CENSOR

The distance censor was a fun assignment. having already used a distance censor to create a robot, this assignment has an added twist. We created code to read the distance of an object from the censor and the distance corresponded to a  certain color. The closer the distance the color was red. I tthen transitioned to blues and then greens. 

CLASSES, OBJECTS, AND MODULES

HELLO VS CODE

FANCY LED

HELLO PROCESSING
