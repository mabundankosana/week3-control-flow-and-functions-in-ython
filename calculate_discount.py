def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        
        return price


try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    
    final_price = calculate_discount(price, discount_percent)
    print(f"The final price is: ${final_price:.2f}")
except ValueError:
    print("Please enter valid numbers for the price and discount percentage.")
