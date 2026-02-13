tuple_list=eval(input("Enter the list of tuples"))
k=int(input("Enter the k value:"))

produce=1
for tup in tuple_list:
    if k < len(tup):
        produce *= tup[k]
    else:
        print("Invalid k value")
        break