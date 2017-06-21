#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      N.VINAY RAM
#
# Created:     20/06/2017
# Copyright:   (c) N.VINAY RAM 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    amt=int(input("What the Amount"))
    rate=int(input("Whats the rate"))
    yr=int(input("whats the number of years"))
    si = amt*yr*rate/100
    print("The simple interest is",si)


if __name__ == '__main__':
    main()
