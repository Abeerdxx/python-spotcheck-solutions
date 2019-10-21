username = "serious_cat612"
correctUsername = "serious_dog612"

# Two ways to check that `username` is not an empty string:

# if username 
    # - this works because Python sees an empty string as "False"

# or:

# if username != "" 
#   - simple comparison of strings

if username:
    if username == correctUsername:
        print("Welcome back, serious_dog612")
    else:
        print("Sorry, that username is incorrect")
else:
    print("Please enter a username")
