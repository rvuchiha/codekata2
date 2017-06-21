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
    num=int(input("Enter the number until which you want to find the fib series"))
    fib1=[0,1]
    a=0
    b=1
    for b in range(1,num):
        print (b)
        fib1=[a+b,]
        print (fib1)
        fib=a+b
        a=b
        b=fib
        fib1.append(b)

    print fib1

if __name__ == '__main__':
    main()
