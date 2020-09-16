import re

def parse_ranges(feed):
    intake = re.sub(r'->exit', r'', feed)
    num_list = []
    for pair in intake.split(','):
        if '-' in pair:
            x,y = pair.split('-')
            num_list.append([int(x), int(y)+1])
        else:
           num_list.append([int(pair), int(pair)+1])

    for pair in num_list:
        a,b = pair
        numbers = range(a,b)
        for num in numbers:
            yield num

