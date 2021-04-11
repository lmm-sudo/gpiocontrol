import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)

try:
    while True:
        GPIO.output(16, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(16, GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt:  # 异常处理，如果Ctrl+C退出程序
    GPIO.output(16, GPIO.LOW)
    GPIO.cleanup()
