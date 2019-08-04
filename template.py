#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: YONG HAO CHEN
Student Number: CHNYON001
Prac: Prac 1
Date: 04-08-2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time
from itertools import product
# Logic that you write
k = 0
l = [[0,1],[0,1],[0,1]]
m = list(product(*l))
def increment(channel):
	global k
	k +=1
	if k == 8:
		k=0
	GPIO.output(chan_list_output,m[k])
def decrement(channel):
	global k
	k -=1
	if k==-1:
		k=7
	GPIO.output(chan_list_output,m[k])
def main():
    time.sleep(0.001)


# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
	GPIO.setmode(GPIO.BCM)
	chan_list_output = [17,27,22]
	chan_list_input = [23,24]
	GPIO.setup(chan_list_output, GPIO.OUT)
	GPIO.output(chan_list_output, GPIO.LOW)
	GPIO.setup(chan_list_input, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
	GPIO.add_event_detect(23, GPIO.RISING, callback=increment,bouncetime=200)
	GPIO.add_event_detect(24, GPIO.RISING, callback=decrement, bouncetime=200)
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
