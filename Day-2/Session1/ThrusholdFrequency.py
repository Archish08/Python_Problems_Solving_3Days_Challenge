tuple_series=input("Enter the list of number series")
k = int(input("Enter the threshold frequency"))
processed_num=[]
print("The numbers with frequency:")
for num in tuple_series.split(","):
    if num not in processed_num:
        count=tuple_series.count(num)
        if count>=k:
            print(f"Number{num} : {count} times")
        processed_num.append(num)