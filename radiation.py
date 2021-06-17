# ------------__ Hacking STEM – radiation.py – micro:bit __-----------
#  This project is for use with the EM spectrum lesson plan 
#  available from Microsoft Education Workshop at 
#  https://aka.ms/EMspectrum
#  http://aka.ms/hackingSTEM
#
#  Overview: This sketch uses LEDs as light sensors (photodiodes) to 
#   detect and measure different wavelengths in various types of 
#   light sources.
#
#  Pin Connections:
#   Pin 0: IR LED
#   Pin 1: Red LED
#   Pin 2: Green LED
#   Pin 3: Blue LED
#   Pin 4: UV LED
#
#  This project uses a BBC micro:bit microcontroller, information at:
#  https://microbit.org/
#
#  Comments, contributions, suggestions, bug reports, and feature
#  requests are welcome!
#  https://github.com/microsoft/hackingstem-nasa-radiation-microbit
#
#  Copyright 2019, Jen Fox
#  Microsoft EDU Workshop - HackingSTEM
#  MIT License terms detailed in LICENSE.txt
# ===---------------------------------------------------------------===

from microbit import *

#Define program variables
# These constants are the pins used on the micro:bit for the sensors 
LED_SENSOR_PIN1 = pin0
LED_SENSOR_PIN2 = pin1
LED_SENSOR_PIN3 = pin2
LED_SENSOR_PIN4 = pin3
LED_SENSOR_PIN5 = pin4

# Setup & Config
display.off()  # Turns off LEDs to free up additional input pins
#Turn off all micro:Bit analog pins being used as inputs
LED_SENSOR_PIN4.write_digital(0)
LED_SENSOR_PIN5.write_digital(0)

uart.init(baudrate=9600)  # Sets serial baud rate
DATA_RATE = 10 # Frequency of code looping
EOL = '\n' # End of Line Character

# This function reads voltage of from each pin attached to an LED  sensor 
def process_sensors():
    #declare the LED  sensor variables 
    global light_sensor_1, light_sensor_2, light_sensor_3, light_sensor_4, light_sensor_5 

    #read analog voltage!
    light_sensor_1 = LED_SENSOR_PIN1.read_analog()
    light_sensor_2 = LED_SENSOR_PIN2.read_analog()
    light_sensor_3 = LED_SENSOR_PIN3.read_analog()
    light_sensor_4 = LED_SENSOR_PIN4.read_analog()
    light_sensor_5 = LED_SENSOR_PIN5.read_analog()


#=============================================================================#
#------------------------------Main Program Loop------------------------------#
#=============================================================================#

while (True):
    process_sensors()
    #uart is the micro:bit command for serial
    uart.write('{},{},{},{},{}'.format(light_sensor_1, light_sensor_2, 
    light_sensor_3, light_sensor_4, light_sensor_5)+EOL)

    sleep(DATA_RATE)
