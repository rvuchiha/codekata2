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
    a= int(input("Enter the a term"))
    b= int(input("Enter the b term"))
    c= int(input("Enter the c term"))
    if(a>b and a>c):
        print'a is greatest'
    elif(b>a and b>c):
        print'b is greatest'
    else:
        print'c is greatest'
if __name__ == '__main__':
    main()
