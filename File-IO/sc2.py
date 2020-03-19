goodies = ["Barnacle", "Circus", "Rake", "Cherry", "Steam", "Toothpaste", "Knee", "Coat"]

with open("example.txt", "a") as the_file:
    for item in goodies:
        if item[0] == "C":
            the_file.write(item + "\n")