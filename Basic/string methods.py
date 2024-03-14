a = ''' Hello Buddy 
THis is python programming with the string method '''
print(a)

b = "apple"
print(b[-1])
print(b[0:2])
print(b[1:])
print(b[:])

name= ' Python Programming'
name.upper()
print(name[5:-1])
print(name[1:8:2])
print(name[1:12:3])

first = "John"
last = "Doe"
message = first + '[' + last + '] is a coder'
print(message)

msg = f' { first }  { last} is a professional coder'
print(msg)
print(len(msg))
print(msg.replace('coder','cricketer'))
print('is' in msg)
x=name.find('y')
print(x)
