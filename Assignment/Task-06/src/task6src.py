

"""
Task 6: Organise Milk Payment Logic into Functions.

This program calculates milk payments and totals for ten days.
The base rate of Rs. 44.00 per litre is provisional and must
be replaced if the assignment specifies an official rate formula.
"""

from decimal import Decimal, ROUND_HALF_UP

# Global constant: read by functions, never modified inside them.
BASE_RATE_PER_LITRE = Decimal("44.00")
MONEY_PLACES = Decimal("0.01")


def money(amount):
    """Round a monetary amount to two decimal places."""
    return amount.quantize(MONEY_PLACES, rounding=ROUND_HALF_UP)


def rate_per_litre():
    """Return the configured fixed rate per litre."""
    return BASE_RATE_PER_LITRE


def payout(litres, rate):
    """Calculate and return the payment for a quantity of milk."""
    return money(litres * rate)


def ten_day_total(entries):
    """Return the total payment for all entries in a ten-day period."""
    total = Decimal("0.00")

    for entry in entries:
        total += entry["payment"]

    return money(total)


def get_positive_decimal(prompt):
    """Read a non-negative decimal number and reject invalid input."""
    while True:
        text = input(prompt).strip()

        try:
            value = Decimal(text)

            if not value.is_finite() or value < 0:
                print("Enter a valid non-negative number.")
                continue

            return value

        except Exception:
            print("Invalid number. Try again (example: 8.5).")


def main():
    """Collect milk entries and display their payment totals."""
    entries = []
    rate = rate_per_litre()

    print("MILK PAYMENT CALCULATOR")
    print(f"Rate per litre: Rs. {rate:.2f}")

    for day in range(1, 11):
        print(f"\nDay {day}")

        litres = get_positive_decimal("Enter litres of milk: ")
        payment = payout(litres, rate)

        entry = {
            "day": day,
            "litres": litres,
            "payment": payment
        }
        entries.append(entry)

        print(f"Litres: {litres:.2f}")
        print(f"Payment: Rs. {payment:.2f}")

    total_litres = sum(
        (entry["litres"] for entry in entries),
        Decimal("0")
    )
    total_payment = ten_day_total(entries)

    print("\n" + "=" * 38)
    print("TEN-DAY PAYMENT SUMMARY")
    print("=" * 38)
    print(f"{'Total litres':<20} {total_litres:>12.2f}")
    print(f"{'Total payment (Rs.)':<20} {total_payment:>12.2f}")


if __name__ == "__main__":
    main()
