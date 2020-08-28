# coding=utf-8
# Tag en string ind
# Hvis ord ikke er i dictionary og ikke er - ordet tilføjes som key, værdien sættes til 1
# Hvis ordet er i dictionary - værdien opjusteres med 1, gå videre til næste
# returner dictionary

def remove_punctuation(word):
    index_stop = 0
    index_start = 0
    for char in word[::-1]:
        if not char.isalpha():
            index_stop -= 1
        else:
            break
    for char in word:
        if not char.isalpha():
            index_start += 1
        else:
            break
    if index_start == 0 and index_stop == 0:
        return word
    elif index_start >= 0 and index_stop == 0:
        return word[index_start:]
    else:
        return word[:index_stop]

def count_words(given_string):
    word_array = given_string.split()
    word_dictionary = {}
    for instance in word_array:
        clean_instance = remove_punctuation(instance).lower()

        if clean_instance in word_dictionary:
            word_dictionary[clean_instance] +=1
        else:
            word_dictionary[clean_instance] = 1
    return word_dictionary


