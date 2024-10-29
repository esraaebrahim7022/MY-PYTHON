#loops  
#while loop(continue)
i=1
while i<=10:
    if i==6:
       continue #لو الشرط اتحقق اعمله سكيب وكمل
    i+=1
    print(i)

#break 
i=2
while i<=10:
    if i==5:
       break#لو الشرط اتحقق وقف اللوب واخرج
    i+=1
    print(i)

print("the loop ended ")
###################

numApple =0 
numOrange =0 

while True:
 fruit = input("what is the kind : ") 
 if fruit == "done":
    break
 elif fruit == "orange":
    numOrange += 1 
 elif fruit == "apple" :
    numApple += 1 
 else:
    print ("not valid")

totalFruit = numApple + numOrange 

print ("total : "  , totalFruit)


######################################

#for  loops :
#فانكشن len بيرجعلي عدد القيم الي جوه الليست او عدد حروف الكلمه ال 

buddies =['rabanzil','cidrella','snowhite','wenner']

for i in range(len(buddies)):
   if buddies[i]==' wenner':
      print(i," the wenner!")
   else:
      print(i,' not the wenner!')



