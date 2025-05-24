# Shoe Inventory Management System

## About
Hey, warehouse champs! Struggling to keep tabs on your shoe stock? Our Shoe Inventory Management System is your new best friend. This CLI app makes inventory a breeze - add, delete, restock, or search shoes with ease, all stored in a simple CSV file (`inventory.txt`). Need to spot low stock or calculate total stock value? We’ve got you covered with features like restocking alerts and value-per-item breakdowns. Perfect for store managers, it’s easy to use and saves you time. Got questions? Drop an issue on our GitHub repo, and let’s keep your warehouse running smooth!

## Setup
Follow these steps to set up the Shoe Inventory Management System locally:

1. **Fork the repository**:
   - Click the 'Fork' button at the top right corner of the [repository's GitHub page](https://github.com/XolaniGatebe/Inventory-Manager-System.git).
   - This creates a copy in your GitHub account.

2. **Clone your forked repository**:
     ```bash
     git clone https://github.com/XolaniGatebe/Inventory-Manager-System.git
     ```
   - Navigate to the directory:
     ```bash
     cd shoe-inventory
     ```

3. **Install Python libraries**:
   - Ensure Python 3.8+ is installed (`python --version` or `python3 --version`).
   - No external libraries are required (uses standard `csv` module), but check `requirements.txt` if added:
     ```bash
     pip install -r requirements.txt
     ```
     - Note: If `requirements.txt` is empty or absent, skip this step.

4. **Run the application**:
   - Execute the main script:
     ```bash
     python3 inventory.py
     ```
   - The CLI menu launches, offering options to manage the inventory.

5. **Navigate to the app**:
   - Interact via the CLI menu (e.g., select “1” to view all shoes, “2” to add a shoe).
   - Requires `inventory.txt` in the same directory for data storage (sample file included in the repository).

## Making Changes and Pushing to Your Fork
After modifying the application, push changes to your forked GitHub repository:

```bash
git add -u
git commit -m "Your commit message (e.g., Added shoe category feature)"
git push origin main
