def stock_portfolio_tracker():
    # Hardcoded stock prices (in USD)
    stock_prices = {
        "AAPL": 180.50,
        "TSLA": 250.75,
        "MSFT": 300.20,
        "AMZN": 120.90,
        "GOOG": 135.60
    }
    
    print("Stock Portfolio Tracker")
    print("Available stocks:", ", ".join(stock_prices.keys()))
    
    portfolio = {}
    total_value = 0.0
    
    while True:
        print("\nMenu:")
        print("1. Add stock to portfolio")
        print("2. View current portfolio")
        print("3. Calculate total investment")
        print("4. Save portfolio to file")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            stock = input("Enter stock symbol: ").upper()
            if stock not in stock_prices:
                print("Invalid stock symbol. Available stocks:", ", ".join(stock_prices.keys()))
                continue
            
            try:
                quantity = int(input(f"Enter quantity of {stock}: "))
                if quantity <= 0:
                    print("Quantity must be positive")
                    continue
                
                portfolio[stock] = portfolio.get(stock, 0) + quantity
                print(f"Added {quantity} shares of {stock} to your portfolio.")
            except ValueError:
                print("Please enter a valid number for quantity.")
        
        elif choice == "2":
            if not portfolio:
                print("Your portfolio is empty.")
            else:
                print("\nCurrent Portfolio:")
                for stock, quantity in portfolio.items():
                    print(f"{stock}: {quantity} shares")
        
        elif choice == "3":
            if not portfolio:
                print("Your portfolio is empty.")
            else:
                total_value = 0.0
                print("\nPortfolio Value:")
                for stock, quantity in portfolio.items():
                    value = quantity * stock_prices[stock]
                    total_value += value
                    print(f"{stock}: {quantity} shares × ${stock_prices[stock]:.2f} = ${value:.2f}")
                print(f"\nTotal Investment Value: ${total_value:.2f}")
        
        elif choice == "4":
            if not portfolio:
                print("Cannot save - portfolio is empty.")
            else:
                filename = input("Enter filename to save (e.g., portfolio.txt): ")
                try:
                    with open(filename, 'w') as f:
                        f.write("Stock Portfolio\n")
                        f.write("===============\n")
                        for stock, quantity in portfolio.items():
                            value = quantity * stock_prices[stock]
                            f.write(f"{stock}: {quantity} shares @ ${stock_prices[stock]:.2f} = ${value:.2f}\n")
                        f.write(f"\nTotal Value: ${total_value:.2f}")
                    print(f"Portfolio saved to {filename}")
                except:
                    print("Error saving file.")
        
        elif choice == "5":
            print("Exiting portfolio tracker. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Start the portfolio tracker
stock_portfolio_tracker()