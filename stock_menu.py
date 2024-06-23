# -*- coding: utf-8 -*-
"""
Created on Sun May 19 23:33:16 2024

@author: Valentin Costea
"""

from datetime import datetime
from stock_class import Stock, DailyData
from account_class import Traditional, Robo
import matplotlib.pyplot as plt
import csv


# Function For Adding Stocks to the Tracking List
def add_stock(stock_list):
    option = ""

    while option != "0":
        print("\nAdd Stock ----")

        symbol = input("Enter Stock Symbol: ").upper()
        name = input("Enter Company Name: ")
        shares = float(input("Enter Number of Shares: "))

        new_stock = Stock(symbol, name, shares)
        stock_list.append(new_stock)

        print()
        option = input(
            "Stock Added - Press Enter to Add Another Stock or 0 to Stop: ")


# Remove stock and all daily data


# Function For Deleting Stocks to the Tracking List
def delete_stock(stock_list):
    print("\nDelete Stock ----")

    # Display the stock list
    print("Stock List: [", end="")
    for stock in stock_list:
        print(stock.symbol + " ", end="")
    print("]")  # End the stock list

    # Input symbol to delete
    symbol = input("Which stock do you want to delete?: ").upper()

    found = False
    i = 0

    # Search and delete the stock
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            stock_list.pop(i)
            break   # Once found, stop searching
        i += 1

    # Output the result
    if found:
        print(f"Deleted {symbol}")
    else:
        print(f"Error: Stock Symbol '{symbol}' not found.")

    _ = input("Press Enter to Continue ***")


# List stocks being tracked
def list_stocks(stock_list):
    print("\nStock List ----")
    # The :<10 and :<20 operators format the table setting minimum character requirements per column
    print(f"{'Symbol':<10} {'Name':<20} {'Shares':<10}")
    print("=" * 40)

    for stock in stock_list:
        # print(stock.symbol," " * (14-len(stock.symbol)),stock.name," " * (14-len(stock.name)),stock.shares)
        # I've changed the output format because the company names are the biggest being listed
        print(f"{stock.symbol:<10} {stock.name:<20} {stock.shares:<10}")

    print()
    _ = input("Press Enter to Continue ***")


# Adding Daily Stock Data
def add_stock_data(stock_list):
    print("\nAdd Daily Stock Data ----")
    print("Stock List: [", end="")
    for stock in stock_list:
        print(stock.symbol, " ", end="")
    print("]")
    symbol = input("Which stock do you want to use?: ").upper()
    found = False
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            current_stock = stock
    if found == True:
        print("Ready to add data for: ", symbol)
        print("Enter Data Separated by Commas - Do Not use Spaces")
        print("Enter a Blank Line to Quit")
        print("Enter Date,Price,Volume")
        print("Example: 8/28/20,47.85,10550")
        data = input("Enter Date,Price,Volume: ")
        while data != "":
            date, price, volume = data.split(",")
            daily_data = DailyData(date, float(price), float(volume))

            current_stock.add_data(daily_data)
            data = input("Enter Date,Price,Volume: ")
        print("Date Entry Complete")
    else:
        print("Symbol Not Found ***")
    _ = input("Press Enter to Continue ***")


def investment_type(stock_list):
    print("\nInvestment Account ---")
    balance = float(input("What is your initial balance: "))
    number = input("What is your account number: ")
    acct = input("Do you want a Traditional (t) or Robo (r) account: ")
    if acct.lower() == "r":
        years = float(input("How many years until retirement: "))
        robo_acct = Robo(balance, number, years)
        print("Your investment return is ", robo_acct.investment_return())
        print("\n\n")
    elif acct.lower() == "t":
        trad_acct = Traditional(balance, number)
        temp_list = []
        print("Choose stocks from the list below: ")
        while True:
            print("Stock List: [", end="")
            for stock in stock_list:
                print(stock.symbol, " ", end="")
            print("]")
            symbol = input(
                "Which stock do you want to purchase, 0 to quit: ").upper()
            if symbol == "0":
                break
            shares = float(input("How many shares do you want to buy?: "))
            found = False
            for stock in stock_list:
                if stock.symbol == symbol:
                    found = True
                    current_stock = stock
            if found == True:
                current_stock.shares += shares
                temp_list.append(current_stock)
                print("Bought ", shares, "of", symbol)
            else:
                print("Symbol Not Found ***")
        trad_acct.add_stock(temp_list)


# Function to create stock chart


