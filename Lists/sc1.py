stuff = []

stuff.append("Cheese")
stuff.append("Curtain")
stuff.append("Castle")

new_thing = "Curtain"

if new_thing not in stuff:
    stuff.append(new_thing)
else:
    print("That's already in there")