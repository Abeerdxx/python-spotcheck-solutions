def get_unicode_table(start, end):
    for i in range(start, end + 1):
        print(f"{i}: {chr(i)}")


get_unicode_table(200, 1000)


"""
Should handle the case of invalid range?
No
In the documentation of chr() is written:
ValueError will be raised if i is outside that range.

https://docs.python.org/3/library/functions.html#chr
"""