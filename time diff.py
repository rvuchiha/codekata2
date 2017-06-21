#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      N.VINAY RAM
#
# Created:     21/06/2017
# Copyright:   (c) N.VINAY RAM 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    h1=int(input("Enter the hours of first time"))
    m1=int(input("Enter the minutes of first time"))
    h2=int(input("Enter the hours of second time"))
    m2=int(input("Enter the minutes of second time"))
    td=(h1*60+m1)-(h2*60+m2)
    if(td<1):
        print'the time difference is',(-td),'mins'
    else:
        print'the time difference is',(td),'mins'
if __name__ == '__main__':
    main()
