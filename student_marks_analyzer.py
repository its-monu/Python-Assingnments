print("===== STUDENT MARKS ANALYZER =====")

name = input("Enter Student Name: ")

m1 = float(input("Enter marks in Python: "))
m2 = float(input("Enter marks in DSA: "))
m3 = float(input("Enter marks in Mathematics: "))

total = m1 + m2 + m3
percentage = total / 3

print("\n===== RESULT =====")
print("Student Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 60:
    print("Grade: A")
elif percentage >= 50:
    print("Grade: B")
elif percentage >= 40:
    print("Grade: C")
else:
    print("Grade: F")

if percentage >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")

print("==============================")
