family_dict = {
    'Family 1 (F1)': ['Father (F1)', 'Father (F1)', 'Son 1 (F1)'],
    'Family 2 (F2)': ['Mother (F2)', 'Father (F2)', 'Daughter 1 (F2)', 'Daughter 2 (F2)'],
    'Family 3 (F3)': ['Mother (F3)', 'Father (F3)', 'Son 1 (F3)', 'Daughter 1 (F3)'],
    'Family 4 (F4)': ['Grand parent (F4)', 'Grand Mother (F4)', ]
}


# Build the people list:
people_list = []
for k, v in family_dict.items():
    people_list += v
people_list = sorted(set(people_list))


# Possible pairs for the family secret santa, where the first coordinate is santa (who gifts) and the second is the child (who recieves)
possible_pairs = []
for i in people_list:
    for j in people_list:
        possible_pairs.append((i, j))
