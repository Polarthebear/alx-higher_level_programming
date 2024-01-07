#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arguments = sys.argv
    if len(arguments) == 2:
        print("{}: argument".format(len(arguments) - 1))
    elif len(arguments) >= 3:
        print("{}: arguments".format(len(arguments) - 1))
    else:
        print("{} arguments.".format(len(arguments) - 1))
