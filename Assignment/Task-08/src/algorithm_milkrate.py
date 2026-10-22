
def rate_per_litre(fat, snf):
    """Calculate the rate per litre."""
    fat_steps = round((fat - 3.5) * 10)
    snf_steps = round((snf - 8.5) * 10)

    rate = (
        30.00
        + fat_steps * 0.40
        + snf_steps * 0.30
    )

    return round(rate, 2)


def payout(litres, fat, snf):
    """Calculate the milk payment."""
    return round(
        litres * rate_per_litre(fat, snf), 2
    )


print(f"Payment: {payout(10, 3.5, 8.5):.2f}")