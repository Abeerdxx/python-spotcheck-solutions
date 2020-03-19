from random import randint

random_number = randint(1, 10)

while True:
    input_number = int(input("Guess what my number is!\n"))
    if random_number == input_number:
        print("You got it!")
        break
    elif random_number < input_number:
        print(f"Not yet. My number is smaller than {input_number}. Try again")
    else:
        print(f"Not yet. My number is bigger than {input_number}. Try again")
