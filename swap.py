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
    a= int(input("Enter the number"))
    print('The entered number is:',a)
    b=a/10
    c=a%10
    sn=c*10+b
    print('The swapped number is:',sn)


if __name__ == '__main__':
    main()
