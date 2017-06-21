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
    m1= int(input("Enter the mark in math"))
    m2= int(input("Enter the mark in phy"))
    m3= int(input("Enter the mark in chem"))
    m4= int(input("Enter the mark in comp"))
    m5= int(input("Enter the mark in python"))
    total=m1+m2+m3+m4+m5
    avg=(total)/5
    percent=float(total/5)
    print'the total is',(total)
    print'the average is',(avg)
    print'the percentage is',(percent),'%'

if __name__ == '__main__':
    main()
