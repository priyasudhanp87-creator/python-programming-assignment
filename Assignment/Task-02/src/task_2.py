
from decimal import Decimal
import sys

# 1. Explore Python values and types
print("1. PYTHON VALUES AND TYPES")

values = [10, 10.0, "10", True, [10, 8.5]]

for value in values:
    print(repr(value), "->", type(value))


# 2. Division operators
print("\n2. DIVISION OPERATORS")

print("7 / 2  =", 7 / 2)
print("7 // 2 =", 7 // 2)
print("7 % 2  =", 7 % 2)
print("-7 // 2 =", -7 // 2)
print("-7 % 2  =", -7 % 2)


# 3. Floating-point precision
print("\n3. FLOATING-POINT PRECISION")

print("0.1 + 0.2 =", 0.1 + 0.2)
print("0.1 + 0.2 == 0.3 ->", 0.1 + 0.2 == 0.3)

print(
    'Decimal("0.1") + Decimal("0.2") == Decimal("0.3") ->',
    Decimal("0.1") + Decimal("0.2") == Decimal("0.3")
)


# 4. Calculate total using float
def total_float(items):
    total = 0.0

    for amount in items:
        total += float(amount)

    return total


# 5. Complete total_decimal()
def total_decimal(items):
    total = Decimal("0.00")

    for amount in items:
        total += Decimal(amount)

    return total


# 6. Compare Decimal(float(amount))
def total_decimal_from_float(items):
    total = Decimal("0.00")

    for amount in items:
        total += Decimal(float(amount))

    return total


# 7. Integer paise alternative
def total_integer_paise(items):
    total = 0

    for amount in items:
        value = Decimal(amount)
        paise = value * 100

        if paise != paise.to_integral_value():
            raise ValueError("Use at most two decimal places.")

        total += int(paise)

    return total


# 8. Round after each addition
def total_rounded_float(items):
    total = 0.0

    for amount in items:
        total = round(total + float(amount), 2)

    return total


# 9. Runtime payment input
print("\n4. PAYMENT TOTAL - RUNTIME INPUT")

while True:
    try:
        count = int(input("How many payment amounts? "))

        if count < 1:
            print("Enter at least one payment.")
            continue

        break

    except ValueError:
        print("Enter a valid whole number.")

payments = []

for i in range(count):
    while True:
        amount = input(
            f"Enter payment {i + 1} (example 440.00): "
        ).strip()

        try:
            value = Decimal(amount)

            if not value.is_finite() or value < 0:
                print("Enter a valid non-negative amount.")
                continue

            if value * 100 != (value * 100).to_integral_value():
                print("Use at most two decimal places.")
                continue

            payments.append(amount)
            break

        except Exception:
            print("Invalid amount. Example: 440.00")


# 10. Compare payment calculation methods
print("\n5. PAYMENT TOTAL COMPARISON")

print("Payments:", payments)
print("Float total:", repr(total_float(payments)))
print("Decimal total:", total_decimal(payments))
print("Decimal(float(amount)):",
      total_decimal_from_float(payments))

paise_total = total_integer_paise(payments)

print("Integer paise:", paise_total, "paise")
print("Integer paise in rupees:",
      f"{Decimal(paise_total) / 100:.2f}")

print("Rounded float total:",
      f"{total_rounded_float(payments):.2f}")


# 11. Repeated-payment precision experiment
print("\n6. REPEATED-PAYMENT EXPERIMENT")

experiment_payments = ["33.40"] * 1000 + ["0.10"] * 3

print("Payment count:", len(experiment_payments))
print("Float total:", repr(total_float(experiment_payments)))
print("Decimal total:", total_decimal(experiment_payments))
print("Decimal(float(amount)) total:",
      total_decimal_from_float(experiment_payments))

experiment_paise = total_integer_paise(experiment_payments)

print("Integer paise:", experiment_paise)
print("Total in rupees:",
      f"{Decimal(experiment_paise) / 100:.2f}")

print("Rounded float total:",
      f"{total_rounded_float(experiment_payments):.2f}")


# 12. Memory usage
print("\n7. MEMORY SIZE (BYTES)")

print("Float:", sys.getsizeof(33.40))
print("Decimal:", sys.getsizeof(Decimal("33.40")))
print("Integer paise:", sys.getsizeof(3340))


# 13. Complexity analysis
print("\n8. COMPLEXITY ANALYSIS")

print("Time complexity for each total function: O(n)")
print("Running total auxiliary space: O(1)")
print("Payment list storage: O(n)")
