# ----------------------------------------------------------------------
# liste_actions.py
#
# Model for the list of actions
# ----------------------------------------------------------------------

# Standard library
import csv

# Local Librairies : project-specific modules
from config import ACTIONS_LIST_FILE_PATH
from action import Action


class ActionsList:
    """Represents the actions list"""
    def __init__(self):
        self.actions: list[Action] = []
        self.file_path = ACTIONS_LIST_FILE_PATH
        self.load_actions()

    def add(self, action: Action):
        self._actions.append(action)

    def load_actions(self):
        """Load CSV and add via add() for central logic"""
        try:
            with open(self.file_path, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    action = Action(row['name'], float(row['value']),
                                    float(row['return_percent']))
                    self.add(action)
        except FileNotFoundError:
            print(f"CSV file not found: {self.file_path}")