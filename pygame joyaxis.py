import pygame
from time import sleep

pygame.init() 
pygame.joystick.init()
colck=pygame.time.Clock()
joystick=pygame.joystick.Joystick(0)
try:
	joystick = pygame.joystick.Joystick(0) 
	joystick.init() # init instance
	print ("Enabled joystick: {0}".format(joystick.get_name()))
except pygame.error:
	print ("no joystick found.")
     
while  True:
  colck.tick(30)
   # For each joystick:
 
  for event in pygame.event.get(): 
      if event.type == pygame.JOYAXISMOTION:
        print('')
      if event.type == pygame.JOYBALLMOTION:
        print('')
      if event.type == pygame.JOYHATMOTION:
        print('')
      if event.type == pygame.JOYBUTTONDOWN:
        print('')
      if event.type == pygame.JOYBUTTONUP:
        print('')

      if joystick.get_axis(0) >= 0.5:
        print ("right ") 
      if joystick.get_axis(0) <= -1:
        print("left")
      if joystick.get_axis(1) <= -1:
        print("forward")     
      if joystick.get_axis(1) >= 0.5:
        print("revrese")
      if joystick.get_axis(2) <= -1:
        print("up")
      if joystick.get_axis(2) >= 0.5:
        print("down")
      if joystick.get_axis(3) >= 0.5:
        print ("right") 
      if joystick.get_axis(3) <= -1:
        print("left")
        
      if joystick. get_button ( 0 ):
        print("zero")
      if joystick. get_button ( 1 ):
        print("one")

      if joystick. get_button ( 2 ):
        print("two")
      if joystick. get_button ( 3 ):
        print("three")
      if joystick. get_button ( 4 ):
        print("four")
      if joystick. get_button ( 5 ):
        print("five")
      if joystick. get_button ( 6 ):
        print("six")
      if joystick. get_button ( 7):
        print("10")
      if joystick. get_button ( 11 ):
        print("11")          
pygame.quit()