#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      N.VINAY RAM
#
# Created:     21/06/2017
# Copyright:   (c) N.VINAY RAM 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    n= int(input("Enter the year"))
    if(n%4==0):
        print (n),'is a leap year'
    else:
        print (n),'is not a leap year'
if __name__ == '__main__':
    main()
