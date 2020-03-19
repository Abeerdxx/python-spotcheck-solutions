import csv

stocks = [
    {"name": "Apple", "price": 246},
    {"name": "Tesla", "price": 328},
    {"name": "Microsoft", "price": 140},
    {"name": "Amazon"},
    {"name": "Lionsgate", "price": 8},
    {"name": "Netflix", "price": 276},
    {"name": "Google"},
    {"name": "Activision", "price": 55},
]

with open("stocks.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write the header row - *outside* of the for loop
    csv_writer.writerow(["Company", "Price"])

    for stock in stocks:
        name = stock["name"]
        price = 0

        # Make sure the price exists before trying to access it
        if "price" in stock:
            price = stock["price"]

        csv_writer.writerow([name, price])
