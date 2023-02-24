#######################
# VALIDATION FUNCTIONS
#######################

def validate_year(x):
    digits = '0123456789'
    for char in x:   
        if char not in digits:
            return False
    x = int(x)                 
    if x >= 1960 and x <= 2022:
        return True
    else:
        return False

    
def validate_name(x):
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    whitespace = ' '
    letters = upper + lower + whitespace
    for char in x:   
        if char not in letters:
            return False
    return True    