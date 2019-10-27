def determine_biggest(num1, num2):
    if num1 > num2:
        return num1
    
    # Note that we don't need an "else", because `return` ends the function!
    return num2

biggest = determine_biggest(91234, 91241)
print("Biggest number is " + biggest) # outputs: Biggest number is 91241