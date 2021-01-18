# int -> boolean
# Recursive function that takes an integer (n) and returns True or False 
# if after following the below rules, the integer can be reduced to exactly 42.
#   1) If n is even, then you may give back n/2 bears.
#   2) If n is divisible by 3 or 4, then you may multiply the last two digits of n and give back this many bears.
#   3) If n is divisible by 5, then you may give back 42 bears.
def bears(n):
    # base2 is a boolean value resulting from the recursive result after meeting the first criteria
    # base34 is a boolean value resulting from the recursive result after meeting the second criteria
    # base5 is a boolean value resulting from the recursive result after meeting the third criteria
    # new_n is the new value of n after its been reduced
    # ones and tens are the int values of the last and second to last digits of n
    if n == 42:
        return True
    elif n < 42:
        return False
    if n % 2 == 0:
        new_n = n/2
        if new_n == 42:
            return True
        elif new_n > 42:
            base2 = bears(new_n)
            if base2 == True:
                return True
    if (n % 3 == 0) or (n % 4 == 0):
        ones = n % 10
        tens = n // 10
        new_n = n - (ones * tens)
        if new_n == 42:
            return True
        elif new_n > 42:
            base34 = bears(new_n)
            if base34 == True:
                return True
    if n % 5 == 0:
        new_n = n - 42
        if new_n > 42:
            base5 = bears(new_n)
            if base5 == True:
                return True
    return False