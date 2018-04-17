from inappropriate_notifications import notify_me, run_random_notifications
import argparse

def main():
    parser = argparse.ArgumentParser(description='Display inappropriate notifications at random intervals.')
    parser.add_argument('--once', dest='function', action='store_const', const=notify_me, default=run_random_notifications, help='Only display one notification')
    parser.add_argument('--time-between', '-t', default=10, type=int, help='Number of seconds (on average) between notifications.')
    parser.add_argument('--notification-count', '-c', default=100, type=int, help='Number of notifications to display before ending program.')

    args = parser.parse_args()
    if args.function == notify_me:
        args.function()
    else:
        args.function(seconds_between=args.time_between, number_notifications=args.notification_count)

if __name__ == '__main__':
    main()
