def print_unicode_table(start, end):
    for i in range(start, end + 1):
        print(f"{i}: {chr(i)}")


print_unicode_table(200, 1000)
