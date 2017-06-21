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
    str1=raw_input("Enter the first string")
    str2=raw_input("Enter the second string")
    str3=str1
    str1=str2
    str2=str3
    print('the interchanged strings are '+str1+' and '+str2)

if __name__ == '__main__':
    main()
