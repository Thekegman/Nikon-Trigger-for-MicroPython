import pyb
from pyb import Timer
from time import sleep

nikonCommand = [76, 1058, 15, 61, 15, 137, 15, 1078, 76, 1058, 15, 61, 15, 137, 15, 1078]
red_led = pyb.LED(1)

clock = 38e3
tim = pyb.Timer(5, freq=clock)
tchannel = tim.channel(1, Timer.PWM, pin=pyb.Pin.board.X1, pulse_width_percent=0)
T = 1/clock

def trigger():
	toggle = 1
	for i in nikonCommand:
		tchannel.pulse_width_percent(50*toggle)
		toggle ^= 1
		pyb.udelay(int(T*1e6*i))
	tchannel.pulse_width_percent(0)


sw = pyb.Switch()

while not sw():
	pyb.delay(50)

frames = 10*24 # 10 seconds
shooting_time = 60*60 # 1hour
for i in range(frames):
	trigger()
	pyb.delay(int(1000*shooting_time/frames))
	
red_led.on()