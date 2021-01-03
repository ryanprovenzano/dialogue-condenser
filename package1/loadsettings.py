import re
import configparser

from .cleaning_settings import clean_bad_config_data

config = configparser.ConfigParser()
config.read('settings.conf')
list_of_sections = config.sections() #Getting the list of sections from the config file.
interval_list_strings = clean_bad_config_data(list_of_sections) #List of the different gap intervals

#Prefix to put at beginning of output filename (file_prefix)
for test in ['default', 'DEFAULT', 'Default']:
    if config['DEFAULT']['FilePrefix'] == test :
        file_prefix = 'TRIM_'
        prefix_default = True
        break
    else:
        prefix_default = False
if prefix_default != True:
     file_prefix = config['DEFAULT']['FilePrefix']

#Converts a list of numeric strings into a reverse sorted list of integers.
def convert_strings_to_ints( strings ):

    temp = []
    for item in strings:
        temp.append(int(re.sub('[^0-9]','', item)))
    return sorted(temp, reverse = True)

#For converting a single int value to it's corresponding section string.
def revert_to_string( input ):

    for i in range(len(list_of_sections)):

        section_string = list_of_sections[i]

        numeric_chars = [] #Emptying this list everytime before the for loop

        for char in section_string:
            if char.isnumeric():
                numeric_chars.append(char)

        numeric_string = ''.join(numeric_chars)
        numeric_int = int(numeric_string)

        if input == numeric_int:
            return section_string

interval_list_ints = convert_strings_to_ints(interval_list_strings)

interval_list_min = min(interval_list_ints)
