
import math

# Runtime input
fat = float(input("Enter fat percentage: "))
snf = float(input("Enter SNF percentage: "))
litres = float(input("Enter milk quantity in litres: "))

base_rate = float(input("Enter base rate per litre: "))
fat_step_rate = float(input("Enter rate per fat step: "))
snf_step_rate = float(input("Enter rate per SNF step: "))

fat_step_size = float(input("Enter fat step size: "))
snf_step_size = float(input("Enter SNF step size: "))

base_fat = float(input("Enter base fat percentage: "))
base_snf = float(input("Enter base SNF percentage: "))

# Calculate step counts
fat_steps = round((fat - base_fat) / fat_step_size)
snf_steps = round((snf - base_snf) / snf_step_size)

# Calculate rate and payment
rate_per_litre = (
    base_rate
    + fat_steps * fat_step_rate
    + snf_steps * snf_step_rate
)
amount = round(litres * rate_per_litre, 2)

print("\n--- Calculation Result ---")
print("Fat steps:", fat_steps)
print("SNF steps:", snf_steps)
print(f"Rate per litre: Rs {rate_per_litre:.2f}")
print(f"Amount: Rs {amount:.2f}")

# Chained comparisons and Boolean operators
fat_valid = 2.0 <= fat <= 7.0
snf_valid = snf >= base_snf
valid = fat_valid and snf_valid and litres >= 0

print("Fat valid:", fat_valid)
print("SNF valid:", snf_valid)
print("Input valid:", valid)

# Floating-point surprise
raw_steps = (4.2 - 3.5) / 0.1

print("\n--- Expression Analysis ---")
print("(4.2 - 3.5) / 0.1 =", repr(raw_steps))
print("round(raw_steps) =", round(raw_steps))
print("int(raw_steps) =", int(raw_steps))
print("math.floor(raw_steps) =", math.floor(raw_steps))

print("\n--- Unexpected Expressions ---")
print("0.1 + 0.2 =", repr(0.1 + 0.2))
print("0.1 + 0.2 == 0.3:", 0.1 + 0.2 == 0.3)

print("-7 // 2 =", -7 // 2)
print("int(-7 / 2) =", int(-7 / 2))
print("math.floor(-7 / 2) =", math.floor(-7 / 2))

print("2 ** 3 ** 2 =", 2 ** 3 ** 2)
print("-2 ** 2 =", -2 ** 2)
print("(-2) ** 2 =", (-2) ** 2)

