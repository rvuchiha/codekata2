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
    char=raw_input("Enter the char")
    import string
    if char in ('1','2','3','4','5','6','7','8','9','0'):
        print 'it is a number'
    elif char in (string.lowercase[:26]):
        print 'it is a alphabet'
    else:
        print 'it is a special charector'
if __name__ == '__main__':
    main()
