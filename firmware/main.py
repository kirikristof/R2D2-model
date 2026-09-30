#import network
#import socket
import machine
import utime
#import secrets <--there used to be a secrets.py file containing wifi credentials, but now it is useless, since the robot is working with usb
#import gc
import sys
import select
'''
html = """ <!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>R2D2 controlling</title>

<style>
body {
    font-family: Arial;
    text-align: center;
    margin-top: 20px;
}

button {
    width: 100px;
    height: 55px;
    margin: 5px;
    font-size: 18px;
}

.stop {
    background: #ff5555;
}

h2 {
    margin-top: 30px;
}
</style>
</head>

<body>

<h2>Moving R2D2</h2>

<div>
    <button onclick="fetch('forward')">FORWARD</button>
</div>

<div>
    <button onclick="fetch('left')">LEFT</button>
    <button class="stop" onclick="fetch('stop')">STOP</button>
    <button onclick="fetch('right')">RIGHT</button>
</div>

<div>
    <button onclick="fetch('back')">BACK</button>
</div>


<h2>R2D2 Head</h2>

<div>
    <button onclick="fetch('qwerty')">LEFT</button>
    <button class="stop" onclick="fetch('megallj')">STOP</button>
    <button onclick="fetch('abcd')">RIGHT</button>
</div>


<script>
function send(command) {
    console.log(command);


      fetch('/' + command);
    
}
</script>

</body>
</html>

"""

"""
#rear large logic display, wlan indicator
l_l_red = machine.Pin(9, machine.Pin.OUT)
l_l_green = machine.Pin(10, machine.Pin.OUT)
# wifi
ssid = secrets.ssid
password = secrets.password
onboard_led = machine.Pin("LED", machine.Pin.OUT)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
while wlan.status() != 3:
    l_l_red.value(1)
if wlan.status() ==3:
    l_l_green.value(1)
    utime.sleep(2)
    l_l_green.value(0)
ip_address = wlan.ifconfig()[0]
addr = socket.getaddrinfo('0.0.0.0',80)[0][-1]
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(5)
s.setblocking(False)
#rear circular yellow/green light, the IP address indicator
r_c_yellow = machine.Pin(5, machine.Pin.OUT)#I will use yellow for dot/period to avoid confusion
r_c_green = machine.Pin(6, machine.Pin.OUT) 
morse_dictionary={'1':',----', #i am using ',' instead of '.' because there will be also '.' characters between numbers.
                  '2':',,---',
                  '3':',,,--',
                  '4':',,,,-',
                  '5':',,,,,',
                  '6':'-,,,,',
                  '7':'--,,,',
                  '8':'---,,',
                  '9':'----,',
                  '0':'-----',
                  '.':'.'}
for char in ip_address:
    if char in morse_dictionary:
        pattern = morse_dictionary[char]
        for symbol in pattern:
            if symbol == ',':
                r_c_green.value(1)
                utime.sleep(0.5)
                r_c_green.value(0)
                utime.sleep(0.2)
            elif symbol == '-':
                r_c_green.value(1)
                utime.sleep(1.2)
                r_c_green.value(0)
                utime.sleep(0.2)
            if symbol == '.':
                r_c_yellow.value(1)
                utime.sleep(0.5)
                r_c_yellow.value(0)
'''
# rear circular light. I called the leds again because messing with multi line strings always caused problems with testing
#when switching to wireless these two lines should be deleted, as the leds are defined above.
r_c_yellow = machine.Pin(5, machine.Pin.OUT)
r_c_green = machine.Pin(6, machine.Pin.OUT) 

#front circular red/blue light, indicating battery voltage
f_c_red = machine.Pin(7, machine.Pin.OUT)
f_c_blue = machine.Pin(8, machine.Pin.OUT)
#measuring batteries via ADC
voltage_divider = machine.ADC(0)#GP26
calculated_factor = 0.00027480221 #this is calculated by dividing the voltage of the battery pack measured with a multimeter, with the raw ADC value. This is kind of a constant for my exact setup
#homing sequence sensor
sensor = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)
#stby
stby = machine.Pin(15, machine.Pin.OUT)
# motor a
ain1 = machine.Pin(14, machine.Pin.OUT)
ain2 = machine.Pin(13, machine.Pin.OUT)
pwma = machine.PWM(12)
pwma.duty_u16(0)
pwma.freq(1000)
# motor b
bin1 = machine.Pin(17, machine.Pin.OUT)
bin2 = machine.Pin(18, machine.Pin.OUT)
pwmb = machine.PWM(19)
pwma.duty_u16(0)
pwmb.freq(1000)
#stepper motor for head
pin1 = machine.Pin(1, machine.Pin.OUT)
pin2 = machine.Pin(2, machine.Pin.OUT)
pin3 = machine.Pin(3, machine.Pin.OUT)
pin4 = machine.Pin(4, machine.Pin.OUT)
pins = [pin1, pin2, pin3, pin4]
fwd_sequence = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1],
]
back_sequence = [
    [0,0,0,1],
    [0,0,1,0],
    [0,1,0,0],
    [1,0,0,0],
]
motor_active = False
positive_direction = False
negative_direction = False
STEP_LIMIT = 10000  #TEMPORARY limit, further calculation required!!!!!!!!!!!!
position = 0
step_index = 0
# def homing_sequence():     homing sequence turned out to be quite useless in my setup, the cables are never in danger. they avoid the gears entirely.
#     global step_index, position 
#     while sensor.value() == 0:
#         for pin, val in zip(pins, fwd_sequence[step_index]):
#             pin.value(val)
#         step_index = (step_index + 1) % 4
#         position += 1
#         utime.sleep_ms(3)
#     if sensor.value() == 1:
#         for pin in pins:
#             pin.value(0)
#     while sensor.value() == 1:
#         for pin, val in zip(pins, fwd_sequence[step_index]):
#             pin.value(val)
#         step_index = (step_index + 1) % 4
#         position -= 1
#         utime.sleep_ms(3)
#     if sensor.value() == 0:
#         position = 10010 #a little over the limit
#     while position > 5000: #halfway, thus looking forward
#         for pin, val in zip(pins, back_sequence[step_index]):
#             pin.value(val)
#         step_index = (step_index + 1) % 4
#         position -= 1
#         utime.sleep_ms(3)
stby.value(0)
pwma.duty_u16(0)
pwmb.duty_u16(0)
ain1.value(0)
ain2.value(0)
bin1.value(0)
bin2.value(0)
#___________________________________
#homing_sequence()
ain1.value(0)
ain2.value(0)
pwma.duty_u16(0)
bin1.value(0)
bin2.value(0)
pwmb.duty_u16(0)
stby.value(1)
#_____________________________________
while True:
    #conn = None
    raw_ADC_value = voltage_divider.read_u16()
    true_voltage = raw_ADC_value*calculated_factor
    if true_voltage <= 6.8:
        f_c_red.value(1)

  #  try:
  #      conn, addr = s.accept()
  #      request = str(conn.recv(1024))
