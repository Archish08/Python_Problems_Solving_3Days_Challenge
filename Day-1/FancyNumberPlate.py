number = input("Enter a 4 digit number:")
if len(number)!=4 or not number.isdigit():
    print("Get Lost")
else:
    increasing=True
    decreasing=True

    for i in range(3):
        if number[i]>=number[i+1]:
            increasing=False
        if number[i]<=number[i+1]:
            decreasing=False
    if increasing:
        print("Fancy Number")
    else:
        print("Not a fancy number")