

"""
Task 9: Implement and Test the Milk Payment Calculator
"""

BASE_RATE = 30.00
STANDARD_FAT = 3.5
STANDARD_SNF = 8.5
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

# Assumed FAT range: replace with the official assignment limits.
MIN_FAT = 2.0
MAX_FAT = 6.0


def calculate_rate(fat, snf):
    """Calculate the milk rate per litre."""
    fat_steps = round((fat - STANDARD_FAT) * 10)
    snf_steps = round((snf - STANDARD_SNF) * 10)

    rate = (
        BASE_RATE
        + fat_steps * FAT_STEP_VALUE
        + snf_steps * SNF_STEP_VALUE
    )
    return round(rate, 2)


def calculate_payment(quantity, fat, snf):
    """Validate inputs and calculate the payment."""
    if quantity < 0:
        raise ValueError("Milk quantity cannot be negative.")

    if not MIN_FAT <= fat <= MAX_FAT:
        raise ValueError(
            f"FAT must be between {MIN_FAT}% and {MAX_FAT}%."
        )

    if snf < 0:
        raise ValueError("SNF cannot be negative.")

    rate = calculate_rate(fat, snf)
    payment = round(quantity * rate, 2)

    return rate, payment


def run_tests():
    """Automatically test normal, boundary and invalid cases."""
    tests = [
        ("Standard values", 10, 3.5, 8.5, 30.00, 300.00),
        ("FAT above standard", 8.5, 4.2, 8.7, 33.40, 283.90),
        ("FAT below standard", 10, 3.0, 8.0, 27.50, 275.00),
        ("Minimum FAT", 5, MIN_FAT, 8.5,
         calculate_rate(MIN_FAT, 8.5), None),
        ("Maximum FAT", 5, MAX_FAT, 8.5,
         calculate_rate(MAX_FAT, 8.5), None),
    ]

    print("\nAUTOMATED TEST RESULTS")
    print("-" * 75)

    for name, quantity, fat, snf, expected_rate, expected_payment in tests:
        rate, payment = calculate_payment(quantity, fat, snf)

        assert rate == expected_rate
        if expected_payment is not None:
            assert payment == expected_payment

        print(
            f"{name}: PASS | Rate = Rs. {rate:.2f}"
            f" | Payment = Rs. {payment:.2f}"
        )

    invalid_tests = [
        ("Negative quantity", -1, 3.5, 8.5),
        ("FAT below allowed range", 5, MIN_FAT - 0.1, 8.5),
        ("FAT above allowed range", 5, MAX_FAT + 0.1, 8.5),
    ]

    for name, quantity, fat, snf in invalid_tests:
        try:
            calculate_payment(quantity, fat, snf)
            print(f"{name}: FAIL")
            assert False, f"{name} should have been rejected"
        except ValueError:
            print(f"{name}: PASS (invalid input rejected)")

    print("\nAll automated tests passed.")


def main():
    print("MILK PAYMENT CALCULATOR")

    while True:
        try:
            quantity_text = input(
                "\nEnter milk quantity in litres (or Q to quit): "
            ).strip()

            if quantity_text.lower() == "q":
                break

            quantity = float(quantity_text)
            fat = float(input("Enter FAT percentage: "))
            snf = float(input("Enter SNF percentage: "))

            rate, payment = calculate_payment(quantity, fat, snf)

            print(f"Rate per litre: Rs. {rate:.2f}")
            print(f"Total payment: Rs. {payment:.2f}")

        except ValueError as error:
            print(f"Invalid input: {error}")

    print("\nCalculator closed.")


if __name__ == "__main__":
    main()
1