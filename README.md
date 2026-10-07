# R2D2-model
A simple, 3D printed fan-made R2D2 replica, capable of rolling, turning it's head, and has some LEDs

We started this project as complete beginners, to keep us occupated in the summer, and to spend time doing something actually useful.
At first we wanted to make it wireless, but it turned out that is INSANELY hard, and we ran out of time. So now R2-D2 operates tethered with a USB cable.

**What does this project do, and how to use it?**
  It is really simple:
  * you flash MycroPython onto the Raspberry Pi Pico W from the official site, download Thonny IDE on your PC, and upload the code you find here, in the *firmware* folder
  * you plug the USB cable hanging from the bottom of the robot into your PC,
  * you open the code (which is already uploaded on the Pico) in Thonny, and hit RUN
  * you type w, a, s, d, q, e, z, and x from your keyboard into the Shell.
  * w means forward, s means backwards, q turns the head one way, e turns it the other way. x stops the head, z stops the wheels. With a you turn left, and with d        you turn right
  * also dont forget to turn the robot on with the switch hanging from the bottom (there are two holes at the bottom, one for the switch, the other for the USB),         otherwise the wheels won't work ;)
  * the batteries need to be removed for charging
  * The robot is capable of rolling forward and backwards, turning left and right, and rotating it's head. It also has a red and blue (red means low battery, blue means ok) , green and yellow LED (they change color depending on head position).

**What have we learned?**

_Lászlóffy Tamás_: My role was the 3D modelling and the designing. I learned the Fusion 360 management, the use of bluprints, methods of 3D printing, and of course the consequences of my small mistakes which only came to light during assembly. Optimizing the tolerance, figuring out modelling maneuvers and loopholes (especially R2's Dome); these were the most complicated ones. Of course I had some headaches or rage-quit moments; however, I enjoyed the process.

_Benedek Kristóf_: My role was building the electronics, and coding. I've learned the basics of MicroPython, and understanding the basics of low-voltage, low-amperage DC circuits. I've had to learn soldering, understanding how the software communicates with hardware, and how to make the two understand each other. I've also learnt, that overengineering certain features just adds unnecessary complexity, and sometimes trying to make everything perfect at first is the one that causes the problems later on. Iáve also learnt the importance of time management, and communication between teammates.

**What have we changed?**
During the process we had to change some things (Because we overestimated our capabilities at the moment)
