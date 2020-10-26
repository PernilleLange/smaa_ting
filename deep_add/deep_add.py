

def deep_add(intake, start=0):

    total = []
    if start != 0:
        total.append(start)
    for element in intake:
        if hasattr(element, '__iter__'):
            total.append(deep_add(element))
        else:
            total.append(element)
    if len(total) > 0 and type(total[0]) is not int:
        total2 = total[0]
        for num in total[1:]:
            total2 += num
        return total2
    else:
        return sum(total)

