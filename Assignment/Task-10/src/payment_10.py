

from decimal import Decimal, ROUND_HALF_UP
from time import perf_counter

BASE_RATE = 30.00
STANDARD_FAT = 3.5
STANDARD_SNF = 8.5
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30


def round_money(value):
    """Round a monetary amount to two decimal places."""
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def calculate_float_rate(fat, snf):
    fat_steps = round((fat - STANDARD_FAT) * 10)
    snf_steps = round((snf - STANDARD_SNF) * 10)
    return BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE


def calculate_decimal_rate(fat, snf):
    fat_steps = int(
        (fat - Decimal("3.5")) * Decimal("10")
    )
    snf_steps = int(
        (snf - Decimal("8.5")) * Decimal("10")
    )

    rate = (
        Decimal("30.00")
        + Decimal(fat_steps) * Decimal("0.40")
        + Decimal(snf_steps) * Decimal("0.30")
    )
    return rate


def make_entries(count):
    """Create repeatable sample payment entries."""
    entries = []

    for i in range(count):
        quantity = 5.0 + (i % 20) * 0.25
        fat = 3.0 + (i % 11) * 0.1
        snf = 8.0 + (i % 7) * 0.1
        entries.append((quantity, fat, snf))

    return entries


def compare_totals(entries):
    # Float arithmetic, rounding only the final total.
    start = perf_counter()
    float_raw_total = 0.0

    for quantity, fat, snf in entries:
        float_raw_total += quantity * calculate_float_rate(fat, snf)

    float_total_time = perf_counter() - start
    float_total_rounded = round(float_raw_total + 1e-9, 2)

    # Float arithmetic, rounding every payment.
    start = perf_counter()
    float_payment_total = 0.0

    for quantity, fat, snf in entries:
        payment = round(
            quantity * calculate_float_rate(fat, snf) + 1e-9, 2
        )
        float_payment_total += payment

    float_each_time = perf_counter() - start
    float_each_rounded = round(float_payment_total, 2)

    # Decimal arithmetic, rounding only the final total.
    start = perf_counter()
    decimal_raw_total = Decimal("0.00")

    for quantity, fat, snf in entries:
        q = Decimal(str(quantity))
        f = Decimal(str(fat))
        s = Decimal(str(snf))
        decimal_raw_total += q * calculate_decimal_rate(f, s)

    decimal_total_time = perf_counter() - start
    decimal_total_rounded = round_money(decimal_raw_total)

    # Decimal arithmetic, rounding every payment.
    start = perf_counter()
    decimal_payment_total = Decimal("0.00")

    for quantity, fat, snf in entries:
        q = Decimal(str(quantity))
        f = Decimal(str(fat))
        s = Decimal(str(snf))
        payment = round_money(q * calculate_decimal_rate(f, s))
        decimal_payment_total += payment

    decimal_each_time = perf_counter() - start
    decimal_each_rounded = round_money(decimal_payment_total)

    print(f"\nNumber of payments: {len(entries):,}")
    print(f"Float total, round at end: Rs. {float_total_rounded:.2f}")
    print(f"Decimal total, round at end: Rs. {decimal_total_rounded:.2f}")
    print(
        "Difference (float - Decimal): Rs. "
        f"{float_total_rounded - float(decimal_total_rounded):.2f}"
    )
    print(f"Float total time: {float_total_time:.6f} seconds")
    print(f"Decimal total time: {decimal_total_time:.6f} seconds")

    print(f"Float, round each payment: Rs. {float_each_rounded:.2f}")
    print(f"Decimal, round each payment: Rs. {decimal_each_rounded:.2f}")
    print(f"Float per-payment time: {float_each_time:.6f} seconds")
    print(f"Decimal per-payment time: {decimal_each_time:.6f} seconds")


def compare_rate_table(entries):
    """Compare recalculation with dictionary rate lookups."""
    start = perf_counter()

    recalculated_total = 0.0
    for quantity, fat, snf in entries:
        recalculated_total += quantity * calculate_float_rate(fat, snf)

    recalculation_time = perf_counter() - start

    # Precompute each distinct FAT/SNF pair.
    start = perf_counter()
    rate_table = {}

    for _, fat, snf in entries:
        key = (fat, snf)
        if key not in rate_table:
            rate_table[key] = calculate_float_rate(fat, snf)

    precomputation_time = perf_counter() - start

    start = perf_counter()
    lookup_total = 0.0
    for quantity, fat, snf in entries:
        lookup_total += quantity * rate_table[(fat, snf)]

    lookup_time = perf_counter() - start

    print("\nRATE TABLE COMPARISON")
    print(f"Distinct FAT/SNF pairs (k): {len(rate_table)}")
    print(f"Recalculation time: {recalculation_time:.6f} seconds")
    print(f"Table creation time: {precomputation_time:.6f} seconds")
    print(f"Dictionary lookup time: {lookup_time:.6f} seconds")
    print(f"Extra table space: O(k) entries")
    print(f"Totals agree: {abs(recalculated_total - lookup_total) < 0.01}")


def main():
    for count in (300, 6000, 150000):
        entries = make_entries(count)
        compare_totals(entries)

    compare_rate_table(make_entries(150000))


if __name__ == "__main__":
    main()
