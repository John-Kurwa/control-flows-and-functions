def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price


original_price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount)

if discount >= 20:
        # figure in 2 decimal places
    print(f"Discount applied. Final price: ${final_price:.2f}")
else:
        # figure in 2 decimal places
    print(f"No discount applied. Final price: ${final_price:.2f}")

