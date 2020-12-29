import configparser
import re

config = configparser.ConfigParser()
config.read('settings_new.conf')
list_of_sections = config.sections()
#Converts a list of numeric strings into a reverse sorted list of integers.
def convert_strings_to_ints(strings):
    temp = []
    for item in strings:
        temp.append(int(re.sub('[^0-9]','', item)))
    return sorted(temp, reverse = True)

def revert_to_string(input):
    for i in range(len(list_of_sections)):
        section_string = list_of_sections[i]
        section_numerics_list = []
        for i in section_string:
            if i.isnumeric():
                section_numerics_list.append(i)
        numeric_string = ''.join(section_numerics_list)
        numeric_int = int(numeric_string)
        if input == numeric_int:
            return section_string




#List of the different gap intervals
interval_list = convert_strings_to_ints(list_of_sections)


interval_list_min = min(interval_list)


#Prefix to put at beginning of output filename (file_suffix)
for test in ['default', 'DEFAULT', 'Default']:
    if config['DEFAULT']['FileSuffix'] == test :
        file_suffix = 'TRIM_'
        suffix_default = True
        break

if suffix_default != True:
     file_suffix = config['DEFAULT']['FileSuffix']
