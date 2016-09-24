""
Robot Explorador
Universidad de los Andes
Copyleft (c) 2015 Marcelo A. Peña M (Marcelo.p@ula.ve)

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

  Written in Venezuela, Universidad de los Andes.
""



import socket 
import serial
import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

class Motor:

    def __init__(self, pinForward, pinBackward, pinControl):
        self.pinForward = pinForward
        self.pinBackward = pinBackward
        self.pinControl = pinControl
        GPIO.setup(self.pinForward, GPIO.OUT)
        GPIO.setup(self.pinBackward, GPIO.OUT)
        GPIO.setup(self.pinControl, GPIO.OUT)
        self.pwm_forward = GPIO.PWM(self.pinForward, 100)
        self.pwm_backward = GPIO.PWM(self.pinBackward, 100)
        self.pwm_forward.start(0)
        self.pwm_backward.start(0)
        GPIO.output(self.pinControl,GPIO.HIGH)

    def forward(self, speed):
        self.pwm_backward.ChangeDutyCycle(0)
        self.pwm_forward.ChangeDutyCycle(speed)

    def backward(self, speed):
        self.pwm_forward.ChangeDutyCycle(0)
        self.pwm_backward.ChangeDutyCycle(speed)

    def stop(self):
        self.pwm_forward.ChangeDutyCycle(0)
        self.pwm_backward.ChangeDutyCycle(0)

motor1 = Motor(11, 9, 17)
motor2 = Motor(10, 22, 17)

pwm = GPIO.PWM(18,50)
pwm.start(7.5)

serial=serial.Serial('/dev/ttyAMA0', 115200)

host = ''
port = 1976
backlog = 5

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)

try:
   while 1:
	serial.write("0")
	print "se espera una conexion"
	client, address = s.accept()
	print "conectado " + address[0] 
	while 1:
		data = client.recv(1)
		if data == '':
			break
		else:
                        print("Dato recivido ",data)
			if data == "1":
                          GPIO.output(17,GPIO.HIGH)
                          motor1.backward(100)
                          motor2.backward(100)
			elif data=="2":
			  GPIO.output(17,GPIO.LOW)
                          motor1.forward(100)
                          motor2.forward(100)
                        elif data=="4":
                          pwm.ChangeDutyCycle(6.5)
                        elif data=="8":
                          pwm.ChangeDutyCycle(8.5)
                        elif data=="0":
                          motor1.stop()
                          motor2.stop()
                          pwm.ChangeDutyCycle(7.5)
                       
                          
except KeyboardInterrupt:
    client.close()
    pwm.ChangeDutyCycle(7.5)
    time.sleep(1)        
    pwm.stop()                    
    GPIO.cleanup()
