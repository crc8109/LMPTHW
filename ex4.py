from sys import argv
import argparse
from textwrap import dedent

def no_argparse():
    script, flag = argv
    flags = {
            # Help flag
            "-h" : "This is the help flag; it provides a hint. Please pass along a flag like -f",

            # These will change script
            "-f" : "This is foo; try -b next",
            "--foo" : "This is foo; try --boo next",
            "-b" : "To find the secret message, try the -s flag",
            "--bar" : "To find the secret message, try the --secret flag",
            "-s" : "This is the last secret message, you win!",
            # Variables
            "caps" : "capitalize everything!",
            "secret_caps" : "Reveal secret message in all caps!"

    }


    first_secret = "You found secret message foo! It's not very valuable though..."
    second_secret = "You're getting warmer! Maybe try a -s or --secret flag?"

    script = f"""
    Hello! Welcome to {script}!
    Depending what argument you passed along, this script changes!
    The right flag reveals a secret message! Try using the -h flag or something.
    """
    print(dedent(script))

    if flag == "-h" or flag == "--help":
        print(flags["-h"])

    if flag == "-f" or flag == "--foo":
        print(flags["-f"])

    if flag == "-b" or flag == "--bar":
        print(flags["-b"])

    if flag == "-s" or flag == "--secret":
        print(flags["-s"])

    if flag == "-c":
        print(script.upper() +
        "You triggered a variable for this script that capitalizes everything!")
        print("    try -sc now ;)")

    if flag == "-sc":
        print(script.upper() + "You triggered the last hidden variable!")

def use_argparse():
    parser = argparse.ArgumentParser()
    # 3 Flags (including the default -h/--help)
    parser.add_argument('-q', '--quiet',
                    action='store_true',
                    dest='quiet',
                    help='Suppress Output'
                    )

    parser.add_argument('-v', '--verbose',
                    action='store_true',
                    help='Verbose Output'
                    )

    # 3 Arguments
    parser.add_argument('-H', '--host',
                    default='localhost',
                    dest='host',
                    help='Provide destination host. Defaults to localhost',
                    type=str
                    )

    parser.add_argument('-P', '--port',
                    default='3000',
                    dest='port',
                    help='Provide destination port. Defaults to 3000',
                    type=str
                    )

    parser.add_argument('-U', '--user',
                    default='root',
                    dest='user',
                    help='Provide user to access host. Defaults to root!',
                    type=str
                    )

    args = parser.parse_args()

    print('Quiet mode is %r.' % args.quiet)
    print('Verbose mode is %r.' % args.verbose)
    print(f'The host is "{args.host}"')
    print(f'The port is "{args.port}"')
    print(f'The user is "{args.user}"')
    # parser.add_argument('integers', metavar='N', type=int, nargs='+')
    # parser.add_argument('-f', '--foo', help='foo help')
    # parser.add_argument('-b', '--bar', help='bar help')
    # parser.add_argument('-z', '--baz', help='baz help')
    # parser.add_argument('-t', '--turn-on', action='store_true')
    # parser.add_argument('-x', '--exclude', action='store_false')
    # parser.add_argument('-s', '--start', action='store_true')
    # args = parser.parse_args()
    #
    # print(args)

# Comment out ONE of the calls below to see how the exercise is handled differently
# no_argparse()
use_argparse()
