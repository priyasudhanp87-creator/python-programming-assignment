
# TASK 5: Read Input and Convert Types

def read_number(prompt):
    while True:
        text = input(prompt).strip()

        try:
            return float(text)
        except ValueError:
            print("Invalid number! Enter a value like 8.5.")


print("=== Clerk Entry ===")

clerk_name = input("Enter clerk name: ").strip()

fat_percent = read_number(
    "Enter fat percentage (example 8.5): "
)

litres = read_number(
    "Enter milk quantity in litres: "
)

base_rate = read_number(
    "Enter base rate per litre (Rs): "
)

amount = litres * base_rate

print("\n=== Entry Summary ===")
print(f"{'Clerk':<18}: {clerk_name}")
print(f"{'Fat percentage':<18}: {fat_percent:>8.2f}%")
print(f"{'Milk quantity':<18}: {litres:>8.2f} L")
print(f"{'Base rate':<18}: Rs {base_rate:>8.2f}")
print(f"{'Amount':<18}: Rs {amount:>8.2f}")


