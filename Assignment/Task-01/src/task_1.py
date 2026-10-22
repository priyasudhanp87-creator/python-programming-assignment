Add this task's src files here. Replace or remove this file when adding your actual files.

from dataclasses import dataclass

MIN_FAT = 3.0
MAX_FAT = 7.0
MIN_SNF = 7.5


@dataclass
class MilkEntry:
    farmer_id: str
    day: int
    litres: float
    fat: float
    snf: float
    shift: str
    rate: float

    def payment(self):
        return round(self.litres * self.rate, 2)


def main():
    entries = []
    count = int(input("Number of entries: "))

    if count <= 0:
        print("Error: Number of entries must be positive.")
        return

    for i in range(count):
        print(f"\nEntry {i + 1}")
        farmer_id = input("Farmer ID: ").strip()
        day = int(input("Day (1-10): "))
        litres = float(input("Litres: "))
        fat = float(input("Fat %: "))
        snf = float(input("SNF %: "))
        shift = input("Shift (Morning/Evening): ").strip().title()
        rate = float(input("Rate per litre (Rs): "))

        if (not farmer_id or not 1 <= day <= 10
                or litres < 0 or not 3.0 <= fat <= 7.0
                or snf < MIN_SNF
                or shift not in ("Morning", "Evening")
                or rate <= 0):
            print("Invalid entry. Check the entered values.")
            return

        entries.append(
            MilkEntry(farmer_id, day, litres, fat, snf, shift, rate)
        )

    total = 0.0

    print("\n=== Payment Summary ===")
    print("ID | Day | Litres | Fat | SNF | Shift | Rate | Amount")

    for e in entries:
        amount = e.payment()
        total += amount
        print(
            f"{e.farmer_id} | {e.day} | {e.litres:.2f} | "
            f"{e.fat:.2f} | {e.snf:.2f} | {e.shift} | "
            f"Rs {e.rate:.2f} | Rs {amount:.2f}"
        )

    print(f"Ten-day total: Rs {total:.2f}")
    print("Official rate must be checked against the current Aavin chart.")


if __name__ == "__main__":
    main()
