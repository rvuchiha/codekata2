#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      N.VINAY RAM
#
# Created:     21/06/2017
# Copyright:   (c) N.VINAY RAM 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    a= int(input("Enter the number"))
    d=a
    sum=1
    for n in range(1000):
        y=a/10
        if(y != 0):
            sum+=1
            n+=1
            a=a/10
        else:
            exit

        exit
    rev=0
    s=sum
    for s in range(s,0,-1):
        x=d%10
        d=d/10
        e=x*(10**(s))
        rev+=e
    ans=rev/10
    print (ans)
if __name__ == '__main__':
    main()
