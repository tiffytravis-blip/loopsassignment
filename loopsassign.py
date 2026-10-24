def menu():
    print("\nTaco Palace Menu")
    print("1. Taco - $3.50")
    print("2. Burrito - $5.00")
    print("3. Nachos - $4.50")
    print("4. Soft Drink - $2.00")
    print("5. Quit")


def price(choice):
    if choice == 1:
        return 3.50
    elif choice == 2:
        return 5.00
    elif choice == 3:
        return 4.50
    elif choice == 4:
        return 2.00


orders = []
total = 0

print("Welcome to Taco Palace! Please view the menu and make a selection.")

while True:
    menu()
    choice = int(input("Enter your choice: "))

    if choice == 5:
        break

    elif choice == 1:
        item = "Taco"
    elif choice == 2:
        item = "Burrito"
    elif choice == 3:
        item = "Nachos"
    elif choice == 4:
        item = "Soft Drink"
    else:
        print("Invalid choice. Try again.")
        continue

    print("You selected", item)

    orders.append(item)
    total = total + price(choice)

if len(orders) == 1:
    print("You ordered a", orders[0].lower())
elif len(orders) == 2:
    print("You ordered a", orders[0].lower(), "and a", orders[1].lower())
else:
    print("You ordered a", orders[0].lower(),
          ", a", orders[1].lower(),
          "and a", orders[2].lower())
print(f"Your total is ${total:.2f}")