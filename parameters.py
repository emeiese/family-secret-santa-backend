from pandas import DataFrame
from numpy import random
family_dict = {
    'Picasso-Retamal': ['José Picasso', 'Juana Retamal', 'María Picasso Retamal'],
    'Retamal-Martinez': ['Pedro Retamal', 'Josefa Martinez', 'Juan Retamal Martinez', 'Alejandra Retamal Martinez'],
    'Durán-Retamal': ['Rodrigo Durán', 'Francisca Retamal', 'Olga Durán Retamal', 'Mercedes Durán Retamal'],
    'Retamal-Ortiz': ['José Retamal', 'Juana Ortiz', ]
}


# Build the people list:
people_list = []
for k, v in family_dict.items():
    people_list += v
people_list = sorted(set(people_list))

# Set some random costs between people: 
#  you can comment this line and uncomment the other one to have equal costs for everybody
people_cost = DataFrame(random.randint(-2, high=1, size=(len(people_list), len(people_list))), index=people_list, columns=people_list)
# people_cost = DataFrame(-1, index=people_list, columns=people_list)

# You can also set costs between people:
# For example:
people_cost.loc[('José Picasso', 'Juana Ortiz')] = 10
people_cost.loc[('Pedro Retamal', 'Mercedes Durán Retamal')] = 10

# Possible pairs for the family secret santa, where the first coordinate is santa (who gifts) and the second is the child (who recieves)
possible_pairs = []
for i in people_list:
    for j in people_list:
        possible_pairs.append((i, j))
