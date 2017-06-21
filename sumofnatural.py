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
    sum=0
    a= int(input("Enter the number till which sum is to be found"))
    for n in range(a):
        sum+=(n+1)
    print 'sum is',(sum)

if __name__ == '__main__':
    main()
