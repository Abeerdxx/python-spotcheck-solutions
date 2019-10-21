salaries = [1200, 2500, 1800, 1600, 1800, 700, 3200, 1500, 1300, 1300, 850, 1900]
sum = 0
for salary in salaries:
    sum = sum + salary

total_average = sum / len(salaries)
above_average_salaries = []

for salary in salaries:
    if salary > total_average:
        above_average_salaries.append(salary)

print(above_average_salaries) # outputs: [2500, 1800, 1800, 3200, 1900]
