# Student Records Management System

names = []
marks = []

n = int(input("Enter the number of students: "))

for i in range(n):
    name = input(f"\nEnter student {i + 1} name: ")
    mark = float(input(f"Enter {name}'s marks: "))

    names.append(name)
    marks.append(mark)

print("\n--- Student Records ---")

for i in range(len(names)):
    print(f"{names[i]}: {marks[i]} marks")

# Search for a student
search_name = input("\nEnter name to search: ")

if search_name in names:
    index = names.index(search_name)
    print(f"{search_name} scored {marks[index]} marks.")
else:
    print("Student not found.")

# Sort students by marks
print("\n--- Students Sorted by Marks ---")

sorted_records = sorted(
    zip(names, marks),
    key=lambda student: student[1],
    reverse=True
)

for name, mark in sorted_records:
    print(f"{name}: {mark} marks")

# Highest and lowest scores
if marks:
    highest = max(marks)
    lowest = min(marks)

    print("\n--- Score Results ---")
    print("Highest Score:", highest)
    print("Lowest Score:", lowest)

    highest_index = marks.index(highest)
    lowest_index = marks.index(lowest)

    print("Top Student:", names[highest_index])
    print("Lowest Scoring Student:", names[lowest_index])
