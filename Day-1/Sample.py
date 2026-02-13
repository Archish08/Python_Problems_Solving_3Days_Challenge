print("A has 1000/-Rs")
x = 1000
print("He buys pizza for 830")
pizza = 830
change = x - pizza
print("he gets change of",change)

notes = [100, 50, 20, 10, 5, 2, 1]
note_count = {}

for note in notes:
    count = change // note
    if count > 0:
        note_count[note] = count
        change -= note * count

print("Change Breakdown:")
for note, count in note_count.items():
    print(f"{note}Rs notes: {count}")