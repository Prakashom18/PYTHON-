name= ['apple','banana', 'mango']
for x in name:
    print(x)
print(len(name))
print(name[0:2])
numbers=[1,2,3,7,8,9]
a=0
while a < len(numbers):
    print(numbers[a])
    a=a+1
numbers.append(6)
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers.remove(3)
print(numbers)
numbers.pop()
print(numbers)
numbers.insert(4,5)
print(numbers)

num = range(5)
print(num)
for x in num:
    print(x)
n= range(5,10)
print(n)
for x in n:
    print(x)

counting = (1,2,3,4,5,5)
print( "THe number is 5 is",counting.count(5) )