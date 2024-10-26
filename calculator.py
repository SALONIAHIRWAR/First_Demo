
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      cyber
#

# Created:     01/08/2023
# Copyright:   (c) cyber 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

print(''' Addition= +
subtrection= -
multiplication= *
division= /''')

num1=(int(input("Enter the value1:-")))
opr=(input("Enter the opr"))
num2=(int(input("Enter the value2:-")))


if opr=="+":
      print(num1+num2)
elif opr== "-":
       print(num1-num2)
elif opr== "*":
       print(num1*num2)
elif opr=="/":
       print(num1/num2)
else:
   print("Invalid opr....")



   # outher is saloni