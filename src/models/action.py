# ----------------------------------------------------------------------
# actions.py
#
# Model for 1 action
# ----------------------------------------------------------------------

class Action:
    """Represents a single action"""

    def __init__(self, name: str, value: float, return_percent: float):
        self.name = name
        self.value = value
        self.return_percentage = return_percent

    @property
    def profit(self) -> float:
        return self.value * self.return_percentage