#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv_len = len(sys.argv)

    add = 0
    if argv_len == 1:
        pass
    else: 
        for i in range(1, argv_len):
            add += int(sys.argv[i])
    print('{}'.format(sum))
