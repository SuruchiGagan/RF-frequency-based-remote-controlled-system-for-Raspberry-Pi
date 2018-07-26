import RPi.GPIO as GPIO
import time
import Adafruit_DHT

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

TRIG = 11
ECHO = 12
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.output(3,1)
GPIO.output(5,1)
GPIO.output(7,1)
GPIO.output(8,1)
GPIO.output(13,1)
GPIO.output(16,1)
GPIO.cleanup(15)

GPIO.setup(38,GPIO.IN)
GPIO.setup(40,GPIO.IN)
GPIO.setup(35,GPIO.IN)
GPIO.setup(37,GPIO.IN)
t1=0.0
t2=100.0
h1=0.0
h2=100.0
e=1
d=0
while True:
 try: 
   if GPIO.input(40) == 0:
     print "///////////////////////////////-Obstacle Sensor Start-///////////////////////////////////"
     print " "
     while True:


         GPIO.setup(TRIG,GPIO.OUT)
         GPIO.output(TRIG,0)

         GPIO.setup(ECHO,GPIO.IN)

         time.sleep(0.1)


         GPIO.output(TRIG,1)
         time.sleep(0.00001)
         GPIO.output(TRIG,0)

         while GPIO.input(ECHO) == 0:
               pass
         start = time.time()

         while GPIO.input(ECHO) == 1:
          pass

         stop = time.time()

         diff = stop-start

         x1= diff*17000
         
         GPIO.output(TRIG,1)
         time.sleep(0.00001)
         GPIO.output(TRIG,0)

         while GPIO.input(ECHO) == 0:
               pass
         start = time.time()

         while GPIO.input(ECHO) == 1:
          pass

         stop = time.time()

         diff = stop-start

         x2= diff*17000
         
         x=(x1+x2)/2
         GPIO.setup(3,GPIO.OUT)
         GPIO.setup(5,GPIO.OUT)
         GPIO.setup(7,GPIO.OUT)
	 GPIO.setup(8,GPIO.OUT)
	 GPIO.setup(13,GPIO.OUT)
	 GPIO.setup(16,GPIO.OUT)
         GPIO.setup(15,GPIO.OUT)
         GPIO.setup(38,GPIO.IN)
         GPIO.setup(40,GPIO.IN)

         while (x>200):
               GPIO.output(3,0)
               GPIO.output(5,0)
               GPIO.output(7,0)
               GPIO.output(8,0)
               GPIO.output(13,0)
               GPIO.output(16,1)
               GPIO.cleanup(15)
               print("The obstacle is very very far at a distance =",x,"cms")
               break 
         while (x<200 and x>=150):
               GPIO.output(3,1)
               GPIO.output(5,0)
               GPIO.output(7,0)
               GPIO.output(8,0)
               GPIO.output(13,0)
               GPIO.output(16,0)
               GPIO.cleanup(15)
               print("The obstacle is very far at a distance =",x,"cms")
               break        
         while (x<150 and x>=100):
               GPIO.output(3,1)
               GPIO.output(5,1)
               GPIO.output(7,0)
               GPIO.output(8,0)
               GPIO.output(13,0)
               GPIO.output(16,0)
               GPIO.cleanup(15)
               print("The obstacle is very far at a distance =",x,"cms")
               break
         while (x<100 and x>=75):
               GPIO.output(3,1)
               GPIO.output(5,1)
               GPIO.output(7,1)
               GPIO.output(8,0)
               GPIO.output(13,0)
               GPIO.output(16,0)
               GPIO.output(15,1)
               print("The obstacle is far at a distance =",x,"cms")
               break
         while (x<75 and x>=50):
               GPIO.output(3,1)
               GPIO.output(5,1)
               GPIO.output(7,1)
               GPIO.output(8,1)
               GPIO.output(13,0)
               GPIO.output(16,0)
               GPIO.output(15,1)
               print("The obstacle is coming closer and is at a distance =",x,"cms")
               break
         while (x<50 and x>=25):
               GPIO.output(3,1)
               GPIO.output(5,1)
               GPIO.output(7,1)
               GPIO.output(8,1)
               GPIO.output(13,1)
               GPIO.output(16,0)
               GPIO.output(15,1)
               print("The obstacle is very close at a distance =",x,"cms")
               break
         while (x<25):
               GPIO.output(3,1)
               GPIO.output(5,1)
               GPIO.output(7,1)
               GPIO.output(8,1)
               GPIO.output(13,1)
               GPIO.output(16,1)
               GPIO.output(15,0)
               print("!!!! WARNING!!!! the obstacle is about to collide and is at a distance =",x,"cms")
               break
         if GPIO.input(37) == 0:
	       d=1
	 if d == 1:
               print "/////////////////-Obstacle & Humidity & Temperature Sensors Start Together-/////////////////"
               print " "
               humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 16)
               if humidity is not None and temperature is not None:
                  humidity = round(humidity, 2)
                  temperature = round(temperature, 2)
                  e=0
                  print 'Temperature = {0:0.1f}*C Humidity = {1:0.1f}%'.format(temperature, humidity)
               else:
                  e=0
                  print 'Can not connect to te sensor!'
               if GPIO.input(35) == 0:
		  print "////////////////////-Only Humidity & Temperature Sensor is Turned Off-////////////////////"
                  print " " 
		  d = 0
                  e = 1       
         if GPIO.input(38) == 0:
	       if e == 1:
		  print "////////////////////////////-Obstacle Sensor Stopped-/////////////////////////////////////"
                  print " "
	       else:
		  print "///////////////-Both Obstacle & (Humidity & Temperature) Sensor Stopped-//////////////////"
                  print " "
               GPIO.cleanup(3)
               GPIO.cleanup(5)
               GPIO.cleanup(7)
               GPIO.cleanup(8)
               GPIO.cleanup(13)
               GPIO.cleanup(15)
               GPIO.cleanup(16)
               break
         
   if GPIO.input(37) == 0:
         GPIO.setup(15,GPIO.OUT)
         print "/////////////////////////-Humidity & Temperature Sensor Start-////////////////////////////"
         print " "
         c=1
	 while c == 1:
           GPIO.output(15,1)
	   humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 16)
           if humidity is not None and temperature is not None:
             if temperature>t1:
                t1=temperature
             if t2>temperature:
                t2=temperature
             if humidity>h1:
                h1=humidity
             if h2>humidity:
                h2=humidity
             humidity = round(humidity, 2)
             temperature = round(temperature, 2)
           
             print 'Temperature = {0:0.1f}*C Humidity = {1:0.1f}%'.format(temperature, humidity)
           else:
             print 'Can not connect to te sensor!'
	   if GPIO.input(35) == 0:
	      print "Highest temperature",t1,"*C"
              print "Lowest temperature",t2,"*C"
              print "Highest humidity",h1,"%"
              print "Lowest humidity",h2,"%"
              print '/////////////////////////////////////-Humidity & Temperature Sensor Stop-///////////////////////////////'
              GPIO.cleanup(15) 
              c=0
	   
 except KeyboardInterrupt:
        
        GPIO.output(3,0)
        GPIO.output(5,0)
        GPIO.output(7,0)
        GPIO.output(8,0)
        GPIO.output(13,0)
        GPIO.output(16,0)
        GPIO.cleanup(15)

        exit()
