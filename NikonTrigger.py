import pyb
from pyb import Timer
from time import sleep

nikonCommand = [76, 1058, 15, 61, 15, 137, 15, 1078, 76, 1058, 15, 61, 15, 137, 15, 1078]


clock = 38.4e3
tim = pyb.Timer(9, freq=clock)
tchannel = tim.channel(1, Timer.PWM, pin=pyb.Pin.board.X3, pulse_width_percent=0)
T = 1/clock
def trigger():
	toggle = 1
	for i in nikonCommand:
		print(i)
		tchannel.pulse_width_percent(50*toggle)
		toggle ^= 1
		pyb.udelay(int(T*1e6*i))
	tchannel.pulse_width_percent(0)


sw = pyb.Switch()

while True:
	if sw():
		trigger()
	pyb.delay(50)
	