import json, time, os
from flask import Flask, render_template
import netifaces as ni
import serial
#camera1
ip_this = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
#camera2
ip_that = u"143.215.97.174"

#send 1 from serial to mbed, speaker play 1
#cmd1 = '~/Desktop/object_files/send1.o'
#send 2 from serial to mbed, speaker play 2
#cmd2 = '~/Desktop/object_files/send2.o'
#send 3 from serial to mbed, speaker play 3
#cmd3 = '~/Desktop/object_files/send3.o'
#send 4 from serial to mbed, light LED
#cmd4 = '~/Desktop/object_files/send4.o'

ser = serial.Serial('/dev/ttyACM0', 9600)

print("Trying to connect to mbed...")
#res = os.system(cmd4)
ser.write('4')
time.sleep(1)

while (ser.read(1) != '4'):
    print("Connection failed, reconnecting...")
    ser.write('4')
    time.sleep(1)
print("Connection established")

app = Flask(__name__)

@app.route('/speaker1')
def speaker1():
    ser.write('1')
    time.sleep(0.7)
    while (ser.read(1) != '1'):
        ser.write('1')
        time.sleep(0.7)
    return "OK"

@app.route('/speaker2')
def speaker2():
    ser.write('2')
    time.sleep(0.7)
    while (ser.read(1) != '2'):
        ser.write('2')
        time.sleep(0.7)
    return "OK"

@app.route('/speaker3')
def speaker3():
    ser.write('3')
    time.sleep(0.7)
    while (ser.read(1) != '3'):
        ser.write('3')
        time.sleep(0.7)
    return "OK"

@app.route('/ledlight')
def ledlight():
    ser.write('5')
    time.sleep(0.7)
    while (ser.read(1) != '5'):
        ser.write('5')
        time.sleep(0.7)
    return "OK"


# Main render
@app.route('/')
def index():
    return  render_template('homesecurity.html',
                            ip1_to_render=ip_this,
                            ip2_to_render=ip_that)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
