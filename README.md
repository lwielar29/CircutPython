# CircutPython
My circut python assignments
2019-2020
Engineering 3

LED FADE
 
Using CircutPython I developed code to make an led light slowly get brighter and then to slowly face back until it is very dim. I learned the basics on Circutpython and its differences from arduino coding. Specifically I learned how to import libraries into Circutpython and gained an understanding of dutycycle, the part of the code that makes the light fade a a certain rate.   
<img src="engineering/pics for github/ledfade.jpg" width="75">

LED BLINK

Similary to LED FADE, I used CircutPython to make my led turn on and off. Although it is a simple assignment using CircutPython instead of arduino required me to learn an almost new language of code. This code was simplier and so I gained a deeper understanding of the code. At first, I had a hard time firguring out if I would need to use the While True in my code. I learned that with such a simple code I didn't need to as there were no parameters needed for it to blink. 
<img src="media/octocat.jpg" width="75">

SERVO
 
For this assignment I learned how to make a servo spin back and forth using CircutPython code. The servo would spin in one direction when I touched one wire and would spin in the other direction when I touched the other wire. My favorite part of the assiignment was the touchio library. I found it interesting to gain a deeper understanding of how the metro board is able to sense that the wire has been touched through the disruption of electrons. A difficult part of this assignment was constructing my code so that when I touched the wire it did not move to the postion but would only move towards the position when I was touching the wire. I had to use "+= 5" to make this happen. 
<img src="media/octocat.jpg" width="75">

LCD PRESSES

I wired and coded an LCD screen to print the number of times I pressed a button through CircutPython. I had to add a lot of new libraries to CIRCUTROPY in order to use my LCD screen. This assignment mirrored a difficult assignment last year, but we used Circutpython code instead. Using my code from last year as a base for constrcuting this new code, the assignment was too difficult and highlightened the differnces and also similarites between arduino code and circutpython. I learned it was more simple to upload only certain parts of the library that I would be using my phrasing my code like this, "from digitalio import DigitalInOut, Direction, Pull." 
<img src="media/octocat.jpg" width="75">

PHOTOINTERRUPTER

This assignment required me to wire a photointerrupter and code so that it would count how many times something had passed between the photointerrupter legs. The tricky part was then that my serial monitor had to print how many times something had passed within my photointerrupter every 4 seconds. To do this I had to create values that represented the 4 seconds. I made a variable, "max" and made it equal 4. Then in my code I used the variable "remaining" and the current time since the program had been running "time.time" to construct a code that would only print every 4 seconds. 
<img src="media/octocat.jpg" width="75">

DISTANCE CENSOR

The distance censor was a fun assignment. Having already used a distance censor to create a robot, this assignment has an added twist. We created code to read the distance of an object from the censor and the distance corresponded to a  certain color of an led built into the metroboard. The closer the distance the color was red. It then transitioned to blues and then greens on a color fading scale. A hard part of the assignment was figuring out how to make an led a certain color. I had to google how an led works and the pixel coding for it to be a certain color. I learned that the code for coloring is an amount from 0-250 and is a combination of red, green, blue.  
<img src="media/octocat.jpg" width="75">

CLASSES, OBJECTS, AND MODULES

This assignment took coloring a RGB led to a whole new level. We had to make two rgb leds transition through 6 colors of the rainbow each at a different point in the cycle, utilizing the already assigned code. To make this code worked we had to create a class that created variables and functions that would enable the code to work. It was hard to create a class and know what I needed to put in the def __ init __ and what needed to be made its own function. I learned that the code in def ___ init __ would always  need to be true and always be running. This meant doing this such as setting the output and where they will find the pin. 
<img src="media/octocat.jpg" width="75">

HELLO VS CODE

For this assignment I used the code writing program VS Code to write code and upload it to my metroboard and then puch my code to my github with clicks of a few buttons stragiht from the program. I wrote a simple code that would print hello on the serial monitor. The tricky part of this assignment was installinga ll of the fies needed to run VS Code and learning how to git add and git commit on VS Code. I learned how to access the github part of VS Code and click the "+" to gitadd my code and then "ctrl enter" with a somment to commit my code to my git hub repository. 

FANCY LED

This assignment combined the hello vs. code assignment and the classes, objects, and modules assignment. In this assignment we wired 6 leds that would blink in a specific pattern - alternate, blink, chase, and sparkle. We decided in our code what these four patterns would entail. We were given a set code and had to make a class in VS Code that would make it work. I learned how to use a for statement as I needed to repeat areas of my code, but didn't want to jumble of writting it out. I learned to structure a for statement like this:  for i in range(0,5): "i" can be any sort of variable and the range dictates how many times it will repeat or is a great way to randomize a pattern when used with if statements.  

<img src="media/octocat.jpg" width="75">

