#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arguments = sys.argv
    argv_len = len(arguments) - 1
    if argv_len == 0:
        print("0 arguments.")
    elif argv_len == 1:
        print("1 argument:")
    else:
        print("{}: arguments".format(argv_len))

    for i in range(argv_len):
        print("{}: {}".format(i + 1, arguments[i + 1]))
