import configparser
import re


config = configparser.ConfigParser()
config.read('settings_new.conf')

#Converts a list of numeric strings into a reverse sorted list of integers.
def convert_strings_to_ints(strings):
    temp = []
    for item in strings:
        temp.append(int(re.sub('[^0-9]','', item)))
    return sorted(temp, reverse = True)

interval_list = convert_strings_to_ints(config.sections())

print(interval_list)
print(min(interval_list))

#Sorting the list by ascending will retrieve all the sections with the intervals growing in ascending order,
#regardless of whether "ms" is attacheed to the send of it
