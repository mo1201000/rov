import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)



pwm1 = 	7			
dir1 = 	11			
pwm2 = 	12			
dir2 = 13
			
pwm3 =15 				
dir3 = 16	
			
pwm4 = 18				
dir4 = 22

motorpwm1=40
motorpwm2=37

motorpwm3=38
motorpwm4=29

motorpwm5=31
motorpwm6=32

motorpwm7=33
motorpwm8=36





GPIO.setup(dir1,GPIO.OUT)  
GPIO.setup(pwm1,GPIO.OUT)
GPIO.setup(dir2,GPIO.OUT)
GPIO.setup(pwm2,GPIO.OUT)
GPIO.setup(dir3,GPIO.OUT)  
GPIO.setup(pwm3,GPIO.OUT)
GPIO.setup(dir4,GPIO.OUT)
GPIO.setup(pwm4,GPIO.OUT)
GPIO.setup(motorpwm1,GPIO.OUT)
GPIO.setup(motorpwm2 ,GPIO.OUT)
GPIO.setup(motorpwm3,GPIO.OUT)
GPIO.setup(motorpwm4,GPIO.OUT)
GPIO.setup(motorpwm5,GPIO.OUT)
GPIO.setup(motorpwm6 ,GPIO.OUT)
GPIO.setup(motorpwm7,GPIO.OUT)
GPIO.setup(motorpwm8,GPIO.OUT)

p1 = GPIO.PWM( pwm1, 100)			
p2 = GPIO.PWM(pwm2, 100)
p3 = GPIO.PWM(pwm3, 100)			
p4 = GPIO.PWM(pwm4, 100)

p5=GPIO.PWM(motorpwm1, 100)
p6=GPIO.PWM(motorpwm2, 100)
p7=GPIO.PWM(motorpwm3, 100)
p8=GPIO.PWM(motorpwm4, 100)
p9=GPIO.PWM(motorpwm5, 100)
p10=GPIO.PWM(motorpwm6,100)
p11=GPIO.PWM(motorpwm7,100)
p12=GPIO.PWM(motorpwm8,100)