def display_stock_chart(stock_list, symbol):
    # Initialize lists
    date = []
    price = []
    volume = []

    # Initializing the company name
    company = ""

    # Getting the Data for the Chart
    for stock in stock_list:
        if stock.symbol == symbol:
            company = stock.name
            for dailyData in stock.DataList:
                date.append(dailyData.date)
                price.append(dailyData.close)
                volume.append(dailyData.volume)

    # Ploting the data
    plt.plot(date, price)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(company)
    plt.show()


# Display Chart


def display_chart(stock_list):
    print("\Stock Chart ---")

    # Display the stock list
    print("Stock List: [", end="")
    for stock in stock_list:
        print(stock.symbol + " ", end="")
    print("]")  # End the stock list

    # Input symbol to delete
    symbol = input("Pick a stock for a chart?: ").upper()

    found = False

    # Search and delete the stock
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            current_stock = stock
            break   # Once found, stop searching

    # Output the result
    if found:
        display_stock_chart(stock_list, current_stock.symbol)
    else:
        print(f"Error: Stock Symbol '{symbol}' not found.")

    _ = input("Press Enter to Continue ***")

 # Get price and volume history from Yahoo! Finance using CSV import.


def import_stock_csv(stock_list):
    print("\nAdd stock historical data --- ")

    # Display the stock list
    print("Stock List: [", end="")
    for stock in stock_list:
        print(stock.symbol + " ", end="")
    print("]")  # End the stock list

    symbol = input("Enter stock symbol: ").upper()
    filename = input("Enter the file name: ")

    for stock in stock_list:
        if stock.symbol == symbol:
            with open(filename, newline='') as stockdata:
                datareader = csv.reader(stockdata, delimiter=',')
                next(datareader)
                for row in datareader:
                    daily_data = DailyData(
                        str(row[0]), float(row[4]), float(row[6]))
                    stock.add_data(daily_data)

    display_report(stock_list)

    # Display Report for All Stocks


def display_report(stock_list):
    print("\nStock Report ---")

    for stock in stock_list:
        print(f"Report for: {stock.symbol} {stock.name}")
        print(f"Shares: {stock.shares}\n")

        # variable initialization
        count = 0
        price_total = 0
        volume_total = 0
        lowPrice = 999999999999.99
        highPrice = 0.0
        lowVolume = 999999999999
        highVolume = 0

        # Working with the stock data
        for daily_data in stock.DataList:
            count += 1
            price_total += daily_data.close
            volume_total += daily_data.volume

            if daily_data.close < lowPrice:
                lowPrice = daily_data.close

            if daily_data.close > highPrice:
                highPrice = daily_data.close

            if daily_data.volume < lowVolume:
                lowVolume = daily_data.volume

            if daily_data.volume > highVolume:
                highVolume = daily_data.volume

            priceChange = highPrice - lowPrice
            print(daily_data.date, daily_data.close, daily_data.volume)

        # Stock data summary
        if count > 0:
            print("\nSummary ---")
            print(f"Low Price: ${lowPrice:,.2f}")
            print(f"High Price: ${highPrice:,.2f}")
            print(f"Average Price: ${(price_total/count):,.2f}")
            print(f"Low Volume: {lowVolume:,.0f}")
            print(f"High Volume: {highVolume:,.0f}")
            print(f"Average Volume: {(volume_total/count):,.2f}")
            print(f"Change in Price: ${priceChange:,.2f}")
            print(f"Profit/Loss: ${(priceChange*stock.shares):,.2f}")
        else:
            print("*** No daily history ***")

        # Spacing
        print("\n\n\n")

    # Ending report
    print("--- Report Complete ---")
    _ = input("Press Enter to Continue ***")


def main_menu(stock_list):
    option = ""
    while True:
        print("Stock Analyzer ---")
        print("1 - Add Stock")
        print("2 - Delete Stock")
        print("3 - List stocks")
        print("4 - Add Daily Stock Data (Date, Price, Volume)")
        print("5 - Show Chart")
        print("6 - Investor Type")
        print("7 - Load Data")
        print("0 - Exit Program")
        option = input("Enter Menu Option: ")
        if option == "0":
            print("Goodbye")
            break

        if option == "1":
            add_stock(stock_list)
        elif option == "2":
            delete_stock(stock_list)
        elif option == "3":
            list_stocks(stock_list)
        elif option == "4":
            add_stock_data(stock_list)
        elif option == "5":
            display_chart(stock_list)
        elif option == "6":
            investment_type(stock_list)
        elif option == "7":
            import_stock_csv(stock_list)
        else:

            print("Goodbye")

# Begin program


def main():
    stock_list = []
    main_menu(stock_list)


# Program Starts Here
if __name__ == "__main__":
    # execute only if run as a stand-alone script
    main()
