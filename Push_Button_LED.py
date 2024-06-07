import RPi.GPIO as GPIO #type: ignore
import time

BUTTON_PIN = 26
LED_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.input(BUTTON_PIN)

while True:
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        GPIO.output(LED_PIN, GPIO.HIGH)
    else:
        GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.02)

GPIO.cleanup()