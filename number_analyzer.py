print("===== NUMBER ANALYZER =====")

num = int(input("Enter a number: "))

if num > 0:
    print("Number is Positive")
elif num < 0:
    print("Number is Negative")
else:
    print("Number is Zero")

if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

print("Square =", num * num)
print("Cube =", num * num * num)

print("===== Analysis Complete =====")
