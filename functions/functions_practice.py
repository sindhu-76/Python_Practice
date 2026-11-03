
# Python Functions Practice
# Student Marks Calculator

# Get number of subjects
n = int(input("Enter number of subjects: "))

# Get marks
marks_list = []

for i in range(n):
    marks = int(input("Enter marks: "))
    marks_list.append(marks)

print("Marks List:", marks_list)

# 1. Calculate total marks
def total_marks(l):
    total = 0
    for i in l:
        total += i
    return total

# 2. Calculate average marks
def avg_marks(l):
    total = total_marks(l)
    average = total / len(l)
    print("Average Marks:", average)

# 3. Find highest marks
def highest_marks(l):
    large = l[0]
    for i in l:
        if i > large:
            large = i
    return large

# 4. Find lowest marks
def lowest_marks(l):
    small = l[0]
    for i in l:
        if i < small:
            small = i
    return small

# 5. Calculate percentage
def percentage(l):
    total = total_marks(l)
    per = (total / (len(l) * 100)) * 100
    return per

# 6. Calculate grade
def grade_system(l):
    percent = percentage(l)
    if percent > 90:
        print("Grade: A")
    elif percent > 70:
        print("Grade: B")
    elif percent > 50:
        print("Grade: C")
    elif percent > 30:
        print("Grade: D")
    else:
        print("Grade: E")

# 7. Count passed subjects
def count_passed_std(l):
    count = 0
    for i in l:
        if i >= 25:
            count += 1
    print("Passed Subjects:", count)
    print("Failed Subjects:", len(l) - count)

# Display results
print("\n----- Student Marks Report -----")

total = total_marks(marks_list)
print("Total Marks:", total)

avg_marks(marks_list)

highest = highest_marks(marks_list)
print("Highest Marks:", highest)

lowest = lowest_marks(marks_list)
print("Lowest Marks:", lowest)

percent = percentage(marks_list)
print("Percentage:", percent, "%")

grade_system(marks_list)

count_passed_std(marks_list)
