#فانكشن open بتاخد اسم الملف والي محتاجه اعمله فيه
workers_file = open('Workers','r')

print(workers_file.readable())#فانكشن بتشوفلي الملف صالح للقراءه ولا لا

print(workers_file.readlines())#read line by line (in list)

workers_file.close()#لازم نقفل الملف بعد ما بنقراه
############################3

#كيفيه انشاء ملف مش موجود a,a+,w,w+
workers_file =open('esoo','+a')

workers_file.write('\nesraaaaaaaaaaaaaaa')


#r:read file (only)
#a:write file (only)
#r+,a+ :read and write
#a:(append):اضيف فقط على اخر الملف
#w ,w+:امسح المكتوب ف الفايل واكتب من جديد



