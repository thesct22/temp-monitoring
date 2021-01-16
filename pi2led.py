import telnetlib
import sys

import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
 
# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)
 
# create the mcp object
mcp = MCP.MCP3008(spi, cs)
 
# create an analog input channel on pin 0 for temperature
tempchan = AnalogIn(mcp, MCP.P0)

# create an analog input channel on pin 1 for humidity
humchan = AnalogIn(mcp, MCP.P1)

#create a telnet object for given ip and port
tn = telnetlib.Telnet("ip.address.of.LEDboard","8080")

temp=0
hum=0

while 1:

    #read temp and humidity values
    temp=tempchan.value
    hum=humchan.value

    #calculation of values from channel values happen here
    
    #temp = ((temp * 330)/float(1023)) -50
    #hum = (hum * 100)/float(1023)
    
    #will fine tune once hardware is received

    tn.write("[01U1Y00FF0"+temp+" C\x0A"+hum+" %%XX]")
    time.sleep(20)