from random import uniform

exchange_rate = uniform(3.5, 5.5)   # random number between 3.5 to 5.5
amount_of_shekels = float(input("Please enter the amount of Shekels you would like to exchange:\n"))
amount_of_euros = int(amount_of_shekels * exchange_rate)

print(f"The amount of euros after the converting is {amount_of_euros}. The exchange rate is {exchange_rate}")
