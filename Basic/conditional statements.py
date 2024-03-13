is_hot = True
if is_hot:
    print("It is hot")
else:
    print("It is not hot")

a = int(input("Enter the temperature"))
if a >30 and a>10:
    print("IT is hot day")
elif a<10 and a<30:
    print("It is cold day")
else:
    print("It is neither cold or hot")


name = input("enter the name")
if len(name)>5:
    print("Character out of range")
elif len(name)<5 and len(name)>=3:
    print("Character looks good")
else:
    print("Invalid")