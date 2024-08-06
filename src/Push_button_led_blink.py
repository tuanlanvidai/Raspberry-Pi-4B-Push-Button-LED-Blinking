#Using RPIGPIO module for this project
import RPi.GPIO as GPIO

#Assign variable with GPIO PIN 17 and PIN 26
LED_PIN =17
BUTTON_PIN = 26

#Using BCM mode (use the name of GPIO pin rather than the PIN number 1-40 on Pi)
GPIO.setmode(GPIO.BCM)
#Setup channel for the variables. Led for output, Button for input.
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN)

while True:
    #If the button is pressed (1) then LED blink
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        GPIO.output(LED_PIN, GPIO.HIGH)
    #If the button is not pressed (0) then LED turn off
    else:
        GPIO.output(LED_PIN, GPIO.LOW)

GPIO.cleanup()
