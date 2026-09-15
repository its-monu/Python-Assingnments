print("===== CAR DRIVE SIMULATION =====")

speed = 0

while True:
    print("\n1. Accelerate")
    print("2. Brake")
    print("3. Show Speed")
    print("4. Stop Car")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        speed = speed + 10
        print("Car speed:", speed, "km/h")

    elif choice == "2":
        speed = speed - 10

        if speed < 0:
            speed = 0

        print("Car speed:", speed, "km/h")

    elif choice == "3":
        print("Current speed:", speed, "km/h")

    elif choice == "4":
        speed = 0
        print("Car stopped.")

    elif choice == "5":
        print("Exiting Car Drive Simulation.")
        break

    else:
        print("Invalid choice.")
