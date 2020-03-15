# In file main.py, how will you import a password variable from the config module?
from config import password
print(password)
# using relative path:
# from .module2 import foo2

from data.users import admin
print(admin)

from utils.math.fractions import first
print(first)

# From file1.py import function foo11 in file11.py
# using relative path:
# from .subfolder1.file11 import foo11
# import module file11 using absolute path:
# from folder1.subfolder1 import file11 