import game from game # imports game class
import RPi.GPIO as GPIO
import time
#Serial Pins
SER = 25
SRCLK = 26
RCLK = 27

#Button Pins

bUp      = 5
bDown    = 6
bLeft    = 12
bRight   = 13
bForward = 16
bBack    = 19

#setup the pin mode for the GPIO 

GPIO.setmode(GPIO.BCM)

#turn off the warnings

GPIO.setwarnings(False)

#setup the buttons

GPIO.setup(bUp     , GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(bDown   , GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(bLeft   , GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(bRight  , GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(bForward, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(bBack   , GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

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

def updateOut(gameOb): # send changes to LED matrix
    nums = gameop.matrix()
    colors = np.zeros((4,4,4,3))
    state = gameOb.isWon()
    
    for i in range (0,4): # For each level
        for j in range (0,4): # Row
            for k in range (0,4): # Colomn
            if nums.at(i,j,k) == 2 or nums.at(i,j,k) == 16 or nums.at(i,j,k) == 32: #enable red
                colors.at(i,j,k,0) = 1
            if nums.at(i,j,k) == 4 or nums.at(i,j,k) == 16 or nums.at(i,j,k) == 64: #enable green
                colors.at(i,j,k,1) = 1
            if nums.at(i,j,k) == 8 or nums.at(i,j,k) == 32 or nums.at(i,j,k) == 64: #enable blue
                colors.at(i,j,k,2) = 1
    
    GPIO.output(RCLK, 0) # enable serail stream to registers
    
    for c in range(0,3): # for each of 3 colors (Red then green then blue)
        for k in range (0,4): # For each level
            for i in range (0,4): # Row
                for j in range (0,4): # Colomn
                    #begin data shift out;
                    GPIO.output(SER, colors[i][j][k][c])
                    GPIO.output(SRCLK,1)
                    time.sleep(.0005) #Pi Clock speed is too high for registers
                    GPIO.output(SRCLK,0)
    
    #Clock Register. This latches the current state of the serial buffer to the output
    #register, updating the cube;
    GPIO.output(RCLK, 1)
    return state # Used to end game

fris = game() #intailize a game object

#Set Interupts for buttons. Starting with translations
GPIO.add_event_detect(bUp     , GPIO.RISING, callback = fris.up_movement()      , bouncetime = 25)
GPIO.add_event_detect(bDown   , GPIO.RISING, callback = fris.down_movement()    , bouncetime = 25)
GPIO.add_event_detect(bLeft   , GPIO.RISING, callback = fris.left_movement()    , bouncetime = 25)
GPIO.add_event_detect(bRight  , GPIO.RISING, callback = fris.right_movement()   , bouncetime = 25)
GPIO.add_event_detect(bForward, GPIO.RISING, callback = fris.forward_movement() , bouncetime = 25)
GPIO.add_event_detect(bBack   , GPIO.RISING, callback = fris.backward_movement(), bouncetime = 25)

#Check for win and update board with new random pieces
GPIO.add_event_detect(bUp     , GPIO.FALLING, callback = updateOut(fris), bouncetime = 25)
GPIO.add_event_detect(bDown   , GPIO.FALLING, callback = updateOut(fris), bouncetime = 25)
GPIO.add_event_detect(bLeft   , GPIO.FALLING, callback = updateOut(fris), bouncetime = 25)
GPIO.add_event_detect(bRight  , GPIO.FALLING, callback = updateOut(fris), bouncetime = 25)
GPIO.add_event_detect(bForward, GPIO.FALLING, callback = updateOut(fris), bouncetime = 25)
GPIO.add_event_detect(bBack   , GPIO.FALLING, callback = updateOut(fris), bouncetime = 25)

textPlay = input("Enable text game? (y/n) ") #Taking user input for the movement choice

while(1): # main game loop
    if (textPlay == 'y' or textPlay == 'Y' )
        fris.printBoard() # prints the current game board to terminal (Debug / if you don't have an LED Cube)
        movement_choice = input("Make your move::::>>>>    ") #Taking user input for the movement choice
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
        if (updateOut(fris)):
            break
    else:
        movement_choice = input("Press enter to show current board: ")
        fris.printBoard()