import unicodedata

def is_anagram(intake_1, intake_2):
    norm_string1 = ''.join([c for c in unicodedata.normalize('NFKD', intake_1).lower() if not unicodedata.combining(c)])
    dict_to_check_1 = {}
    norm_string2 = ''.join([c for c in unicodedata.normalize('NFKD', intake_2).lower() if not unicodedata.combining(c)])
    dict_to_check_2 = {}
    for char in norm_string1:
        if char not in dict_to_check_1 and char.isalpha():
            dict_to_check_1[char] = 1
        elif char in dict_to_check_1:
            dict_to_check_1[char] += 1
    for char in norm_string2:
        if char not in dict_to_check_2 and char.isalpha():
            dict_to_check_2[char] = 1
        elif char in dict_to_check_2:
            dict_to_check_2[char] += 1

    return dict_to_check_1 == dict_to_check_2
