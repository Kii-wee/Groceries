def main(): #while loop ch 5
    groceries = []
    bought = set()

    print("=== Grocery List Manager ===\n")

    while True:  # Main while loop (ch 5)
        print("1. Add items")
        print("2. Mark as bought")
        print("3. Remove item")
        print("4. Show list")
        print("5. Quit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            add_items(groceries)
        elif choice == "2":
            mark_bought(groceries, bought)
        elif choice == "3":
            remove_item(groceries, bought)
        elif choice == "4":
            show_list(groceries, bought)
        elif choice == "5":
            print("\nFinal Grocery List:")
            show_list(groceries, bought, final=True)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")


def add_items(groceries): # Void function (ch 6), while loop and sentinel value (ch 5)
    print("\nEnter grocery items one per line.")
    print("Type 'done' when finished.") #sentinel value

    while True:  #loop w sentinel
        item = input("Item: ").strip()

        if item.lower() == "done":
            break

        if item:
            groceries.append(item)
            print(f"Added: {item}")
        else:
            print("Please enter an item or 'done'.")


def mark_bought(groceries, bought): #Void function, prints output (ch 6)
    if not groceries:
        print("Your list is empty!")
        return

    show_list(groceries, bought)

    try:
        num = int(input("\nEnter the number to mark as bought: ")) - 1
        if 0 <= num < len(groceries):
            bought.add(num)
            print(f"Marked as bought: {groceries[num]}")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number.")


def remove_item(groceries, bought): #Void function (ch 6)
    if not groceries:
        print("Your list is empty!")
        return

    show_list(groceries, bought)

    try:
        num = int(input("\nEnter the number to remove: ")) - 1
        if 0 <= num < len(groceries):
            item = groceries.pop(num)
            bought.discard(num)
            bought = {x - 1 if x > num else x for x in bought}
            print(f"Removed: {item}")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number.")


def show_list(groceries, bought, final=False): ## VOID FUNCTION, CHAPTER 6. Prints list with for loop (ch 5)
    if not groceries:
        print("  (list is empty)")
        return

    for i in range(len(groceries)):  # Loop
        mark = "[x]" if i in bought else "[ ]"
        if final:
            print(f"   {mark} {groceries[i]}")
        else:
            print(f"{i + 1}. {mark} {groceries[i]}")


if __name__ == "__main__":
    main()