# ------------__ Hacking STEM – radiation.py – micro:bit __-----------
#  Measuring Radiation for use with the NASA Radiation lesson plan 
#  lesson plan available from Microsoft Education Workshop at 
#  http://aka.ms/hackingSTEM
#
#  Overview: This sketch uses LEDs as light sensors (photodiodes) to detect and measure   
#  different wavelengths in various types of light sources.
#
#  This project uses a BBC micro:bit microcontroller, information at:
#  https://microbit.org/
#
#  Comments, contributions, suggestions, bug reports, and feature
#  requests are welcome! For source code and bug reports see:
#  http://github.com/[TODO github path to Hacking STEM]
#
#  Copyright 2019, Jen Fox
#  Microsoft EDU Workshop - HackingSTEM
#  MIT License terms detailed in LICENSE.txt
# ===---------------------------------------------------------------===

from microbit import *

# Setup & Config
display.off()  # Turns off LEDs to free up additional input pins
uart.init(baudrate=9600)  # Sets serial baud rate
DATA_RATE = 10 # Frequency of code looping
EOL = '\n' # End of Line Character

# These constants are the pins used on the micro:bit for the sensors 
LED_SENSOR_PIN1 = pin0
LED_SENSOR_PIN2 = pin1
LED_SENSOR_PIN3 = pin2
LED_SENSOR_PIN4 = pin3
LED_SENSOR_PIN5 = pin4
LED_SENSOR_PIN6 = pin10
    

def analog_off():
    #Function to turn all analog pins off
    LED_SENSOR_PIN4.write_digital(0)
    LED_SENSOR_PIN5.write_digital(0)
    LED_SENSOR_PIN6.write_digital(0)
    

def process_sensors():
    # This function reads voltage of from each pin attached to an LED  sensor 
    global light_sensor_1, light_sensor_2, light_sensor_3, light_sensor_4, light_sensor_5, light_sensor_6
    light_sensor_1 = LED_SENSOR_PIN1.read_analog()
    light_sensor_2 = LED_SENSOR_PIN2.read_analog()
    light_sensor_3 = LED_SENSOR_PIN3.read_analog()
    light_sensor_4 = LED_SENSOR_PIN4.read_analog()
    light_sensor_5 = LED_SENSOR_PIN5.read_analog()
    light_sensor_6 = LED_SENSOR_PIN6.read_analog()


#=============================================================================#
#---------------The Code Below Here is for Excel Communication----------------#
#=============================================================================#

# Array to hold the serial data
parsedData = [0] * 5

def getData():
    #   This function gets data from serial and builds it into a string
    global parsedData, builtString
    builtString = ""
    while uart.any() is True:
        byteIn = uart.read(1)
        if byteIn == b'\n':
            continue
        byteIn = str(byteIn)
        splitByte = byteIn.split("'")
        builtString += splitByte[1]
    parseData(builtString)
    return (parsedData)

def parseData(s):
    #   This function seperates the string into an array
    global parsedData
    if s != "":
        parsedData = s.split(",")

#=============================================================================#
#------------------------------Main Program Loop------------------------------#
#=============================================================================#
analog_off() #turn off analog output once

while (True):
    process_sensors()
    serial_in_data = getData()
    if (serial_in_data[0] != "#pause"):
        #uart is the micro:bit command for serial
        uart.write('{},{},{},{},{},{}'.format(light_sensor_1, light_sensor_2, light_sensor_3, light_sensor_4, light_sensor_5, light_sensor_6)+EOL)

    sleep(DATA_RATE)
