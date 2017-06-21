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
    a_string=raw_input("Enter the string")
    newstring = ''
    i = len(a_string)
    while i:
        i -= 1
        newstring += a_string[i]
    print (newstring)
if __name__ == '__main__':
    main()
