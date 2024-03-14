import random
number = int(random.randint(0,9))
num = 5
i=0
while i<3:
    a = int(input("enter the guessed number"))
    if a == number:
        print("You guessed correct")
        break
    else:
        print("try again")
    i = i+1
print("the number is ", number)