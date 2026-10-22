

# Task 7: Milk Rate Module Demonstration

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30


def rate_per_litre(fat, snf):
    """Calculate milk rate per litre."""
    fat_steps = round((fat - 3.5) * 10)
    snf_steps = round((snf - 8.5) * 10)

    rate = (
        BASE_RATE
        + fat_steps * FAT_STEP_VALUE
        + snf_steps * SNF_STEP_VALUE
    )
    return round(rate, 2)


def payout(litres, fat, snf):
    """Calculate total milk payment."""
    return round(litres * rate_per_litre(fat, snf), 2)


# Test the functions
print(" Milk Rate Calculator")
print("Rate:", rate_per_litre(3.5, 8.5))
print("Payment:", payout(10, 3.5, 8.5))
print("Rate:", rate_per_litre(4.2, 8.7))
print("Payment:", payout(8.5, 4.2, 8.7))
