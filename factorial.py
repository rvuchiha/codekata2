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
    fact=1
    a= int(input("Enter the number for which is to be found"))
    for n in range(a):
        fact*=(n+1)
    print 'factorial is',(fact)
if __name__ == '__main__':
    main()
