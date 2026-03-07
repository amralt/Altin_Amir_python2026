def invert(old_dict: dict) :
    new_dict = dict()
    for i in old_dict.keys():
        new_dict[old_dict[i]] = i
    return dict(sorted(new_dict.items()))

print(invert({'a': 1, 'b': 2, 'c': 3}))