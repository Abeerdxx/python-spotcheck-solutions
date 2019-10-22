
people = ["Holly", "Irene", "Jessica", "Kyle", "Mike", "Nadine", "Olly"]
person_of_interest = "Olly"

index = 0
found = False

# added `and index...` to the end-condition
# now we guarantee we won't go out of bounds
while not found and index < len(people):

    if people[index] == person_of_interest:
        found = True
    else:
        index = index + 1

# we also want to show some indication of failure, hence this if-else
if found:
    print(person_of_interest + "'s index in the list is: " + str(index))
else:
    print("Couldn't find the index of " + person_of_interest)
