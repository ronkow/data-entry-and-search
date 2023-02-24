from file import file_to_list_of_dicts

from validation import validate_year
from validation import validate_name


# STEP 6
# Prompt the user if he/she wishes to do another search.
# Validate the user entry (y or n).
# Return y or n.
def another_search():
    print()
    print('Do you want to do another search? (y/n)')
    x = input()
    print()
    while x not in ('y', 'n', 'Y', 'N'):
        print('Invalid entry. Enter y or n:')
        x = input()
    return x.lower()


# STEP 5
# If result r is an empty list, print a message.
# If result r is not an empty list, print the search results.
# Return None.
def print_result(lod): # lod: list of dicts
    print('MATCHED RECORDS')
    print('---------------')
    print('NAME\tGENDER\tBIRTH YEAR')  # \t tab character
    for d in lod:
        print(d['name'], end='\t')    
        print(d['gender'], end='\t')
        print(d['birthyear'], end='\n')    
    return None


def match_record(lod, matched_records, key, q):
    for d in lod:
        record_value = d[key].lower() 
        if q.lower() == record_value:
            matched_records.append(d)
    return matched_records


# STEP 4
# Match the field x and query q with every record in lod.
# Return any matched record.
def search_database(lod, x, q): # lod: list of dictionaries
    matched_records = []
    
    if x == '1': # name
        matched_records = match_record(lod, matched_records, 'name', q)
                        
    elif x == '2': # gender
        matched_records = match_record(lod, matched_records, 'gender', q)
                        
    else: # birthyear
        matched_records = match_record(lod, matched_records, 'birthyear', q)
        
    return matched_records


# STEP 3
# Prompt the user to enter the text (name, gender or birth year) to search for.
# Validate all user entry: 
#   name must be all letters and spaces only
#   gender must be m or f
#   birth year must be a four digit number 19xx or 20xx 
# Return a valid query text (name, gender or birth year).
def enter_query(x):
    if x == '1':
        print('Enter the name:')
        query = input()
        
        valid = validate_name(query)
    
        while not valid:
            print('Invalid entry. Enter a name with all letters:')
            query = input()
            valid = validate_name(query)
        
    elif x == '2':
        print('Enter the gender:')
        query = input().lower()
        
        while query not in ('m', 'f'):
            print('Invalid entry. Enter a gender m or f:')
            query = input()
        
    else:
        print('Enter the birthyear:')
        query = input()
        
        valid = validate_year(query)
    
        while not valid:
            print('Invalid entry. Enter a year from 1960 to 2022:')
            query = input()
            valid = validate_year(query)
    
    return query


# STEP 2
# Prompt the user to select a search field (1, 2 or 3).
# Validate the user entry (1, 2 or 3).
# Return the selected option (1, 2 or 3).
def select_search_field():
    print('DATA SEARCH')
    print('-----------')
    print('Select an option:')
    print('1. Search by name.')
    print('2. Search by gender.')
    print('3. Search by birth year.')
    x = input()
    
    while x not in ('1', '2', '3'):
        print('Invalid entry. Enter 1, 2 or 3:')
        x = input()
    return x


# STEP 1
# Read the data file (data/data.csv).
# Return the data stored in a list of dicts.
def read_data(DATA_PATH):
    try:
        lod = file_to_list_of_dicts(DATA_PATH)
    except FileNotFoundError as e:
        print('ERROR:',e)
    
    #print(lod)
    return lod
    

# STEPS:
# 1. Read the data file and store the data in a list of dicts (lod).
# 2. In a while loop, call select_search_field(). 
#    select_search_field() returns the user selection x (1, 2 or 3)
# 3. Call enter_query(x).
#    enter_query(x) returns the query text.
# 4. Call search_database(lod, x, q).
# 5. Print the matched records.
# 6. Call another_search().
# 7. If another_search() returns 'n', end the search.
#    Otherwise, the loop in step 2 runs again.

def search(DATA_PATH):    
    
    # STEP 1
    lod = read_data(DATA_PATH)

    # While loop keeps iterating until 
    # the user selects 'n' in STEP 7.
    while True:
        # STEP 2
        x = select_search_field()
        
        # STEP 3
        query = enter_query(x)        
   
        # STEP 4
        result = search_database(lod, x, query)        
        
        # STEP 5
        print_result(result)
           
        # STEP 6
        x = another_search()
        
        # STEP 7
        if x == 'n':
            return None
