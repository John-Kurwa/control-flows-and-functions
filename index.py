original_price = float(input("Enter the original price: "))
calculate_discount = float(input("Enter the discount percentage: "))


if calculate_discount >= 20:
        discount_percent = original_price * (calculate_discount / 100)
        final_price = original_price - discount_percent
        print(f"Discount applied. Final price: Ksh{final_price:.2f}")
        
else:
    print(f"No discount applied. Final price: Ksh{original_price:.2f}")
