while True:
    age_input = input("Enter your age (or type 'quit' to exit): ")

    if age_input == "quit":
        print("Program ended.")
        break

    age = int(age_input)

    if age < 12:
        price = 8
    elif age >= 65:
        price = 10
    else:
        price = 15

    print(f"Your ticket price is ${price}.")
