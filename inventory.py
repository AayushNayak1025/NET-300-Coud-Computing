# Question 3 — Inventory Restock Alert (User Input Version)

inventory = [
    {"item": "Rice", "threshold": 10},
    {"item": "Eggs", "threshold": 12},
    {"item": "Milk", "threshold": 6},
    {"item": "Bread", "threshold": 5},
    {"item": "Chicken", "threshold": 4},
    {"item": "Cooking Oil", "threshold": 3},
]

restock_count = 0

print("------ INVENTORY INPUT SYSTEM ------")

for product in inventory:
    stock = int(input(f"Enter stock for {product['item']}: "))

    print("Item:", product["item"])
    print("Stock:", stock)
    print("Threshold:", product["threshold"])

    if stock < product["threshold"]:
        print("Status: Restock Alert 🚨")
        restock_count += 1
    else:
        print("Status: Stock is sufficient ✅")

    print("-----------------------------")

print("\nTotal items needing restock:", restock_count)