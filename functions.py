stack = []

def push():
    try:
        item = int(input("Enter items to push: "))
        stack.append(item)
        print(f"Pushed{item}")
    except ValueError:
        print("Only integer values are alllowed")


def pop():
    if not stack:
        print("Stack is empty")
    else:
        popped = stack.pop()
        print(f"Popped{popped}")


def peek():
    if not stack:
        print("Stack is empty")
    else:
        print(f"Top item is {stack[-1]}")


def display():
    if not stack:
        print("Stack is empty")
    else:
        print(f"Stack items: {stack}")


# def exit():
#     pass

while True:
    print(
        """
        1. Push
        2. Pop
        3. Peek
        4. Display
        5. Exit"""
    )

    choice = int(input("Enter your choice: "))
    if choice == "1":
        push()
    elif choice == "2":
        pop()
    elif choice == "3":
        peek()
    elif choice == "4":
        display()
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
    print()  
    print("Current stack:", stack)  
