# Send to raspberry pi: scp led_on.py pi@192.168.1.39:~/led_on.py
# Run: python3 led_on.py
import RPi.GPIO as GPIO
import time

LED_PIN = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)  # Turn LED on
finally:
    print("Ending Program")
    GPIO.cleanup()  # Clean up GPIO settings on exit