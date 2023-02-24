import os

from file import file_to_list_of_dicts
from file import list_of_dicts_to_file

from validation import validate_name
from validation import validate_year

from data_search import search

############################
# RETRIEVE AND PRINT RECORDS
############################

def print_records(lod):
    print(f'NAME\tGENDER\tBIRTH YEAR')
    for i in lod:
        print(f"{i['name']}\t{i['gender']}\t{i['birthyear']}")    

                
def retrieve_all_data(filepath):
    try:
        lod = file_to_list_of_dicts(filepath)
    except FileNotFoundError as e:
        print('ERROR:',e)
    else:
        print('ALL RECORDS')
        print('-----------')
        print_records(lod)

            
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
    print('DATA ENTRY')
    print('----------')
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
    print('STUDENT DATASTORE')
    print('-----------------')
    print('Select an option:')
    print('1. Retrieve all records.')
    print('2. Enter a record.')
    print('3. Search for a record.')
    print('4. Quit.')
    x = input()
    
    while x not in ('1', '2', '3', '4'):
        print('Invalid entry. Enter 1, 2, 3 or 4:')
        x = input()
    return x

###################
# MAIN
###################

def main():
    DATA_DIR = 'data-entry-and-search-python\data'
    DATA_PATH = os.path.join(DATA_DIR, 'data.csv')
    
    while True:
        print()
        x = select_option()
        if x == '1':
            print()
            retrieve_all_data(DATA_PATH)
            
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
            return

            
if __name__ == '__main__':
    main()
