
# TASK 3: Choose Variables and Name the Constants

# Named constants: UPPER_CASE convention
MIN_FAT_PERCENT = 3.0
MAX_FAT_PERCENT = 7.0
MIN_SNF_PERCENT = 7.5


def read_float(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = float(input(prompt))

            if minimum is not None and value < minimum:
                print(f"Enter a value >= {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Enter a value <= {maximum}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Enter a number.")


print("=== Named Constants and Runtime Input ===")

# Get rate values from the user at runtime
BASE_RATE = read_float("Enter base rate per litre: ", 0)
FAT_RATE = read_float("Enter fat rate: ", 0)
SNF_RATE = read_float("Enter SNF rate: ", 0)

# Get milk details at runtime
litres = read_float("Enter milk quantity in litres: ", 0)

fat_percent = read_float(
    "Enter fat percentage (3 to 7): ",
    MIN_FAT_PERCENT,
    MAX_FAT_PERCENT
)

snf_percent = read_float(
    "Enter SNF percentage (minimum 7.5): ",
    MIN_SNF_PERCENT
)

# Illustrative formula only
rate_per_litre = (
    BASE_RATE
    + fat_percent * FAT_RATE
    + snf_percent * SNF_RATE
)

payment_amount = round(litres * rate_per_litre, 2)

print("\n=== Payment Result ===")
print(f"Base rate: Rs {BASE_RATE:.2f}")
print(f"Rate per litre: Rs {rate_per_litre:.2f}")
print(f"Milk quantity: {litres:.2f} litres")
print(f"Payment amount: Rs {payment_amount:.2f}")

# Dynamic typing
print("\n=== Dynamic Typing ===")
value = 10
print(value, type(value).__name__)

value = "ten"
print(value, type(value).__name__)

# Multiple assignment and swapping
print("\n=== Swapping ===")
a, b = 5, 9
print("Before swap:", a, b)

a, b = b, a
print("After swap:", a, b)

print("\nUPPER_CASE is a convention; Python does not enforce constants.")
