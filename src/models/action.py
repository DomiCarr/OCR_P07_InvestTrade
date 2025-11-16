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
        """Compute profit rounded to 2 decimals"""
        return round(self.value * self.return_percentage, 2)