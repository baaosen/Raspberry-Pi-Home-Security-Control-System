import json, time, os
from flask import Flask, render_template
import netifaces as ni

#camera1
ip_this = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
#camera2
ip_that;

#send 1 from serial to mbed, speaker play 1
cmd1 = '/home/pi/Documents/4180-proj/main.o'
#send 2 from serial to mbed, speaker play 2
cmd1 = '/home/pi/Documents/4180-proj/main.o'
#send 3 from serial to mbed, speaker play 3
cmd1 = '/home/pi/Documents/4180-proj/main.o'

print("Trying to connect to mbed...")
res = os.system(cmd)
time.sleep(1)
while (res == -1):
    print("Connection failed, reconnecting...")
    res = os.system(cmd)
    time.sleep(1)
print("Connection established")

app = Flask(__name__)


@app.route('/change angle')
def camera1():
    render_template('homesecurity.html',
                            html_server_ip=ip_that)

@app.route('/speaker1')
def speaker1():
    res = os.system(cmd)
    time.sleep(1)
    while (res == -1):
        res = os.system(cmd)
        time.sleep(1)
    return "OK"

# Main render
@app.route('/')
def index():
    f = open('/home/pi/Documents/4180-proj/weather.data', 'r');
    global pressure
    pressure = f.readline()
    global humidity
    humidity = f.readline()
    global temperature
    temperature = f.readline()
    global wind_speed
    wind_speed = f.readline()
    global wind_dir
    wind_dir = f.readline()
    global rain_size
    rain_size = f.readline()
    f.close()
    return  render_template('homesecurity.html',
                            ip1_to_render=ip_this,
                            ip2_to_render=ip_that)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
