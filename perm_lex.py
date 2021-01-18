# string -> list of strings
# Recursive function that determines all the permutations of an input string (a)
# in lexicographic (dictionary) order. These permutations are return in a list.
def perm_gen_lex(a): 
    #str_list is the list of all permutations at a given level of recursion (in dictionary order)
    # reduc_str is the reduced input string with the first letter removed
    # str_list_init is the list result from the last recursive function call
    if len(a) == 1:
        return [a]
    str_list = []
    for letter in a:
        reduc_str = a.replace(letter, "")
        str_list_init = perm_gen_lex(reduc_str)
        for string in str_list_init:
            string = letter + string
            str_list.append(string)
    return str_list

 