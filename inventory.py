import csv


class Shoe:
    """A class representing a shoe with inventory details."""

    def __init__(self, country, code, product, cost, quantity):
        """Initialize a Shoe object with the given attributes.

        Args:
            country (str): The country of origin.
            code (str): The style code of the shoe.
            product (str): The name of the shoe product.
            cost (float): The cost of the shoe.
            quantity (int): The quantity available in inventory.
        """
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        """Return the cost of the shoe as a formatted string.

        Returns:
            str: A string describing the product and its cost.
        """
        return f"{self.product} is costing R{self.cost}"

    def get_quantity(self):
        """Return the quantity of the shoe as a formatted string.

        Returns:
            str: A string describing the product and its quantity.
        """
        return f"The quantity of {self.product} is {self.quantity} units"

    def __str__(self):
        """Return a string representation of the Shoe object.

        Returns:
            str: A formatted string with all shoe details.
        """
        return (
            f"Country: {self.country}, Style code: {self.code}, "
            f"Product name: {self.product}, Item price: {self.cost}, "
            f"Quantity: {self.quantity}"
        )


# Global list to store Shoe objects
shoe_list = []


def read_shoes_data():
    """Read shoe data from inventory.txt and populate the shoe_list."""
    try:
        # Open the file with UTF-8 encoding to handle BOM
        with open("inventory.txt", "r", encoding="utf-8-sig") as file:
            # Read the CSV file as a dictionary
            reader = csv.DictReader(file)
            # Process each row to create a Shoe object
            for row in reader:
                # Capitalize country and product names for consistency
                country = row["Country"].title()
                code = row["Code"].upper()
                product = row["Product"].title()
                shoe = Shoe(
                    country=country,
                    code=code,
                    product=product,
                    cost=float(row["Cost"]),
                    quantity=int(row["Quantity"])
                )
                # Add the shoe to the global list
                shoe_list.append(shoe)
    except FileNotFoundError:
        print("Error: inventory.txt file not found!")
    except KeyError as error:
        print(f"Error: Missing expected column in CSV: {error}")
    except Exception as error:
        print(f"Error reading file: {error}")


def capture_shoes():

    """Capture user input to create a new Shoe object
     and add it to shoe_list."""
    print("\n--- Add a New Shoe ---")
    # Collect user input for shoe details
    country = input("Enter the country: ").title()
    code = input("Enter the style code (e.g., SKU12345): ").upper()
    product = input("Enter the product name: ").title()
    # Handle invalid cost input
    try:
        cost = float(input("Enter the cost (e.g., 2300): "))
    except ValueError:
        print("Error: Cost must be a number!")
        return
    # Handle invalid quantity input
    try:
        quantity = int(input("Enter the quantity: "))
    except ValueError:
        print("Error: Quantity must be a whole number!")
        return
    # Create and append the new shoe
    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)
    print(f"Shoe '{product}' added successfully!")


def view_all():

    """Display all shoes in the inventory
      in a table format with dynamic column widths."""

    if not shoe_list:
        print("\nNo shoes in the inventory!")
        return

    # Define column headers
    headers = ["Country", "Code", "Product", "Cost", "Quantity"]

    # Initialize maximum lengths with the header lengths
    max_country = len(headers[0])
    max_code = len(headers[1])
    max_product = len(headers[2])
    max_cost = len(headers[3])
    max_quantity = len(headers[4])

    # Calculate maximum length for each column based on data
    for shoe in shoe_list:
        max_country = max(max_country, len(shoe.country))
        max_code = max(max_code, len(shoe.code))
        max_product = max(max_product, len(shoe.product))
        cost_str = f"{shoe.cost:.2f}"
        max_cost = max(max_cost, len(cost_str))
        # Quantity is an integer, convert to string for length calculation
        quantity_str = str(shoe.quantity)
        max_quantity = max(max_quantity, len(quantity_str))

    # Print the table
    print("\n--- All Shoes in Inventory ---")
    # Print the header row
    print(
        f"{headers[0]:<{max_country}}  {headers[1]:<{max_code}}  "
        f"{headers[2]:<{max_product}}  {headers[3]:<{max_cost}}  "
        f"{headers[4]:<{max_quantity}}"
    )
    # Print the separator line
    # Add spaces between columns
    total_width = (
        max_country + max_code + max_product + max_cost + max_quantity + 8
    )
    print("-" * total_width)
    # Print each row of data
    for shoe in shoe_list:
        cost_str = f"{shoe.cost:.2f}"
        quantity_str = str(shoe.quantity)
        print(
            f"{shoe.country:<{max_country}}  {shoe.code:<{max_code}}  "
            f"{shoe.product:<{max_product}}  {cost_str:<{max_cost}}  "
            f"{quantity_str:<{max_quantity}}"
        )


