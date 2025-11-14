# ----------------------------------------------------------------------
# liste_actions.py
#
# Model for the list of actions
# ----------------------------------------------------------------------

# Local Librairies : project-specific modules
from action import Action


class ListeActions:
    def __init__(self):
        self.actions: list[Action] = []