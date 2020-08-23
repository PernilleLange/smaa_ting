import collections

def uniques_only(intake):
    checked_hashables = set()
    checked_unhashables = []
    for item in intake:
        if isinstance(item, collections.Hashable):
            if item not in checked_hashables:
                checked_hashables.add(item)
                yield item
        else:
            if item not in checked_unhashables:
                checked_unhashables.append(item)
                yield item





