import numpy as np
import pandas as pd

from pulp import LpProblem, lpSum, LpVariable, LpMinimize, LpStatus, value


def solve_fss(family_dict: dict, people_cost: pd.DataFrame):
    """
    Solves the family secret santa problem (basically, a secret santa with restrictions)

    Args:
        family_dict (dict): dictionary with the family names as keys and a list of their members as
                            values: dict[name] = [member 1, member 2]
        people_cost (pd.DataFrame): a datafrane with with the social costs of gift-giving
                                    between family members.
    """
    people_list = list(people_cost.index)
    # Possible pairs for the family secret santa, where the first coordinate is santa (who gifts)
    # and the second is the child (who recieves)
    possible_pairs = []
    for i in people_list:
        for j in people_list:
            possible_pairs.append((i, j))

    # Set Problem:
    prob = LpProblem("wsp-problem", LpMinimize)

    # Set Variables:
    pairs = LpVariable.dicts("pairs", ((santa, child) for (santa, child) in possible_pairs),
                             cat='Binary')

    # Minimize social costs
    prob += lpSum([people_cost.loc[(i, j)] * pairs[i, j]
                  for (i, j) in possible_pairs])

    # s.t:

    # Just one santa by person:
    for santa in people_list:
        prob += lpSum([pairs[santa, child] for child in people_list]) == 1

    # It can't be an assignment between members of the same family, and you can't be your own santa.
    for family_name, family_members in family_dict.items():
        for santa in family_members:
            for member in family_members:
                prob += pairs[santa, member] == 0

    # Only one santa can make you a gift (I'm sorry :c )
    for child in people_list:
        prob += lpSum([pairs[santa, child] for santa in people_list]) == 1

    prob.solve()
    status = LpStatus[prob.status]
    val = value(prob.objective)
    print("Status:", status)
    print("Value:", val)

    return {"problem": prob, "solution": pairs}
