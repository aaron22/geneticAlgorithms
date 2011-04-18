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

from graphics import *

def main():
    win = GraphWin("My Circle", 100, 100)
    c = Line(Point(25,25), Point(75,75))
    c.draw(win)
    win.getMouse() # Pause to view result
    c.undraw()
    win.getMouse()
    win.close()    # Close window when done

if __name__ == '__main__':
    main()