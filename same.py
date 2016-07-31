#!/usr/bin/python3
#
# same.py
# Like less/more but dumps text slowly
#
# Authors:
#
#     Schuyler Martin <sam8050@rit.edu>

import signal
import sys
import time

#### CONSTANTS ####
USAGE = "Usage: same.py [in_file]"

TEXT_SPEED = 0.025

#### FUNCTIONS ####


def kill_trap(signal, frame):
    '''
    Function/trap to handle CTRL-C interrupt signal
    :param: signal UNIX-signal
    :param: frame Context
    '''
    sys.exit(0)

def read_input():
    '''
    Reads input from file or STDIN, based on command line arguments
    :return: List of strings (one string per line of input)
    '''
    str_lst = []
    # read from file
    if (len(sys.argv) > 1):
        for line in open(sys.argv[1]):
            str_lst.append(line.strip(" "))
    # read from STDIN
    else:
        for line in sys.stdin:
            str_lst.append(line.strip(" "))
    return(str_lst)

def main():
    '''
    Primary execution point of the script
    '''
    # register trap for signal
    signal.signal(signal.SIGINT, kill_trap)
    # capture input
    raw_data = read_input()
    # write output...slowly
    for line in raw_data:
        for ch in line:
            print(ch, end="", flush=True)
            time.sleep(TEXT_SPEED)

if __name__ == '__main__':
    main()
