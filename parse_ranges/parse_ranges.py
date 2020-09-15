def parse_ranges(intake):
    num_list = [(a,b+1) for (a,b) in [[int(x), int(y)] for (x, y) in [pair.split('-') for pair in intake.split(',')]]]

    for pair in num_list:
        a,b = pair
        numbers = range(a,b)
        for num in numbers:
            yield num
test = '1-2,4-4,8-10'
hest = parse_ranges(test)

print(next(hest))
print(next(hest))
print(next(hest))
# print(next(parse_ranges(test)))
# print(next(parse_ranges(test)))
# print(next(parse_ranges(test)))
# print(next(parse_ranges(test)))




