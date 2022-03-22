"""
    File contain all project constants
"""
import os.path
# CITY_DATA = { 'chicago': 'chicago.csv',
#               'new york': 'new_york.csv',
#               'washington': 'washington.csv' }
data_dir_path = os.path.join(os.path.dirname(__file__), '../data')
data_files = os.listdir(data_dir_path)
CITY_DATA = {  file_path.split('.')[0].replace('_', ' '): os.path.join(data_dir_path, file_path) for file_path in data_files}

WEEK_DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

if __name__ == '__main__':
    print("======================== * CONSTANTS * ============================")
    print("1. CITY_DATA: \n-------------\n", CITY_DATA)
    print("===================================================================")
