
stock_prices = {
    "TCS": 3500,
    "INFY": 1500,
    "TVS": 1800,
    "TESLA": 2500
}


s_name = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))


if s_name in stock_prices:
    price = stock_prices[s_name]
    total_value = price * quantity

    print("Stock:", s_name)
    print("Price per stock:", price)
    print("Quantity:", quantity)
    print("Total investment value:", total_value)
else:
    print("Stock not found.")
