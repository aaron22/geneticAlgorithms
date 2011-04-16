#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      aaron
#
# Created:     16/04/2011
# Copyright:   (c) aaron 2011
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import sys

def main():
    for i in sys.argv:
        arg = i.split('=')
        if arg[0] == 'gens':
            print("gens -> ", int(arg[1]))
        elif arg[0] == 'length':
            print("length -> ", int(arg[1]))
        elif arg[0] == 'popsize':
            print("popsize -> ", int(arg[1]))

if __name__ == '__main__':
    main()