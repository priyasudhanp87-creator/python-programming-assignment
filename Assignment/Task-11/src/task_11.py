import json

rate_card = {
    "base": "30.00",
    "fat": "0.40",
    "snf": "0.30"
}

with open("rate_card.json", "w") as file:
    json.dump(rate_card, file, indent=2)

print("Rate card file created successfully.")


from decimal import Decimal
import json
from pathlib import Path

RATE_CARD_FILE = Path("rate_card.json")

def load_rate_card():
    with RATE_CARD_FILE.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return {
        "base": Decimal(data["base"]),
        "fat": Decimal(data["fat"]),
        "snf": Decimal(data["snf"])
    }

def calculate_rate(rate_card, fat_steps, snf_steps):
    return (
        rate_card["base"]
        + Decimal(fat_steps) * rate_card["fat"]
        + Decimal(snf_steps) * rate_card["snf"]
    )

def calculate_payment(litres, rate):
    amount = Decimal(str(litres)) * rate
    return amount.quantize(Decimal("0.01"))

rate_card = load_rate_card()
print("Rate card loaded:", rate_card)

fat_steps = int(input("Enter fat steps: "))
snf_steps = int(input("Enter SNF steps: "))
litres = input("Enter milk quantity in litres: ")

rate = calculate_rate(rate_card, fat_steps, snf_steps)
amount = calculate_payment(litres, rate)

print(f"Rate per litre: Rs {rate:.2f}")
print(f"Payment amount: Rs {amount:.2f}")

