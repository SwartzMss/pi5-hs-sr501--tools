from gpiozero import MotionSensor
import time
import signal


def monitor(pin: int = 18) -> None:
    """Monitor the HS-SR501 sensor and print when motion is detected.

    Parameters
    ----------
    pin: int
        BCM pin number where the sensor output is connected.
    """

    sensor = MotionSensor(pin)

    print("PIR Module Test (press Ctrl+C to exit)")
    time.sleep(2)  # allow the sensor to stabilize
    print("Ready")

    sensor.when_motion    = lambda: print("Motion", time.strftime("%H:%M:%S"))
    sensor.when_no_motion = lambda: print("NoMotion", time.strftime("%H:%M:%S"))

    try:
        signal.pause()
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        sensor.close()


if __name__ == "__main__":
    monitor()
