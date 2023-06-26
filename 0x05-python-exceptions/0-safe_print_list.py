#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x list of elements.

    args:
        my_list(list): print elements from list.
        x(int): number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    ret = 0
    for k in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except indexError:
            break
        print("")
        return(ret)
