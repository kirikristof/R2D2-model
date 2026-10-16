# R2D2-model
<img width="3000" height="4000" alt="16083" src="https://github.com/user-attachments/assets/55b7023d-0e51-4f7c-a882-3057224f9302" />

A simple, 3D printed fan-made R2D2 replica, capable of rolling, turning it's head, and has some LEDs

We started this project as complete beginners, to keep us occupated in the summer, and to spend time doing something actually useful.
At first we wanted to make it wireless, but it turned out that is INSANELY hard, and we ran out of time. So now R2-D2 operates tethered with a USB cable.

**What does this project do, and how to use it?**
  It is really simple:
  * You flash MycroPython onto the Raspberry Pi Pico W from the official site, download Thonny IDE on your PC, and upload the code you find here, in the *firmware* folder
  * You plug the USB cable hanging from the bottom of the robot into your PC,
  * You open the code (which is already uploaded on the Pico) in Thonny, and hit RUN
  * You type w, a, s, d, q, e, z, and x from your keyboard into the Shell.
  * w means forward, s means backwards, q turns the head one way, e turns it the other way. x stops the head, z stops the wheels. With a you turn left, and with d        you turn right
  * Also dont forget to turn the robot on with the switch hanging from the bottom (there are two holes at the bottom, one for the switch, the other for the USB),         otherwise the wheels won't work ;)
  * The batteries need to be removed for charging
  * The robot is capable of rolling forward and backwards, turning left and right, and rotating it's head. It also has a red and blue (red means low battery, blue means ok) , green and yellow LED (they change color depending on head position).
<img width="3000" height="4000" alt="16084" src="https://github.com/user-attachments/assets/fe71236d-7b64-4017-b8a1-13e31619c399" />

**What have we learned?**

_Lászlóffy Tamás_: My role was the 3D modelling and the designing. I learned the Fusion 360 management, the use of bluprints, methods of 3D printing, and of course the consequences of my small mistakes which only came to light during assembly. Optimizing the tolerance, figuring out modelling maneuvers and loopholes (especially R2's Dome); these were the most complicated ones. Of course I had some headaches or rage-quit moments; however, I enjoyed the process.

_Benedek Kristóf_: My role was building the electronics, and coding. I've learned the basics of MicroPython, and understanding the basics of low-voltage, low-amperage DC circuits. I've had to learn soldering, understanding how the software communicates with hardware, and how to make the two understand each other. I've also learnt, that overengineering certain features just adds unnecessary complexity, and sometimes trying to make everything perfect at first is the one that causes the problems later on. Iáve also learnt the importance of time management, and communication between teammates.

# CAD
<img width="1080" height="642" alt="Stardance_projekt-R2D2_Torzo_2026-Oct-15_07-09-05PM-000_CustomizedView6091819401" src="https://github.com/user-attachments/assets/e6060817-586f-4951-82be-5a7c22913694" />
<img width="751" height="777" alt="Exploded view R2" src="https://github.com/user-attachments/assets/f3d893e5-8b03-4d8c-a9df-9b473e85089e" />

# Wiring Diagram

<img width="3318" height="2438" alt="20261015_204230" src="https://github.com/user-attachments/assets/aa56efc1-5adb-4941-ac0c-941398cf73df" />

# BOM

<img width="1277" height="688" alt="Képernyőfelvétel (66)" src="https://github.com/user-attachments/assets/cdbc52b0-7af2-44ee-864e-3fa1efe95619" />


**What have we changed?**
During the process we had to change some things (Because we overestimated our capabilities at the moment) Here's a list of them:
* We omitted the wireless feature due to a lack of time and skills (I'm planning to implement it in the future).
* We omitted the feature which would have shown the ip address with morse lights.
* We omitted the homing sequence for the head, because it works just fine without it, and it just adds unnecessary complexity.
* If the Pico operates with USB plugged in, then the buck converter I previously bought is useless too.
* We left out sound systems because of a lack of time.
* In our original plan, the V-groove was designed for airsoft BBs to imitate a lazy-susan; however during testing, it turned out that the 28BYJ-48 Stepper Motor couldn't handle the unbearable friction. As a result we removed the BBs because the mechanism turned smoother without them.

# Additional Note

If the feet are wiggling during assembly, you should duct tape it.

# Special Thanks

* To the Hack Club Admins for their guidance and help
* To the Hack Club members on Slack for their useful replies
* _Electro Nerds Academy_ YouTube Channel
* _Product Design Online_ YouTube Channel 
* _Wokwi’s Raspberry Pi Pico simulator_
* _Get Started with MicroPython on Raspberry Pi Pico_ PDF book
* **Astromech.net** for the impeccable blueprints
* ...and many more YouTube channels and videos
  
