from xbee import XBee, ZigBee
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)

xbee = XBee(ser)
