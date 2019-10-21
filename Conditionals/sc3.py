salary = 1000
good_bonus = 300
stellar_bonus = 500
performance = "stellar"

if performance == "stellar":
    salary += stellar_bonus
elif performance == "good":
    salary += good_bonus

print("Current salary: " + str(salary))