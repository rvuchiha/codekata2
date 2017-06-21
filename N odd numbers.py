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
    num=int(input("Enter the value until whch you want the multiplication tables:"))
    mul=1
    for n in range(num):
        mul=12*(n+1)
        print '12 *',n+1,'=',mul

if __name__ == '__main__':
    main()
