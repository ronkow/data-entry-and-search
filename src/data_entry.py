'''
IMPROVING YOUR PROGRAM
1. Validate all user entries.
2. Split a long function into two or more shorter functions.
3. Delete unnecessary lines of code.
4. Write more comments.
5. Follow python best practices and recommended style.
Style guide:
https://peps.python.org/pep-0008/
'''

import os

from file import file_to_list_of_dicts, list_of_dicts_to_file

from data_search import search

############################
# RETRIEVE AND PRINT RECORDS
############################

def print_records(lod):
    print(f'name\tgender\tbirthyear')
    for i in lod:
        print(f"{i['name']}\t{i['gender']}\t{i['birthyear']}")    

                
def retrieve_all_data_lod(filepath):
    try:
        lod = file_to_list_of_dicts(filepath)
    except FileNotFoundError as e:
        print('ERROR:',e)
    else:
        print_records(lod)

    
#def retrieve_all_data_lol(filepath):
#    lol = file_to_list_of_lists(filepath)
#    for i in lol:
#        print(f'{i[0]}\t{i[1]}\t{i[2]}')
        
###################
# VALIDATION
###################

def validate_year(x):
    digits = '0123456789'
    for char in x:   
        if char not in digits:
            return False   # return statement exits the function.
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
            return False   # return statement exits the function.
    return True    

###################
# ENTER NEW RECORD
###################

def enter_name():
    print('Enter the name:')
    n = input()
    valid = validate_name(n)
    
    while not valid:  # if valid is False, not valid is True
        print('Invalid entry. Enter a name with all letters:')
        n = input()
        valid = validate_name(n)  
    return n


def enter_gender():
    print('Enter the gender:')
    g = input().lower()
    
    while g not in ('m', 'f'):   # membership operator: in, not in
        print('Invalid entry. Enter a gender m or f:')
        g = input()
    return g


def enter_birthyear():
    print('Enter the birth year:')  # 1960 to 2022
    y = input()
    valid = validate_year(y)
    
    while not valid:
        print('Invalid entry. Enter a year from 1960 to 2022:')
        y = input()
        valid = validate_year(y)
    return y


def enter_another_record():
    print()
    print('Do you want to enter another record? (y/n)')
    x = input()
    print()
    while x not in ('y', 'n', 'Y', 'N'):
        print('Invalid entry. Enter y or n:')
        x = input()
        
    return x


def enter_record():    
    lod = []
    
    n = enter_name().title()
    g = enter_gender().upper()
    y = enter_birthyear()
    record = {'name':n, 'gender':g, 'birthyear': y}
    lod.append(record)
    
    yes_no = enter_another_record()
    
    while yes_no == 'y':
        n = enter_name().title()
        g = enter_gender().upper()
        y = enter_birthyear()
        record = {'name':n, 'gender':g, 'birthyear': y}
        lod.append(record)
        
        yes_no = enter_another_record()
    
    print('RECORDS ENTERED')
    print('---------------')
    print_records(lod)
                         
    return lod
    

#################
# USER OPTIONS
#################

def select_option():
    print('Select an option:')
    print('1. Retrieve all records')
    print('2. Enter a record')
    print('3. Search for a record')
    print('4. Quit')
    x = input()
    return x

###################
# MAIN
###################

def main():
    #DATA_PATH = ('data/data.csv')
    
    DATA_PATH = os.path.join('data','data.csv')
    
    while True:
        print()
        x = select_option()
        if x == '1':
            print()
            retrieve_all_data_lod(DATA_PATH)
            
        elif x == '2':
            print()
            lod = enter_record()
            
            try:
                list_of_dicts_to_file(DATA_PATH, lod)
            except FileNotFoundError as e:
                print('ERROR:',e)
                print('We are so sorry your record cannot be saved!')
                
            
        elif x == '3':
            print()
            lod = search(DATA_PATH)
            
        elif x == '4':
            return         # quit

            
if __name__ == '__main__':
    main()