def re_stock():
    """Find the shoe with the lowest quantity, restock it, and update the file."""
    if not shoe_list:
        print("\nNo shoes in the inventory to restock!")
        return
    # Find the shoe with the lowest quantity
    lowest_shoe = min(shoe_list, key=lambda shoe: shoe.quantity)
    print(
        f"\nShoe with lowest quantity: {lowest_shoe.product}"
        f" (Quantity: {lowest_shoe.quantity})"
    )
    # Ask user if they want to restock
    restock = input("Do you want to restock this shoe? (yes/no): ").lower()
    if restock != "yes":
        print("Restock cancelled.")
        return
    # Get additional quantity to restock
    try:
        additional_qty = int(input("Enter the number of units to add: "))
        if additional_qty < 0:
            print("Error: Quantity cannot be negative!")
            return
    except ValueError:
        print("Error: Please enter a valid number!")
        return
    # Update the shoe's quantity
    lowest_shoe.quantity += additional_qty
    print(
        f"Updated quantity for {lowest_shoe.product}: {lowest_shoe.quantity} units"
    )
    # Update the inventory file
    try:
        with open("inventory.txt", "w", encoding="utf-8-sig") as file:
            # Write the CSV header with capitalized names
            file.write("Country,Code,Product,Cost,Quantity\n")
            # Write each shoe's data
            for shoe in shoe_list:
                file.write(
                    f"{shoe.country},{shoe.code},"
                    f"{shoe.product},{shoe.cost},{shoe.quantity}\n"
                    )
        print("Inventory file updated successfully!")
    except Exception as error:
        print(f"Error updating file: {error}")


def search_shoe():
    """Search for a shoe by code and return the matching Shoe object.

    Returns:
        Shoe or None: The matching Shoe object if found, else None.
    """
    if not shoe_list:
        print("\nNo shoes in the inventory to search!")
        return None
    # Get the code to search for
    code = input("\nEnter the shoe code to search (e.g., SKU12345): ").upper()
    # Search for the shoe
    for shoe in shoe_list:
        if shoe.code == code:
            print(f"\nFound shoe: {shoe}")
            return shoe
    print(f"No shoe found with code {code}.")
    return None


def value_per_item():

    """Calculate and display the total value (cost * quantity)
      for each shoe with dynamic column widths."""
    if not shoe_list:
        print("\nNo shoes in the inventory to calculate value!")
        return

    # Define column headers
    headers = ["Product", "Value (R)"]

    # Initialize maximum lengths with the header lengths
    max_product = len(headers[0])
    max_value = len(headers[1])

    # Calculate maximum length for each column based on data
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        value_str = f"{value:.2f}"  # Format value with 2 decimal places
        max_product = max(max_product, len(shoe.product))
        max_value = max(max_value, len(value_str))

    # Print the table
    print("\n--- Value Per Item ---")
    # Print the header row
    print(f"{headers[0]:<{max_product}}  {headers[1]:<{max_value}}")
    # Print the separator line
    # Add space between columns
    total_width = max_product + max_value + 2
    print("-" * total_width)
    # Print each row of data
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        value_str = f"{value:.2f}"
        print(f"{shoe.product:<{max_product}}  {value_str:<{max_value}}")


def highest_qty():
    """Find and display the shoe with the highest quantity."""
    if not shoe_list:
        print("\nNo shoes in the inventory to check!")
        return
    # Find the shoe with the highest quantity
    highest_shoe = max(shoe_list, key=lambda shoe: shoe.quantity)
    print(
        f"\nShoe with highest quantity: {highest_shoe.product}"
        f" (Quantity: {highest_shoe.quantity})"
    )


def delete_shoe():
    """Delete a shoe from the inventory by code and update the file."""
    if not shoe_list:
        print("\nNo shoes in the inventory to delete!")
        return
    # Get the code of the shoe to delete
    code = input("\nEnter the shoe code to delete: ").upper()
    # Search for the shoe and remove it
    for i, shoe in enumerate(shoe_list):
        if shoe.code == code:
            shoe_list.pop(i)
            print(f"Shoe with code {code} deleted.")
            # Update the inventory file
            with open("inventory.txt", "w", encoding="utf-8-sig") as file:
                # Write the CSV header with capitalized names
                file.write("Country,Code,Product,Cost,Quantity\n")
                # Write each shoe's data
                for shoe in shoe_list:
                    file.write(
                        f"{shoe.country},{shoe.code},{shoe.product},"
                        f"{shoe.cost},{shoe.quantity}\n"
                        )
            return
    print(f"No shoe found with code {code}.")


def main_menu():
    """Display a menu to manage the shoe inventory system."""
    # Load initial data from the file
    read_shoes_data()
    # Run the menu loop
    while True:
        print("\n=== Shoe Inventory Management System ===")
        print("1. View all shoes")
        print("2. Add a new shoe")
        print("3. Delete a shoe")
        print("4. Restock a shoe (lowest quantity)")
        print("5. Search for a shoe by code")
        print("6. Calculate value per item")
        print("7. Find shoe with highest quantity")
        print("8. Exit")
        # Get user input
        choice = input("Enter your choice (1-8): ")
        # Execute the chosen function
        if choice == "1":
            view_all()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            delete_shoe()
        elif choice == "4":
            re_stock()
        elif choice == "5":
            search_shoe()
        elif choice == "6":
            value_per_item()
        elif choice == "7":
            highest_qty()
        elif choice == "8":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main_menu()