string = input()
index = 1
streng = ''
for char in string:
    if char == ' ':
        streng += char            
    elif index % 2 == 0:
        streng += char.upper()
        index += 1
    else:
        streng += char.lower()
        index += 1
print(streng)