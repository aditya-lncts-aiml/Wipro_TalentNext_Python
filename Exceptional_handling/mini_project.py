# You had saved the items and their price details in a text file, which you purchased yesterday from a nearby supermarket.
# You need to know:
# 1. How many items did you purchase?
# 2. How many items are free?
# 3. What is the total amount you had to pay?
# 4. What is the discount amount?
# 5. What is the final amount you paid after the discount?
def process_purchase_file():
    try:
        filename = input("Enter the file name: ")
        with open(filename + ".txt", "r") as file:
            lines = file.readlines()

        items_purchased = 0
        free_items = 0
        total_amount = 0
        discount = 0

        for line in lines:
            line = line.strip()
            if not line:
                continue  # skip blank lines
            try:
                name, price = line.split()
                if name.lower() == "discount":
                    discount = int(price)
                elif price.lower() == "free":
                    free_items += 1
                else:
                    total_amount += int(price)
                    items_purchased += 1
            except ValueError:
                print(f"Skipping invalid line: {line}")

        final_amount = total_amount - discount

        print("\nNo of items purchased:", items_purchased)
        print("No of free items:", free_items)
        print("Amount to pay:", total_amount)
        print("Discount given:", discount)
        print("Final amount paid:", final_amount)

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("An error occurred:", e)

# Run the function
process_purchase_file()