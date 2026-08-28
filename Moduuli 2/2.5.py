talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

talent_to_pound = talents * 20
total_pounds = talent_to_pound + pounds

pounds_to_lots = total_pounds * 32
total_lots = pounds_to_lots + lots

total_grams = total_lots * 13.3

kilogram = int(total_grams / 1000)
grams = total_grams % 1000

print("The weigth in modern units: ")
print(f"{kilogram} kilograms and {grams:.2f} grams.")

