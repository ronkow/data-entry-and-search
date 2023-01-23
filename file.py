#################
# FILE FUNCTIONS
#################

# mode: 
# 'r' read
# 'w' delete all data in the dataset and write new data
# 'a' append new data to dataset

import csv

def file_to_list_of_dicts(filepath):
    with open(filepath, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)    
        return list(reader)
    
  
def list_of_dicts_to_file(filepath, lod):
    keys = lod[0].keys()
    with open(filepath, 'a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, keys)
        #writer.writeheader()
        writer.writerows(lod)

