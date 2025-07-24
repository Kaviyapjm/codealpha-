stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 130,
    "AMZN": 140,
    "INFY": 1500
}

portfolio = {}
print("Welcome to the Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))
print("Enter 'done' when finished.\n")

while True:
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not in list. Try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if quantity < 0:
            print("Quantity cannot be negative.")
            continue
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")

total_investment = 0
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    total_investment += value
    print(f"{stock} - Qty: {qty}, Price: ₹{price}, Total: ₹{value}")

print(f"\nTotal Investment Value: ₹{total_investment}")

save = input("\nDo you want to save this to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w",encoding="utf=8") as file:
        file.write(" Portfolio Summary\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = qty * price
            file.write(f"{stock} - Qty: {qty}, Price: ₹{price}, Total: ₹{value}\n")
        file.write(f"\nTotal Investment: ₹{total_investment}\n")
    print("Portfolio saved to 'portfolio_summary.txt'")
else:
    print("Okay, file not saved.")
