import argparse
from pir_motion import monitor


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Monitor HS-SR501 motion sensor")
    parser.add_argument(
        "--pin",
        type=int,
        default=23,
        help="BCM GPIO pin connected to the sensor's OUT pin",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    monitor(pin=args.pin)


if __name__ == "__main__":
    main()
