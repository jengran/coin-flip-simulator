import random

heads = 0
tails = 0

print("Coin Flip Simulator!")

while True:
    print("\nWhat do you want to do?")
    print("1. Flip the coin")
    print("2. Flip multiple times")
    print("3. See current score")
    print("4. Quit")

    choice = input("\nEnter 1, 2, 3, or 4: ")

    if choice == "1":
        result = random.choice(["Heads", "Tails"])
        print("Result:", result)
        if result == "Heads":
            heads += 1
        else:
            tails += 1

    elif choice == "2":
        flips = int(input("How many times do you want to flip?: "))
        for i in range(flips):
            result = random.choice(["Heads", "Tails"])
            if result == "Heads":
                heads += 1
            else:
                tails += 1
        print("Done! Flipped", flips, "times.")

    elif choice == "3":
        total = heads + tails
        print("\n--- Current Score ---")
        print("Heads:", heads)
        print("Tails:", tails)
        print("Total flips:", total)

    elif choice == "4":
        total = heads + tails
        print("\n--- Final Score ---")
        print("Heads:", heads)
        print("Tails:", tails)
        print("Total flips:", total)
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")
