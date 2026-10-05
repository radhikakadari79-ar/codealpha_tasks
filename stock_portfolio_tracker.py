stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 420
}

total_investment = 0

print("=== Stock Portfolio Tracker ===")
print("Available stocks:", ", ".join(stock_prices.keys()))

number_of_stocks = int(input("How many different stocks do you want to enter? "))

for i in range(number_of_stocks):
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        value = stock_prices[stock_name] * quantity
        total_investment += value
        print("Investment value:", value)
    else:
        print("Stock not found.")

print("\nTotal Investment Value:", total_investment)

save = input("Do you want to save the result to a text file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio_result.txt", "w") as file:
        file.write("Stock Portfolio Tracker\n")
        file.write("Total Investment Value: " + str(total_investment))
    print("Result saved to portfolio_result.txt")
