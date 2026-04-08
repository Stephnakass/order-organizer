orders = []

while True:
    name = input("Enter customer name (or type done): ")

    if name.lower() == "done":
        break

    while True:
        try:
            total = float(input("Enter order total: $"))
            break
        except:
            print("Please enter a valid number")

    orders.append({"name": name, "total": total})

print()
print("Order Summary")
print("-------------")

grand_total = 0

for order in orders:
    print(f"{order['name']}: ${order['total']:.2f}")
    grand_total += order['total']

print("-------------")
print(f"Total sales: ${grand_total:.2f}")