"""Assessment 3.2 - Array program (dynamic, menu-driven)
Algorithm from Assessment 3.1: add each letter of the last name,
then remove each letter until the array is empty.
"""


def main():
    name = input("Enter your last name: ").strip().upper()
    if not name:
        print("Last name cannot be empty.")
        return

    capacity = len(name)
    array = [None] * capacity      # fixed-size array
    size = 0                       # number of letters currently stored
    next_letter = 0                # position in the name to add next

    def show():
        print("Array:", array, "| size =", size)

    while True:
        print("\n--- ARRAY MENU (" + name + ") ---")
        print("1. Add next letter")
        print("2. Add all letters")
        print("3. Remove last letter")
        print("4. Remove all letters until empty")
        print("5. Display array")
        print("6. Exit")
        choice = input("Choose (1-6): ").strip()

        if choice == "1":
            if size == capacity:
                print("Array is full.")
            else:
                letter = name[next_letter]
                array[size] = letter
                size += 1
                next_letter += 1
                print("Added:", letter)
                show()

        elif choice == "2":
            while size < capacity:
                letter = name[next_letter]
                array[size] = letter
                size += 1
                next_letter += 1
                print("Added:", letter)
            show()

        elif choice == "3":
            if size == 0:
                print("Array is empty.")
            else:
                size -= 1
                print("Removed:", array[size])
                array[size] = None
                next_letter -= 1
                show()

        elif choice == "4":
            if size == 0:
                print("Array is already empty.")
            while size > 0:
                size -= 1
                print("Removed:", array[size])
                array[size] = None
                next_letter -= 1
            show()
            print("Array is empty.")

        elif choice == "5":
            show()

        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 6.")


if __name__ == "__main__":
    main()