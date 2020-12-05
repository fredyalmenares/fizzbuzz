from fizzbuzz import calculate_fizzbuzz_range
import argparse


def run_default():
    calculate_range(1, 100)


def calculate_range(start, end):
    for result in calculate_fizzbuzz_range(start, end):
        print(result)


def main():
    parser = argparse.ArgumentParser(description="Calculate FizzBuzz algorithm",
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    subs = parser.add_subparsers()
    run_parser = subs.add_parser('run', help='Calculate FizzBuzz algorithm from 1 to 100')
    run_parser.set_defaults(func=run_default)

    range_parser = subs.add_parser('range', help='Calculate FizzBuzz algorithm int the range of the followed typed '
                                                 'numbers.')
    range_parser.add_argument('start',
                              help='Start of the range',
                              type=int)
    range_parser.add_argument('end',
                              help='End of the range',
                              type=int)

    range_parser.set_defaults(func=calculate_range)
    args = parser.parse_args()
    if hasattr(args, 'func'):
        if args.func.__name__ == 'run_default':
            run_default()
        else:
            calculate_range(args.start, args.end)
    else:
        run_default()


if __name__ == '__main__':
    main()
