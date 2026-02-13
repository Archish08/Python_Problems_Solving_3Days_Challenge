#create a list to take input of 5 numbers from user
numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
print("The list of numbers is:", numbers)
#count the number of even and odd numbers in the list
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
