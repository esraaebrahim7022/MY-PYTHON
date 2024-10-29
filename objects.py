from Classes import Employee#بتاخد اسم الملف واسم الكلاس
from Classes import Student

employee1 = Employee('esraa','ebrahim',40,'IT',True,1500)
employee2= Employee('soha','ismail',60,'data entry',False,1000)
employee3= Employee('ahmed','hussam',50,'data analysis',False,500)

employee1.bonus()
employee2.bonus()

#########################################################################

student1 = Student('alaa','ebrahim',19,'IT',5)
student2= Student('samaa','ismail',40,'data entry',2.3)
student3= Student('hanaa','hussam',50,'cs',3)

print(student1.name,student2.gpa,student3.major)
print(student1.is_excellent(),student2.is_excellent())


 