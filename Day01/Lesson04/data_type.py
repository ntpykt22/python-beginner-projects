# String Data type

#literal assignment
first = 'Nuttarpoz'
last = 'Yakathurm'

#แสดง first เท่ากันกับ ประเภท str
# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# consturctor function
# pizza = str("Peperoni")
# # Press "Command + D" for เปลี่ยนค่าตัวแปรครั้งเดียว หลายๆ บรรทัดให้เหมือนกัน
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza , str))

# Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string 
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like pop music from the " + decade + "s."
print(statement)

# Multiple Line
multiline = '''
Hey, how are you? 

I was just checking in.
                         All good?

'''
print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)
