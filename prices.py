# -*- coding: utf-8 -*-
"""
Created on Fri May  3 22:43:13 2024

@author: Valentin Costea
"""

# Class: CEIS150
# Purpose: This program is used to find the number of prices in a list which
# are greater than the minimum price given by the user


# Initializing the variables
count = 0
sum = 0

# Geting the input for the user's full name
full_name = input("Enter your full name: ")

# Getting a floating point input for the minimum price
min_price = float(input("Enter the minimum price: "))

# Creating a hard-coded price list
# price_list = [69.0, 71.0, 84.5, 91.0, 67.4, 81.2, 84.6, 58.8, 79.3, 101.2]
price_list = [55.8, 63.2, 72.9, 88.1, 97.5, 64.3, 78.6, 81.9, 93.4, 106.8]

# Iterating through each price inside the list
for price in price_list:
    # Adding the current price to the sum variable
    sum += price

    # Checking if the price is greater than the minimum price
    if price > min_price:
        # Incrementing the count variable
        count += 1

# Giving the final output
# There was a logic error due to the nature of the floating point variables
# which gave an answer of 787.9999999999999. To solve that issue I've added
# the : .1f at the end of the sum variable in order to show only one decimal
print(f"Hello {full_name}, the minimum price is {min_price}")
print(f"There are {count} prices greater than the minimum price")
print(f"The total price is {sum: .1f}")
