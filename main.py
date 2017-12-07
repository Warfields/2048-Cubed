#import game
import game
import RPi.GPIO as GPIO
import time
#Serial Pins
SER = 25
SRCLK = 26
RCLK = 27

#Button Pins

bUp = 5
bDown = 6
bLeft = 12
bRight = 13
bForward = 16
bBack = 19


#setup the pin mode for the GPIO 

GPIO.setmode(GPIO.BCM)

#turn off the warnings

GPIO.setwarnings(False)

#setup the buttons

GPIO.setup(bUp, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(bDown, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(bLeft, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(bRight, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(bForward, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(bBack, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#setup the serial lines

GPIO.setup(SER, GPIO.OUT)
GPIO.setup(SRCLK, GPIO.OUT)
GPIO.setup(RCLK, GPIO.OUT)

#Clock Shift Registers to intialize them

GPIO.output(SRCLK,1)
GPIO.output(SER,1)
GPIO.output(RCLK,1)
time.sleep(.0005)
GPIO.output(SRCLK,0)
GPIO.output(SER,0)
GPIO.output(RCLK,0)

fris = game() #intailize a game object

def updateOut(matrix): # send changes to LED matrix
    #TODO GENERATE COLOR SCHEME
    GPIO.output(RCLK, 0) # enable serail stream to registers

    for c in range(0,3): # for each of 3 colors (Red then green then blue)
        for k in range (0,4): # For each level
            for i in range (0,4): # Row
                for j in range (0,4): # Colomn
                    #begin data shift out; TODO: Finish this code
                    loop += 1
                    GPIO.output(SRCLK,1)
                    time.sleep(.0005)
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

    #Clock Register. This latches the current state of the serial buffer to the output
    #register, updating the cube;
    GPIO.output(RCLK, 1)

while(not (fris.isWon())): # main game loop
    fris.printBoard() # prints the current game board to terminal (Debug / if you don't have an LED Cube)
    movement_choice = input("Make your move::::>>>>    ") #Taking user input for the movement choice
    #TODO update If statements
    if movement_choice == "w":
        fris.up_movement()
    elif movement_choice == "s":
        fris.down_movement()
    elif movement_choice == "a":
        fris.left_movement()
    elif movement_choice == "d":
        fris.right_movement()
    elif movement_choice == ",":
        fris.forward_movement()
    elif movement_choice == '.':
        fris.backward_movement()
    #update cube
    updateOut(fris.matrix())