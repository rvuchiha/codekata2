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
    n= int(input("Enter the number of days"))
    x=n/365
    y=n%365
    z=y/30
    a=y%30
    b=a/7
    c=a%7

    print('there are',x,'years')
    print('there are',z,'Months')
    print('there are',b,'weeks')
    print('there are',c,'days')

if __name__ == '__main__':
    main()
