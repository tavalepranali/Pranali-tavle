

# Hardcoded stock dictionary with prices as required by task scope
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 175
}

def stock_portfolio_tracker():
    print("=" * 50)
    print("       CODEALPHA STOCK PORTFOLIO TRACKER       ")
    print("=" * 50)
    
    # Display available stock list
    print("\nAvailable Stocks & Prices:")
    for symbol, price in stock_prices.items():
        print(f" - {symbol}: ${price}")
    print("-" * 50)

    portfolio = {}
    total_investment = 0.0

    while True:
        # User input for stock symbol
        stock_name = input("\nEnter Stock Symbol (e.g., AAPL, TSLA) or type 'done' to finish: ").strip().upper()
        
        if stock_name == "DONE":
            break
        
        # Check if the stock is available
        if stock_name not in stock_prices:
            print("❌ Stock not found! Please choose from the available list.")
            continue
        
        # Get stock quantity from user
        try:
            quantity = int(input(f"Enter quantity of '{stock_name}' shares bought: "))
            if quantity <= 0:
                print("❌ Quantity must be 1 or greater.")
                continue
        except ValueError:
            print("❌ Invalid input. Please enter a valid integer quantity.")
            continue

        # Calculate values and update portfolio
        price_per_share = stock_prices[stock_name]
        total_stock_value = price_per_share * quantity
        
        if stock_name in portfolio:
            portfolio[stock_name]['quantity'] += quantity
            portfolio[stock_name]['total_value'] += total_stock_value
        else:
            portfolio[stock_name] = {
                'quantity': quantity,
                'price': price_per_share,
                'total_value': total_stock_value
            }
        
        print(f"✅ Added {quantity} x {stock_name}! (Value: ${total_stock_value})")

    # Display portfolio summary
    if not portfolio:
        print("\nNo stocks were added to your portfolio.")
        return

    print("\n" + "=" * 50)
    print("              PORTFOLIO SUMMARY              ")
    print("=" * 50)
    
    summary_text = "PORTFOLIO SUMMARY\n" + "=" * 50 + "\n"
    
    for stock, details in portfolio.items():
        line = f"Stock: {stock} | Qty: {details['quantity']} | Price: ${details['price']} | Total Value: ${details['total_value']}\n"
        print(line.strip())
        summary_text += line
        total_investment += details['total_value']

    total_line = f"\nTotal Investment Value: ${total_investment}\n"
    print("-" * 50)
    print(total_line.strip())
    summary_text += "-" * 50 + total_line

    # Save summary to .txt file (File Handling)
    save_choice = input("\nDo you want to save the result to a text file? (yes/no): ").strip().lower()
    if save_choice in ['yes', 'y']:
        with open("portfolio_summary.txt", "w", encoding="utf-8") as file:
            file.write(summary_text)
        print("✅ Portfolio summary successfully saved to 'portfolio_summary.txt'!")

if __name__ == "__main__":
    stock_portfolio_tracker()