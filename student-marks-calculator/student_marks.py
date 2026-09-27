name = input("Enter student name: ")

maths = float(input("Enter Maths marks: "))
python = float(input("Enter Python marks: "))
english = float(input("Enter English marks: "))

total = maths + python + english
average = total / 3

print("\nStudent:", name)
print("Total:", total)
print("Average:", average)
if average >= 40:
    print("Result: Passed")
else:
    print("Result: Failed")