while  True:
        GPIO.output(motorpwm1, GPIO.LOW)          
        GPIO.output(motorpwm3, GPIO.LOW)
        GPIO.output(motorpwm5, GPIO.LOW)          
        GPIO.output(motorpwm7, GPIO.LOW)
        for i in range (0,100,1):
            p6.ChangeDutyCycle(.85*i)
            p8.ChangeDutyCycle(.85*i)
            p10.ChangeDutyCycle(.85*i)
            p12.ChangeDutyCycle(.85*i)

        sleep(4)
        GPIO.output(motorpwm1, GPIO.LOW)          
        GPIO.output(motorpwm3, GPIO.LOW)
        GPIO.output(motorpwm5, GPIO.LOW)          
        GPIO.output(motorpwm7, GPIO.LOW)
        GPIO.output(dir1, GPIO.LOW)          
        GPIO.output(dir2, GPIO.LOW) 
        GPIO.output(dir3, GPIO.LOW)          
        GPIO.output(dir4, GPIO.LOW)          
        for i in range (0,100,1):
            p6.ChangeDutyCycle(.85*i)
            p8.ChangeDutyCycle(.85*i)
            p10.ChangeDutyCycle(.85*i)
            p12.ChangeDutyCycle(.85*i)

        p1.start(90)                       
        p2.start(90) 
        p3.start(90)                       
        p4.start(90)  
        sleep(4)
        GPIO.output(motorpwm1, GPIO.LOW)          
        GPIO.output(motorpwm3, GPIO.LOW)
        GPIO.output(motorpwm5, GPIO.LOW)          
        GPIO.output(motorpwm7, GPIO.LOW)
        GPIO.output(dir1, GPIO.HIGH)          
        GPIO.output(dir2, GPIO.HIGH) 
        GPIO.output(dir3, GPIO.HIGH)          
        GPIO.output(dir4, GPIO.HIGH)          
        for i in range (0,100,1):
            p6.ChangeDutyCycle(.85*i)
            p8.ChangeDutyCycle(.85*i)
            p10.ChangeDutyCycle(.85*i)
            p12.ChangeDutyCycle(.85*i)

        p1.start(10)                       
        p2.start(10) 
        p3.start(10)                       
        p4.start(10)  
        sleep(4)
        GPIO.output(motorpwm1, GPIO.LOW)          
        GPIO.output(motorpwm3, GPIO.LOW)
        GPIO.output(motorpwm5, GPIO.LOW)          
        GPIO.output(motorpwm7, GPIO.LOW)
        GPIO.output(dir1, GPIO.HIGH) 
        GPIO.output(dir2, GPIO.HIGH)
        GPIO.output(dir3, GPIO.LOW) 
        GPIO.output(dir4, GPIO.LOW)  
        for i in range (0,100,1):
            p6.ChangeDutyCycle(.85*i)
            p8.ChangeDutyCycle(.85*i)
            p10.ChangeDutyCycle(.85*i)
            p12.ChangeDutyCycle(.85*i)
        p1.start(20)                       
        p2.start(20) 
        p3.start(70)                       
        p4.start(70) 
        sleep(4)
        GPIO.output(motorpwm1, GPIO.LOW)          
        GPIO.output(motorpwm3, GPIO.LOW)
        GPIO.output(motorpwm5, GPIO.LOW)          
        GPIO.output(motorpwm7, GPIO.LOW)
        GPIO.output(dir1, GPIO.LOW) 
        GPIO.output(dir2, GPIO.LOW)
        GPIO.output(dir3, GPIO.HIGH) 
        GPIO.output(dir4, GPIO.HIGH)  
        for i in range (0,100,1):
            p6.ChangeDutyCycle(.85*i)
            p8.ChangeDutyCycle(.85*i)
            p10.ChangeDutyCycle(.85*i)
            p12.ChangeDutyCycle(.85*i)
        p1.start(90)                       
        p2.start(90) 
        p3.start(10)                       
        p4.start(10) 
        sleep(4)
        GPIO.output(dir1, GPIO.LOW)          
        GPIO.output(dir2, GPIO.LOW) 
        GPIO.output(dir3, GPIO.LOW)          
        GPIO.output(dir4, GPIO.LOW)    
        p1.start(0)                       
        p2.start(0) 
        p3.start(0)                       
        p4.start(0) 
        GPIO.output(motorpwm2, GPIO.LOW)          
        GPIO.output(motorpwm4, GPIO.LOW)
        GPIO.output(motorpwm6, GPIO.LOW)          
        GPIO.output(motorpwm8, GPIO.LOW)
        for i in range (0,100,1):
            p5.ChangeDutyCycle(.85*i)
            p7.ChangeDutyCycle(.85*i)
            p9.ChangeDutyCycle(.85*i)
            p11.ChangeDutyCycle(.85*i)
        sleep(4)

        GPIO.output(motorpwm2, GPIO.LOW)          
        GPIO.output(motorpwm4, GPIO.LOW)
        GPIO.output(motorpwm6, GPIO.LOW)          
        GPIO.output(motorpwm8, GPIO.LOW)
        
        GPIO.output(dir1, GPIO.LOW)          
        GPIO.output(dir2, GPIO.LOW) 
        GPIO.output(dir3, GPIO.LOW)          
        GPIO.output(dir4, GPIO.LOW)          
        p1.start(90)                       
        p2.start(90) 
        p3.start(90)                       
        p4.start(90)   
        for i in range (0,100,1):
            p5.ChangeDutyCycle(.85*i)
            p7.ChangeDutyCycle(.85*i)
            p9.ChangeDutyCycle(.85*i)
            p11.ChangeDutyCycle(.85*i)
        sleep(4)
        GPIO.output(dir1, GPIO.HIGH)          
        GPIO.output(dir2, GPIO.HIGH)
        GPIO.output(dir3, GPIO.HIGH)          
        GPIO.output(dir4, GPIO.HIGH)  
        GPIO.output(motorpwm2, GPIO.LOW)          
        GPIO.output(motorpwm4, GPIO.LOW)
        GPIO.output(motorpwm6, GPIO.LOW)          
        GPIO.output(motorpwm8, GPIO.LOW)
                
        p1.start(20)                       
        p2.start(20) 
        p3.start(20)                       
        p4.start(20) 
        for i in range (0,100,1):
            p5.ChangeDutyCycle(.85*i)
            p7.ChangeDutyCycle(.85*i)
            p9.ChangeDutyCycle(.85*i)
            p11.ChangeDutyCycle(.85*i)
        sleep(4)   
        GPIO.output(dir1, GPIO.HIGH) 
        GPIO.output(dir2, GPIO.HIGH)
        GPIO.output(dir3, GPIO.LOW) 
        GPIO.output(dir4, GPIO.LOW)  
        GPIO.output(motorpwm2, GPIO.LOW)          
        GPIO.output(motorpwm4, GPIO.LOW)
        GPIO.output(motorpwm6, GPIO.LOW)          
        GPIO.output(motorpwm8, GPIO.LOW)
        p1.start(20)                       
        p2.start(20) 
        p3.start(90)                       
        p4.start(90) 
        for i in range (0,100,1):
            p5.ChangeDutyCycle(.85*i)
            p7.ChangeDutyCycle(.85*i)
            p9.ChangeDutyCycle(.85*i)
            p11.ChangeDutyCycle(.85*i)
        sleep(4)
        GPIO.output(motorpwm2, GPIO.LOW)          
        GPIO.output(motorpwm4, GPIO.LOW)
        GPIO.output(motorpwm6, GPIO.LOW)          
        GPIO.output(motorpwm8, GPIO.LOW)
        GPIO.output(dir1, GPIO.LOW)
        GPIO.output(dir2, GPIO.LOW) 
        GPIO.output(dir3, GPIO.HIGH)  
        GPIO.output(dir4, GPIO.HIGH)
        p1.start(90)                       
        p2.start(90) 
        p3.start(10)                       
        p4.start(10)
        for i in range (0,100,1):
            p5.ChangeDutyCycle(.85*i)
            p7.ChangeDutyCycle(.85*i)
            p9.ChangeDutyCycle(.85*i)
            p11.ChangeDutyCycle(.85*i)
        sleep(4)
	     
        GPIO.output(dir1, GPIO.LOW)
        GPIO.output(dir2, GPIO.LOW) 
        GPIO.output(dir3, GPIO.LOW)  
        GPIO.output(dir4, GPIO.LOW)
        p1.start(0)                       
        p2.start(0) 
        p3.start(0)                       
        p4.start(0)
        
    
    