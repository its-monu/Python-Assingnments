print("===== LOGIN SYSTEM =====")

username = input("Enter Username: ")
password = input("Enter Password: ")

correct_username = "admin"
correct_password = "1234"

if username == correct_username and password == correct_password:
    print("\nLogin Successful!")
    print("Welcome,", username)
    print("You can access the system now.")
else:
    print("\nLogin Failed!")
    print("Invalid Username or Password.")

print("\n===== Thank You =====")
