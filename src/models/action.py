# ----------------------------------------------------------------------
# actions.py
#
# Model for 1 action
# ----------------------------------------------------------------------

class Action:
    def __init__(self, name, value, return_percentage):
        self.name = name
        self.value = value
        self.return_percentage = return_percentage