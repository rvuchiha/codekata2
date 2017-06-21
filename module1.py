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
    char=raw_input("Enter the char")
    if char=="a" or "e" or "i" or "o" or "u":
        print 'it is a vowel'
    else:
        print 'it is a consonant'

if __name__ == '__main__':
    main()
