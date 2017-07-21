#!/usr/bin/python

from __future__ import print_function
import sys

def Header():
    print("\n[\tThis is an script to reverse strings.\t]")
    print("[\tWritten by Milad Kahsari Alhadi.\t]\n")

def StartPoint(_arg_string):
    inputString = _arg_string
    
    print("\t\033[91m\033[1mString length: {}\033[0m".format(len(inputString)))
    
    inputStringList = [inputString[i:i+4] for i in range(0, len(inputString), 4)]

    print("\n\t\033[92m\033[1mReversed Strings:\033[0m\n")
    for item in inputStringList[::-1]:
        print("\t\t", end='')
        print(item[::-1] + " : push 0x" + str(item[::-1].encode('hex'))) 

    print("\n\n")  

if __name__ == "__main__":
    Header()
    if (len(sys.argv) < 2):
        print("\tUsage: ./reverse.py [String]\n")
    else:
        StartPoint(sys.argv[1])
