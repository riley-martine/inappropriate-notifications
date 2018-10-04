"""Command line utility to interface with inappropriate_notifications code."""
import argparse

from inappropriate_notifications import notify_me, run_random_notifications

from .version import VERSION


def main():
    """Main function. Uses argparse to generate and run a parser."""
    parser = argparse.ArgumentParser(
        description="Display inappropriate notifications at random intervals."
    )

    parser.add_argument(
        "--once",
        dest="function",
        action="store_const",
        const=notify_me,
        default=run_random_notifications,
        help="Only display one notification",
    )

    parser.add_argument(
        "--time-between",
        "-t",
        default=10,
        type=int,
        help="Number of seconds (on average) between notifications.",
    )

    parser.add_argument(
        "--notification-count",
        "-c",
        default=100,
        type=int,
        help="Number of notifications to display before ending program.",
    )

    parser.add_argument("--version", "-V", action="store_true")

    args = parser.parse_args()
    if args.version:
        print(f"Inappropriate Notifications {VERSION}")
    elif args.function == notify_me:
        args.function()
    else:
        args.function(
            seconds_between=args.time_between,
            number_notifications=args.notification_count,
        )


if __name__ == "__main__":
    main()
