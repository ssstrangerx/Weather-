inventory = []

def create_product(sku, name, quantity):
    if not name.strip():
        print("Error: Product name cannot be empty.")
        return None
    try:
        quantity = int(quantity)
        if quantity < 0:
            print("Error: Quantity must be positive.")
            return None
    except ValueError:
        print("Error: Invalid quantity. Please enter a number.")
        return None

    return {"sku": sku, "name": name, "quantity": quantity}

def insert_product(product):
    for item in inventory:
        if item["sku"].lower() == product["sku"].lower():
            print("Error: Product with this SKU already exists.")
            return
    inventory.append(product)
    print(f"Product '{product['name']}' inserted successfully.")

def display_inventory():
    if not inventory:
        print("\nInventory is empty.")
        return
    print("\nCurrent Inventory:")
    print("SKU\t\tName\t\tQuantity")
    print("-----------------------------------")
    for item in inventory:
        print(f"{item['sku']}\t\t{item['name']}\t\t{item['quantity']}")

def search_by_sku(sku):
    for item in inventory:
        if item["sku"].lower() == sku.lower():
            print(f"Found: {item}")
            return
    print("Product not found.")

def search_by_name(name):
    for item in inventory:
        if item["name"].lower() == name.lower():
            print(f"Found: {item}")
            return
    print("Product not found.")

def delete_product(sku):
    for item in inventory:
        if item["sku"].lower() == sku.lower():
            inventory.remove(item)
            print(f"Product '{item['name']}' deleted successfully.")
            return
    print("Product not found.")

def buy_a_product(name):
    for item in inventory:
        if item["name"].lower() == name.lower():  # Fix: Match the product name
            try:
                qty = int(input("Enter purchase quantity: "))
                if qty <= 0:
                    print("Error: Quantity must be positive.")
                    return
                if item['quantity'] >= qty:
                    item['quantity'] -= qty
                    print(f"Purchase Successful! {qty} units of '{item['name']}' purchased.")
                    return
                else:
                    print(f"Error: Insufficient quantity. Only {item['quantity']} units available.")
                    return
            except ValueError:
                print("Error: Invalid quantity. Please enter a number.")
                return
    print("Error: Product not found.")  # Inform user if no product matches

def main():
    while True:
        print("\n--- Inventory Menu ---")
        print("1. Insert Product")
        print("2. Display Inventory")
        print("3. Search Product by SKU")
        print("4. Search Product by Name")
        print("5. Delete Product")
        print("6. Exit")
        print("7. Buy a Product")

        choice = input("Enter your choice: ")

        if choice == "1":
            sku = input("Enter SKU: ")
            name = input("Enter Product Name: ")
            qty = input("Enter Quantity: ")
            product = create_product(sku, name, qty)
            if product:
                insert_product(product)

        elif choice == "2":
            display_inventory()

        elif choice == "3":
            sku = input("Enter SKU to search: ")
            search_by_sku(sku)

        elif choice == "4":
            name = input("Enter Product Name to search: ")
            search_by_name(name)

        elif choice == "5":
            sku = input("Enter SKU to delete: ")
            delete_product(sku)

        elif choice == "6":
            print("Thank you, have a nice day!")
            break

        elif choice == "7":
            name = input("Enter Product Name: ")
            buy_a_product(name)

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
