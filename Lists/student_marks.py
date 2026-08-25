# Student Marks Manager

marks = [85, 90, 78, 92, 88]

print("Marks:", marks)
print("Highest:", max(marks))   # largest value
print("Lowest:", min(marks))    # smallest value
print("Average:", sum(marks)/len(marks))  # average

# loop through marks
for i, mark in enumerate(marks):   # enumerate gives index + value
    print("Student", i+1, ":", mark)

# update a mark
marks[2] = 80   # change 3rd student's mark
print("Updated Marks:", marks)
