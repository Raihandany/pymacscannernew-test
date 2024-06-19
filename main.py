#  Copyright (c) 2024. Yoppy Yunhasnawa, Politeknik Negeri Malang.
#  This software is available under the MIT License.
#  Contact me at: yunhasnawa@polinema.ac.id.

#  Copyright (c) 2024. Yoppy Yunhasnawa, Politeknik Negeri Malang.
#  This software is available under the MIT License.
#  Contact me at: yunhasnawa@polinema.ac.id.

from MacScanner import MacScanner
scanner: MacScanner

# LED Import
import OPi.GPIO as GPIO
import time

# LED Initialize
RED_PIN = 11
GREEN_PIN = 13
YELLOW_PIN = 15

# Set mode GPIO
GPIO.setmode(GPIO.BOARD)

# Setup LED pins
try:
    GPIO.setup(RED_PIN, GPIO.OUT)
    GPIO.setup(GREEN_PIN, GPIO.OUT)
    GPIO.setup(YELLOW_PIN, GPIO.OUT)
except OSError as e:
    print(f"Error setting up GPIO pins: {e}")
    exit(1)

# LED Function
def update_status(status):
    if status == "Scanning":
        GPIO.output(RED_PIN, GPIO.HIGH)
        GPIO.output(GREEN_PIN, GPIO.LOW)
        GPIO.output(YELLOW_PIN, GPIO.LOW)
    elif status == "Uploading":
        GPIO.output(RED_PIN, GPIO.LOW)
        GPIO.output(GREEN_PIN, GPIO.HIGH)
        GPIO.output(YELLOW_PIN, GPIO.LOW)
    elif status == "Idle":
        GPIO.output(RED_PIN, GPIO.LOW)
        GPIO.output(GREEN_PIN, GPIO.LOW)
        GPIO.output(YELLOW_PIN, GPIO.HIGH)
    elif status == "Error":
        GPIO.output(RED_PIN, GPIO.HIGH)
        GPIO.output(GREEN_PIN, GPIO.LOW)
        GPIO.output(YELLOW_PIN, GPIO.HIGH)

def setup():
    endpoint = 'https://asia-southeast2-vertical-tuner-423007-m8.cloudfunctions.net/pymacscannerEndpoint'
    ip_range = '192.168.66.0/24'
    global scanner
    scanner = MacScanner(endpoint, ip_range)

def loop2():
    update_status("Scanning")
    scan_output = scanner.scan()
    if scan_output == 0:
        update_status("Uploading")
        upload_output = scanner.upload()
        if upload_output == 0:
            update_status("Idle")
            print(scanner.upload_result)
        else:
            update_status("Error")
            print("[ERROR] Upload failed!")
    else:
        update_status("Error")
        print("[ERROR] Scan failed!")
    wait(1000)


# ASLI
#def loop():
#    scan_output = scanner.scan()
#    if scan_output == 0:
#        upload_output = scanner.upload()
#        if upload_output == 0:
#            print(scanner.upload_result)
#        else:
#            print("[ERROR] Upload failed!")
#    else:
#        print("[ERROR] Scan failed!")
#    wait(10000)


def wait(ms):
    print("Waiting for {} ms".format(ms))
    time.sleep(ms/1000)


def main():
    setup()
    while True:
        loop()

#main()

if _name_ == "_main_":
        main()


