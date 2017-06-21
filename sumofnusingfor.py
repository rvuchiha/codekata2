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

    a= int(input("Enter the number of terms"))
    aa=0
    for n in range(a):
        nu= int(input("Enter the term"))
        aa+=nu
        n+=1
    print 'sum is',(aa)
if __name__ == '__main__':
    main()
