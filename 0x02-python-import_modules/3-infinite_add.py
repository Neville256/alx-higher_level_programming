#!/usr/bin/python3

if __main__ == "__main__":
    """Print the addition of all arguemnts."""
    import sys
    total = 0
    for k in range(len(sys.argv) - 1):
        total += int(sys.argv[k + 1])
        print("{}".format(total))
