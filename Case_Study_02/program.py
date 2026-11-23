# ==============================================================================
# Case Study 2: Retail Billing with Multiple Discount Rules
# Student Name: NUKALA SASI KIRAN | Roll Number: 26000656 | Branch: CSE
# College: Dr. RVR NRI Institute of Technology
# ==============================================================================

# Initialize parallel lists for product items
products = []
categories = []
quantities = []
prices = []

# Input total number of products
num_products = int(input("Enter number of products: "))

# Gather product details
for i in range(num_products):
    print(f"\nProduct {i+1}:")
    p_name = input("  Product name: ")
    p_cat = input("  Category (Grocery/Electronics/Luxury): ")
    p_qty = int(input("  Quantity: "))
    p_price = float(input("  Unit price (Rs.): "))
    
    products.append(p_name)
    categories.append(p_cat)
    quantities.append(p_qty)
    prices.append(p_price)

# Calculate Subtotal (sum of item total before discount)
subtotal = 0.0
for i in range(num_products):
    subtotal += quantities[i] * prices[i]

# Determine Tiered Discount based on subtotal
if subtotal > 10000.0:
    discount_percent = 10.0
elif subtotal > 5000.0:
    discount_percent = 5.0
else:
    discount_percent = 0.0

discount_amount = subtotal * (discount_percent / 100.0)

# Enforce Maximum Discount Cap of Rs. 2,000
if discount_amount > 2000.0:
    discount_amount = 2000.0

taxable_amount = subtotal - discount_amount

# Calculate Category-Specific Tax per Product
# Category Rates: Grocery 5%, Electronics 12%, Luxury 18%
total_tax = 0.0
item_taxes = []
item_totals = []

for i in range(num_products):
    item_total = quantities[i] * prices[i]
    item_totals.append(item_total)
    
    cat_lower = categories[i].strip().lower()
    if cat_lower == "grocery":
        tax_rate = 0.05
    elif cat_lower == "electronics":
        tax_rate = 0.12
    elif cat_lower == "luxury":
        tax_rate = 0.18
    else:
        tax_rate = 0.05  # Default general rate
        
    item_tax = item_total * tax_rate
    item_taxes.append(item_tax)
    total_tax += item_tax

final_payable = taxable_amount + total_tax

# Display Formatted Tax Invoice
print("\n" + "=" * 65)
print("                          RETAIL INVOICE                         ")
print("=" * 65)
print(f"{'Product':<18}{'Category':<14}{'Qty':>5}{'Price':>10}{'Total':>10}{'Tax':>8}")
print("-" * 65)
for i in range(num_products):
    print(f"{products[i]:<18}{categories[i]:<14}{quantities[i]:>5}{prices[i]:>10.2f}{item_totals[i]:>10.2f}{item_taxes[i]:>8.2f}")
print("-" * 65)
print(f"{'Subtotal':<47} Rs.{subtotal:>10.2f}")
print(f"{f'Discount ({discount_percent:.0f}%)':<47}-Rs.{discount_amount:>10.2f}")
print(f"{'Taxable Amount':<47} Rs.{taxable_amount:>10.2f}")
print(f"{'Total Tax':<47} Rs.{total_tax:>10.2f}")
print("=" * 65)
print(f"{'FINAL PAYABLE AMOUNT':<47} Rs.{final_payable:>10.2f}")
print("=" * 65)
