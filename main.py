#import game
from game import game
import RPi.GPIO as GPIO
#import serial

SER = 25
SRCLK = 26
RCLK = 27
#outputEn = 27 

#setup the pin mode for the GPIO 

GPIO.setmode(GPIO.BCM)

#turn off the warnings, this is optional

GPIO.setwarnings(False)

#setup the buttons

#GPIO.setup(ReedPin, GPIO.IN, GPIO.PUD_UP)

#setup the serial lines

GPIO.setup(SER, GPIO.OUT)
GPIO.setup(SRCLK, GPIO.OUT)
GPIO.setup(RCLK, GPIO.OUT)

GPIO.output(SRCLK,1)
GPIO.output(SER,1)
GPIO.output(RCLK,1)
GPIO.output(SRCLK,0)
GPIO.output(SER,0)
GPIO.output(RCLK,0)

fris = game()

#def serialOut

def updateOut(matrix):
    #Pick Color
    GPIO.output(SER,1)
    #Shift out data
    loop = 0
    for c in range(0,3): # for each of 3 colors
        for k in range (0,4): # go up the individual levels
            for i in range (0,4): # Row
                for j in range (0,4): # Colomn
                    loop+=1
                    GPIO.output(SRCLK,1)
                    GPIO.output(SRCLK,0)
                    if c == 0 & (0):
                        print "1"

                        
                        #Output Red
                    if c == 1:
                        print 2
                        #Green
                    if c == 2:
                        #Blue
                        print 3

    #Clock Register
    GPIO.output(RCLK, 1)
    GPIO.output(RCLK, 0)
    
    #isldfkjgdfhkjgsdj

while(not (fris.isWon())):
    fris.printBoard()
    movement_choice = raw_input("Make your move::::>>>>    ") #Taking user input for the movement choice
    if movement_choice == "w":
        fris.up_movement()
        #fris.up_addition()
    elif movement_choice == "s":
        fris.down_movement()
        #fris.down_addition()
    elif movement_choice == "a":
        fris.left_movement()
        #ris.left_addition()
    elif movement_choice == "d":
        fris.right_movement()
       # fris.right_addition()
    elif movement_choice == ",":
        fris.forward_movement()
     #   fris.forward_addition()
    elif movement_choice == '.':
        fris.backward_movement()
       # fris.backward_addition()
    updateOut(fris.matrix())
    fris.isWon()
