# int, int -> string
# A recursive function that takes a base 10 number (num) and an integer between 2 and 16 (b)
# and returns the string representation of the number, num, converted to the base, b.
def convert(num, b):
    # next_digit is a string conversion of the remainder of current division
    # next_num is the quotient result of current division
    # next_iter is the string result from the last recursive call
    next_digit = str(num % b)
    if next_digit == "10":
        next_digit = "A"
    elif next_digit == "11":
        next_digit = "B"
    elif next_digit == "12":
        next_digit = "C"
    elif next_digit == "13":
        next_digit = "D"
    elif next_digit == "14":
        next_digit = "E"
    elif next_digit == "15":
        next_digit = "F"
    if num // b == 0:
        return next_digit
    next_num = num // b
    next_iter = convert(next_num, b)
    return next_iter + next_digit
