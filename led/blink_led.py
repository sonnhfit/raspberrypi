import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

from time import sleep # Import the sleep function from the time module

PIN_GPIO = 11
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(PIN_GPIO, GPIO.OUT, initial=GPIO.LOW) # Set pin 11 to be an output pin and set initial value to low (off)


while True: # Run forever
  GPIO.output(PIN_GPIO, GPIO.HIGH) # Turn on
  sleep(1) # Sleep for 1 second
  GPIO.output(PIN_GPIO, GPIO.LOW) # Turn off
  sleep(1) # Sleep for 1 second