#
 #       if "GET / " in request or "GET /HTTP" in request:
 #           conn.send('HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n')
 #           conn.send(html)
 #       else:

    if select.select([sys.stdin], [], [], 0)[0]:
        command = sys.stdin.read(1).strip()
        #the line after this should be indented with one tab after the previous else: when switching to wireless, with all the lines after that indented accordingly
    #if "/forward" in request:
        if command == "a":
            pwma.duty_u16(0)
            pwmb.duty_u16(0)
            ain1.value(0)
            ain2.value(0)
            bin1.value(0)
            bin2.value(0)
            utime.sleep_ms(50) 
            pwma.duty_u16(46792)
            pwmb.duty_u16(46792)
            ain1.value(1)
            ain2.value(0)
            bin1.value(1)
            bin2.value(0)
        #elif "/back" in request:
        elif command == "d":
            pwma.duty_u16(0)
            pwmb.duty_u16(0)
            ain1.value(0)
            ain2.value(0)
            bin1.value(0)
            bin2.value(0)
            utime.sleep_ms(50) 
            pwma.duty_u16(46792)
            pwmb.duty_u16(46792)
            ain1.value(0)
            ain2.value(1)
            bin1.value(0)
            bin2.value(1)
        #elif "/left" in request:
        elif command == "s":
            pwma.duty_u16(0)
            pwmb.duty_u16(0)
            ain1.value(0)
            ain2.value(0)
            bin1.value(0)
            bin2.value(0) 
            utime.sleep_ms(50)
            pwma.duty_u16(46792)
            pwmb.duty_u16(46792)
            ain1.value(0)
            ain2.value(1)
            bin1.value(1)
            bin2.value(0)
        #elif "/right" in request:
        elif command == "w":
            pwma.duty_u16(0)
            pwmb.duty_u16(0)
            ain1.value(0)
            ain2.value(0)
            bin1.value(0)
            bin2.value(0)
            utime.sleep_ms(50)
            pwma.duty_u16(46792)
            pwmb.duty_u16(46792)
            ain1.value(1)
            ain2.value(0)
            bin1.value(0)
            bin2.value(1)
        #elif "/stop" in request:
        elif command == "z":
            #i'm using space for stop
            pwma.duty_u16(0)
            pwmb.duty_u16(0)
            ain1.value(0)
            ain2.value(0)
            bin1.value(0)
            bin2.value(0) 
        #elif "/qwerty" in request:
        elif command == "q":
            for pin in pins:
                pin.value(0)
            motor_active = True
            negative_direction = True
            positive_direction = False
       # elif "/abcd" in request:
        elif command == "e":
            for pin in pins:
                pin.value(0)
            position = 0
            motor_active = True
            negative_direction = False
            positive_direction = True
        #elif "/megallj" in request:
        elif command == "x":
            for pin in pins:
                pin.value(0)
            motor_active = False
    #conn.send('HTTP/1.0 204 No Content\r\n\r\n')
  #  except OSError:
  #      #you shall not
  #      pass
  #  finally:
  #      if conn:
  #          try:
  #              conn.close()
  #          except NameError:
  #              pass
  #          gc.collect()

    if motor_active:
        r_c_green.value(0)
        r_c_yellow.value(1)
        if positive_direction and position < STEP_LIMIT:
            for pin, val in zip(pins, fwd_sequence[step_index]):
                pin.value(val)
            step_index = (step_index + 1) % 4
            position += 1
            utime.sleep_ms(3)
        elif negative_direction and position > 0:
            for pin, val in zip(pins, back_sequence[step_index]):
                pin.value(val)
            step_index = (step_index + 1) % 4
            position -= 1
            utime.sleep_ms(3)
        else:
            r_c_yellow.value(0)
            r_c_green.value(1)
            
            motor_active = False
            for pin in pins:
                pin.value(0)
