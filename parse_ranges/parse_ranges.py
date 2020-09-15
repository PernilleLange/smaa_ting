def parse_ranges(intake):
    num_list2 = []
    for pair in intake.split(','):
        if '-' in pair:
            x,y = pair.split('-')
            num_list2.append([int(x), int(y)+1])
        else:
           num_list2.append([int(pair), int(pair)+1])

    for pair in num_list2:
        a,b = pair
        numbers = range(a,b)
        for num in numbers:
            yield num




