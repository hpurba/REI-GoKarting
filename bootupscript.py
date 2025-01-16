# See the README for how to run the code


import RPi.GPIO as GPIO
import time

LED_PIN = 18
SWITCH_PIN = 25

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN)

try:
    # Blink the LED in a loop
    for i in range(2):  # Adjust range for the number of blinks
        GPIO.output(LED_PIN, GPIO.HIGH)  # Turn LED on
        print(f"Light on {i}")
        time.sleep(2)  # Wait 0.5 seconds
        GPIO.output(LED_PIN, GPIO.LOW)  # Turn LED off
        print(f"Light off {i}")
        time.sleep(2)  # Wait 0.5 seconds
    
    # Button control
    printing_on_message = False
    while True:
        if GPIO.input(SWITCH_PIN): # pin is HIGH. Voltage high becauses electricity to to the GPIO pin only
            GPIO.output(LED_PIN, GPIO.LOW)
            if not printing_on_message:
                print("Switch not pressed and light OFF")
                printing_on_message = True
        else: # pin is LOW. Voltage low because of short circuit. Electricity has a path directly to ground.
            GPIO.output(LED_PIN, GPIO.HIGH)
            if printing_on_message:
                print("Switch pressed and light ON")
                printing_on_message = False    
        
except KeyboardInterrupt:
    print("\nExiting safely...")
    # Blinking to say goodbye
    for i in range(10):
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(.05)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(.05)
finally:
    print("Ending Program")
    GPIO.cleanup()  # Clean up GPIO settings on exit
    # time.sleep(1)