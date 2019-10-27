def add(x, y):
    total = x + y
    if total > 100:
        print("Whoa")
    else:
        print("You can do better")

add(3, 5) # outputs: You can do better
add(3, 99) # outputs: Whoa