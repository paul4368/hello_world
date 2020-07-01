a = float(input('Enter in £ and pence....'))
x = "p"
z = "You entered £%s%s" % (a,x) #only way I could find to have no spaces between the numbers and £,p
print(z)
print("The change you need to give, need to be made up of the following ..")
b = a * 100   #changes the float into a whole number, by simply moving the demical point two places
c = int(b) #changes float back into int
print(c//200, "£2")
c = c%200
print(c//100, "£1")
c = c%100
print(c//50, "50p")
c = c%50
print(c//20, "20p")
c = c%20
print(c//10, "10p")
c = c%10
print(c//5, "5p")
c = c%5
print(c//1, "pennies")
