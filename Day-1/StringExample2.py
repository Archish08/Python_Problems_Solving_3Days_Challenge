s = input("Enter a String\n")
length = len(s)
mid = length//2
first_half = s[:mid]
second_half = s[mid:]
fn = first_half[::-1]
ln = second_half[::-1]
result=fn+ln
print(result)