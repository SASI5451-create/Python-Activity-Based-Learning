# ==============================================================================
# Case Study 4: Warehouse Inventory Reconciliation
# Student Name: NUKALA SASI KIRAN | Roll Number: 26000656 | Branch: CSE
# College: Dr. RVR NRI Institute of Technology
# ==============================================================================

# Parallel lists storing inventory dataset
items = ["Rice Bags", "Sugar Bags", "Oil Cans", "Wheat Bags", "Salt Packets", "Dal Bags"]
system_qty = [150, 80, 45, 200, 30, 60]
physical_qty = [143, 85, 38, 200, 18, 58]
reorder_level = 20
discrepancy_threshold = 5

print("=" * 70)
print("             WAREHOUSE INVENTORY RECONCILIATION REPORT            ")
print("=" * 70)
print(f"{'Item Name':<16}{'System Qty':>12}{'Physical Qty':>14}{'Diff':>8}  {'Status':<16}")
print("-" * 70)

discrepancy_count = 0
reorder_count = 0

for i in range(len(items)):
    diff = physical_qty[i] - system_qty[i]
    status = ""
    
    # Check for discrepancy exceeding threshold
    if abs(diff) > discrepancy_threshold:
        status += "DISCREPANCY "
        discrepancy_count += 1
        
    # Check if physical stock fell below reorder level
    if physical_qty[i] < reorder_level:
        status += "REORDER "
        reorder_count += 1
        
    # If within tolerance and above reorder level
    if status == "":
        status = "OK"
        
    print(f"{items[i]:<16}{system_qty[i]:>12}{physical_qty[i]:>14}{diff:>8}  {status.strip():<16}")

print("=" * 70)
print(f"Total Items Audited       : {len(items)}")
print(f"Discrepancies Detected    : {discrepancy_count}")
print(f"Items Requiring Reorder   : {reorder_count}")
print("=" * 70)
