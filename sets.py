numbers =[1,2,3,4,5,6,7,8,9,10,2,1,4,6,8,12,13,56,1,9,10,3,5,7]
#fisrt solution:
unique_list=[]

for number in numbers:
    if number not in unique_list:
        unique_list.append(number)#لو الرقم مميز ضيفهولي

print(unique_list)

####################################

#another solution:

unique_set = set(numbers)
print(unique_set)
##########################################

#sets مش بتقبل التكرار ، وبتستخدم ف ال unique numbers 
uniqueSet =set(numbers)
print (type(uniqueSet))

#######################################
name='esraaaaaa'
unique_set= set(name)
print(set(name))
unique_list =list(unique_set)
unique_list.append(5)
print(unique_list)


#all set
### ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__',
### '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
### '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', 
### '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
### '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 
### 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
################@@@@@@@@@