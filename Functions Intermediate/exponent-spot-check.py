


def get_power_of(exponent):

    def inner(x):
        return x ** exponent
    return inner

calc_power_of_2 = get_power_of(2)
calc_power_of_4 = get_power_of(4)
print(calc_power_of_2(5)) #25
print(calc_power_of_4(2)) #16

