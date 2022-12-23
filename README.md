# Family Secret Santa Assignation Problem 🎁️🎄️

This repository is for calculating the assignation problem for a FAMILY secret santa 🎅️

In this case, the complexity relies on the possible restrictions you may have. Some of them might be:
- you can't assign secret santas between direct family members (you want to encourage gifts between different families)
- you want to impose age restrictions (adults give to adulsts and children makes gifts for other children)

You might have another restrictions, so I encourage you to copy this repo and add them by yourself! 😉️

## How to use it:

Use the notebook `family-secret-santa.ipynb` to interact with the code. Some details:

- You can modify families and their members on `parameters.py`
- You can assign social costs between different family members inside `family-secret-santa.ipynb` (I don't know about yours, but in my family some members doesn't tolerate each other and probably would gift a piece of coal between them, oops). The higher the value, the higher the cost inside the objective function.

Hope this might be as useful for you as it was for me. Have a happy christmas and good luck with your secret santa!