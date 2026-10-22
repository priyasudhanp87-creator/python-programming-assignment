
from decimal import Decimal, ROUND_HALF_UP

def calculate_payment(fat, snf, litres, total_10_days,
                      base_rate=Decimal("32.00"),
                      fat_step_rate=Decimal("0.45"),
                      snf_step_rate=Decimal("0.30")):

    # Convert inputs to Decimal safely
    fat = Decimal(str(fat)).quantize(Decimal("0.01"))
    snf = Decimal(str(snf)).quantize(Decimal("0.01"))
    litres = Decimal(str(litres))
    total_10_days = Decimal(str(total_10_days))

    # Reference readings and step size
    reference_fat = Decimal("3.00")
    reference_snf = Decimal("8.00")
    step_size = Decimal("0.10")

    # Calculate steps; retain fractional steps
    fat_steps = (fat - reference_fat) / step_size
    snf_steps = (snf - reference_snf) / step_size

    # Calculate rate per litre
    rate = (
        base_rate
        + fat_steps * fat_step_rate
        + snf_steps * snf_step_rate
    )

    # Bonus applies only when supply exceeds 500 litres
    bonus_rate = (
        Decimal("0.50")
        if total_10_days > Decimal("500")
        else Decimal("0.00")
    )

    final_rate = rate + bonus_rate
    payment = (litres * final_rate).quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )

    return fat_steps, snf_steps, rate, bonus_rate, final_rate, payment


if __name__ == "__main__":
    fat = input("Enter fat reading (e.g. 4.25): ")
    snf = input("Enter SNF reading (e.g. 8.50): ")
    litres = input("Enter today's milk quantity in litres: ")
    total_10_days = input("Enter total supply in 10 days: ")

    result = calculate_payment(fat, snf, litres, total_10_days)

    fat_steps, snf_steps, rate, bonus, final_rate, payment = result

    print(f"Fat steps: {fat_steps}")
    print(f"SNF steps: {snf_steps}")
    print(f"Rate before bonus: Rs {rate:.2f}")
    print(f"Bonus per litre: Rs {bonus:.2f}")
    print(f"Final rate per litre: Rs {final_rate:.2f}")
    print(f"Total payment: Rs {payment:.2f}")

