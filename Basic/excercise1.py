weight = int(input(" Enter the weight "))
choice= input("enter choice for k or l")
if choice.upper() == "K":
    result = weight * 1000
    print(result)
elif choice.upper() == "L":
    result = weight / 2.20
    print(result)
else:
    print("Invalid")


