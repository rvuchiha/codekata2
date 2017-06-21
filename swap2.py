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
    a= int(input("Enter the first number"))
    b= int(input("Enter the second number"))
    print 'the first number is' ,a
    print 'the second number is' ,b
    c=a
    a=b
    b=c
    print 'After Swap'
    print 'the first number is' ,a
    print 'the second number is' ,b

if __name__ == '__main__':
    main()
