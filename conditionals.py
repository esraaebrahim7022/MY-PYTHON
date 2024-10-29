is_hungry= True
wants_to_eat= False

if is_hungry or wants_to_eat:
    print("eat something")
else:
    print("dont eat")


#لو عايزه احقق شرط والتاني لا عادي مع and
if is_hungry and wants_to_eat:
    print("eat something")

elif is_hungry and not wants_to_eat:
    print("eat to servive")
else:
    print("dont eat")

#########################################################

#Comparisons
def max_num(num1,num2,num3):
    #في حاله ان رقم 1 اكبر منهم
    if num1>=num2 and num1>=num3:
        return num1
    #في حاله ان رقم 2 اكبر منهم
    elif num2>=num1 and num2>=num3:
        return num2
    #في حاله ان رقم 3 اكبر منهم
    else:
        return num3
    
#نطبع القيمه ب print
print(max_num(3,4,5))

#الفانكشن معموله جاهزه في بايثون
print(max(3,4,7))

#another ex:
def match_string(str1,str2):
    if str1==str2:
        print('the string do match')
    else:   
        print("the string dont match")

match_string('cisco','cisco')        