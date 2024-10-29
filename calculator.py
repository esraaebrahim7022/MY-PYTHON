#calculator app
num1 =float(input('Enter Your First Number: '))
operator = input('Enter Your Operator: ')
num2 = float(input('Enter Your Second Number: '))

if operator =='+':
    print(num1+num2)

elif operator =='-':
    print(num1-num2)

elif operator =='/':
    print(num1/num2)

elif operator=='*':
    print(num1*num2)

else:
    print('invalid operator, try again')

##########################################

#Madlips app
color = input('Enter a color: ')
plural_noun = input("enter a plural noun: ")
adjective= input("enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are mean")
print("please keep it " + adjective)