# File Handling Example for Agentic AI

# File name
FILE_NAME = "memory.txt"

# Save memory
def save_memory():
    memory = input("Enter a memory: ")

    with open(FILE_NAME, "a") as file:
        file.write(memory + "\n")

    print("Memory saved successfully!")

# Show all memories
def show_memory():
    try:
        with open(FILE_NAME, "r") as file:
            print("\n----- Agent Memory -----")
            print(file.read())

    except FileNotFoundError:
        print("No memory found.")

# Main Menu
while True:

    print("\n=== Agent Memory System ===")
    print("1. Save Memory")
    print("2. Show Memory")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        save_memory()

    elif choice == "2":
        show_memory()

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")