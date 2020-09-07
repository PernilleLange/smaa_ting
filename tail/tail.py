def tail(intake, tail):
    output_list = []
    if tail <= 0:
        return output_list
    else:
        for item in list(intake)[-tail:]:
            output_list.append(item)
        return output_list

