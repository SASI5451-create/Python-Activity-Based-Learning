# ==============================================================================
# Case Study 10: Smart Canteen Order and Stock Management
# Student Name: NUKALA SASI KIRAN | Roll Number: 26000656 | Branch: CSE
# College: Dr. RVR NRI Institute of Technology
# ==============================================================================

# Canteen Menu dataset: list of lists [Item Name, Unit Price, Available Stock]
menu = [
    ["Idli", 20.0, 50],
    ["Dosa", 30.0, 40],
    ["Sambar", 10.0, 80],
    ["Tea", 8.0, 100],
    ["Coffee", 12.0, 60],
    ["Rice Meal", 60.0, 20]
]

# Display Menu
print("=" * 45)
print("             CAMPUS CANTEEN MENU             ")
print("=" * 45)
print(f"{'No.':<4}{'Item Name':<16}{'Price (Rs.)':>12}{'Stock':>10}")
print("-" * 45)
for i in range(len(menu)):
    item_no = i + 1
    name = menu[i][0]
    price = menu[i][1]
    stock = menu[i][2]
    print(f"{item_no:<4}{name:<16}{price:>12.2f}{stock:>10}")
print("=" * 45)

# Order Placement
order_items = []
order_qty = []
order_unit_prices = []
order_subtotals = []
bill_total = 0.0

num_items_to_order = int(input("\nHow many distinct items do you want to order? "))

for i in range(num_items_to_order):
    print(f"\nOrder item {i+1}:")
    choice = int(input("  Enter item number (1-6): ")) - 1
    
    if choice < 0 or choice >= len(menu):
        print("  Invalid item number! Skipping this item.")
    else:
        item_name = menu[choice][0]
        unit_price = menu[choice][1]
        available_stock = menu[choice][2]
        
        qty = int(input(f"  Enter quantity for {item_name}: "))
        
        if qty <= 0:
            print("  Quantity must be positive! Skipping this item.")
        elif qty > available_stock:
            print(f"  Insufficient stock for {item_name}! Available: {available_stock}, Requested: {qty}")
        else:
            # Deduct inventory stock
            menu[choice][2] = available_stock - qty
            item_cost = unit_price * qty
            bill_total += item_cost
            
            order_items.append(item_name)
            order_qty.append(qty)
            order_unit_prices.append(unit_price)
            order_subtotals.append(item_cost)
            print(f"  Added {qty} x {item_name} to cart.")

# Calculate Bulk Discount (10% if bill_total > Rs. 200)
if bill_total > 200.0:
    discount_amount = bill_total * 0.10
    discount_rate_str = "10%"
else:
    discount_amount = 0.0
    discount_rate_str = "0%"

final_payable = bill_total - discount_amount

# Display Customer Invoice
print("\n" + "=" * 45)
print("                 CANTEEN BILL                ")
print("=" * 45)
if len(order_items) == 0:
    print("No items ordered.")
else:
    print(f"{'Item':<16}{'Qty':>5}{'Rate':>10}{'Total':>12}")
    print("-" * 45)
    for i in range(len(order_items)):
        print(f"{order_items[i]:<16}{order_qty[i]:>5}{order_unit_prices[i]:>10.2f}{order_subtotals[i]:>12.2f}")
    print("-" * 45)
    print(f"{'Subtotal':<30} Rs. {bill_total:>10.2f}")
    print(f"{f'Discount ({discount_rate_str})':<30}-Rs. {discount_amount:>10.2f}")
    print("=" * 45)
    print(f"{'FINAL PAYABLE':<30} Rs. {final_payable:>10.2f}")
    print("=" * 45)

# End-of-Day Low Stock Alert Report (threshold < 5 units)
print("\n" + "-" * 45)
print("            LOW STOCK ALERT REPORT           ")
print("-" * 45)
low_stock_found = False
for i in range(len(menu)):
    item_name = menu[i][0]
    remaining_stock = menu[i][2]
    if remaining_stock < 5:
        print(f"  ALERT: {item_name} has critically low stock ({remaining_stock} units left)!")
        low_stock_found = True

if not low_stock_found:
    print("  All inventory items are adequately stocked.")
print("-" * 45)
