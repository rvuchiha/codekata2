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
import math
def main():
    opt=int(input("enter the shape 1.Triangle 2.Square 3.REctangle"))
    if(opt==1):
        a= int(input("Enter breath:"))
        b= int(input("Enter height:"))
        print("Area is",.5*a*b)
    elif(opt==2):
    	a=int(input("Enter Side:"))
    	print("the Area is ",a*a)
    elif(opt==3):
    	l=int(input("Enter Dimension l:"))
    	b=int(input("Enter Dimension b:"))
    	print("the Area is ",l*b)
    else:
    	print("u r useless")

if __name__ == '__main__':
    main()
