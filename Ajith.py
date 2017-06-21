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
    name = str(raw_input("Enter your name"))
    if name in ["ajith","Ajith"]:
        print 'Greetings Mr.Ajith'
    else:
        exit()

if __name__ == '__main__':
    main()
