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
    a= int(input("Enter the number"))
    sum=1
    for n in range(1000):
        y=a/10
        if(y != 0):
            sum+=1
            n+=1
            a=a/10
        else:
            exit

        exit

    print 'the no. of digits is:',(sum)
if __name__ == '__main__':
    main()
