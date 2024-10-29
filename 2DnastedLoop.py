#2D Lists :

matrix = [
          [1,2,3],
          [4,5,6],
          [7,8,9]
          ]

print(matrix)

#Nested Loops:لوب جوه لوب

for row in matrix:
    for column in row:
        print(column*2 )

########################################
#Python Errors:عندنا انواع كتير من الايرورز
try:
    number = int(input('Enter a number: '))
    print(number)
    result=10/0
except ZeroDivisionError as err:
    print(err)   
except ValueError as err1:
    print('Invalid input')

print('Finished')
