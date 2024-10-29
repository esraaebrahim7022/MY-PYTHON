#نستخدم {}عشان نعرف معجم
#dictionary
convert_month ={
    '0' : 'january',
    'feb' : 'february',
    'mar' : 'march'
}

print(convert_month['feb'])#الطريقه الاولى للطباعه

print(convert_month.get('ma','the value not found'))#الطريقه الثانية للطباعه