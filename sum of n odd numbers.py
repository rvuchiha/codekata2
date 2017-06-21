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
    limit = int(input("Enter the upper limit: "))
    sum = 0
    for n in range(limit):
        if(n%2==1):
            sum+=n
        else:
            sum+=0
    n+=1
    print 'the sum is',(sum)


if __name__ == '__main__':
    main()
