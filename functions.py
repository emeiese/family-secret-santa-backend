import numpy as np
import pandas as pd

from pulp import LpProblem, lpSum, LpVariable, LpMinimize, LpStatus, value
from random import shuffle


def solve_fss(family_dict: dict, people_list: list, people_cost: pd.DataFrame, possible_pairs: list):
    """
    Solves the family secret santa problem (basically, a secret santa with restrictions)

    Args:
        family_dict (dict): _description_
        people_list (list): _description_
        people_cost (pd.DataFrame): _description_
        possible_pairs (list): 
    """
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
