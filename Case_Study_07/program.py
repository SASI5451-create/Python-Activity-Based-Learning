# ==============================================================================
# Case Study 7: Repeated Transaction Detection
# Student Name: NUKALA SASI KIRAN | Roll Number: 26000656 | Branch: CSE
# College: Dr. RVR NRI Institute of Technology
# ==============================================================================

# Banking transactions represented as tuples: (transaction_id, amount, merchant)
transactions = [
    ("T001", 500.00, "Amazon"),
    ("T002", 1200.00, "Flipkart"),
    ("T003", 500.00, "Amazon"),
    ("T004", 750.00, "Swiggy"),
    ("T005", 1200.00, "Flipkart"),
    ("T006", 300.00, "Zomato"),
    ("T007", 500.00, "Amazon")
]

print("=" * 65)
print("            BANK REPEATED TRANSACTION DETECTION REPORT           ")
print("=" * 65)

# List to record duplicate pairs
flagged_pairs = []

# Nested loop to compare each pair of transactions once (i < j)
for i in range(len(transactions)):
    tid_a, amt_a, mer_a = transactions[i]
    for j in range(i + 1, len(transactions)):
        tid_b, amt_b, mer_b = transactions[j]
        
        # Check for same transaction amount and merchant
        if amt_a == amt_b and mer_a == mer_b:
            pair_record = (tid_a, tid_b, amt_a, mer_a)
            flagged_pairs.append(pair_record)

# Display report
if len(flagged_pairs) > 0:
    print(f"{'TxID-1':<10}{'TxID-2':<10}{'Amount (Rs.)':>14}  {'Merchant':<15}")
    print("-" * 65)
    for pair in flagged_pairs:
        t1, t2, amount, merchant = pair
        print(f"{t1:<10}{t2:<10}{amount:>14.2f}  {merchant:<15} [POTENTIAL DUPLICATE]")
else:
    print("No repeated or duplicate transactions detected.")

print("=" * 65)
print(f"Total Transactions Scanned : {len(transactions)}")
print(f"Total Duplicate Pairs Found: {len(flagged_pairs)}")
print("=" * 65)
