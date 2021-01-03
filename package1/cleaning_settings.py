import re

#\d chars are any numerical digits 0-9
RE_D = re.compile('\d')
def contains_numbers_and_ms(string):

    def contains_numbers(string):
        return RE_D.search(string)

    if contains_numbers(string) != None and 'ms' in string:
        return True

def clean_bad_config_data(sections):

    temp = []
    for section in sections:
        if section.isnumeric() or contains_numbers_and_ms(section):
            temp.append(section)
    return temp
