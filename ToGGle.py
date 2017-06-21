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
import string
def main():
    str1=raw_input("Enter the string")
    str2=string.swapcase(str1)
    print 'the toggled string is',str2

if __name__ == '__main__':
    main()
