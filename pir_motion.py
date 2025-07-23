import time
import RPi.GPIO as GPIO


def monitor(pin: int = 18) -> None:
    """Monitor the HS-SR501 sensor and print when motion is detected.

    Parameters
    ----------
    pin: int
        BCM pin number where the sensor output is connected.
    """

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)

    print("PIR Module Test (press Ctrl+C to exit)")
    time.sleep(2)  # allow the sensor to stabilize
    print("Ready")

    try:
        while True:
            if GPIO.input(pin):
                print("Motion detected!")
                # Wait for the sensor to reset
                while GPIO.input(pin):
                    time.sleep(0.1)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        GPIO.cleanup()


if __name__ == "__main__":
    monitor()
