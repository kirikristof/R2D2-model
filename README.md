# R2D2-model
A simple, 3D printed fan-made R2D2 replica, capable of rolling, turning it's head, and has some LEDs

We started this project as complete beginners, to keep us occupated in the summer, and to spend time doing something actually useful.
At first we wanted to make it wireless, but it turned out that is INSANELY hard, and we ran out of time. So now R2-D2 operates tethered with a USB cable.

**What does this project do, and how to use it?**
  It is really simple:
  * you flash MycroPython onto the Raspberry Pi Pico W from the official site, download Thonny IDE on your PC, and upload the code you find in the *firmware* folder
  * you plug the USB cable hanging from the bottom of the robot into your PC,
  * you open the code (which is already uploaded on the Pico) in Thonny, and hit RUN
  * you type w, a, s, d, q, e, z, and x from your keyboard into the Shell.
  * w means forward, s means backwards, q turns the head one way, e turns it the other way. x stops the head, z stops the wheels. With a you turn left, and with d        you turn right
  * also dont forget to turn the robot on with the switch hanging from the bottom (there are two holes at the bottom, one for the switch, the other for the USB),         otherwise the wheels won't work ;)
  * the batteries need to be removed for charging
