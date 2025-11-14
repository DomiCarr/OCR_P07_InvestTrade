# ----------------------------------------------------------------------
# liste_actions.py
#
# Model for the list of actions
# ----------------------------------------------------------------------

# Standard library
import csv

# Local Librairies : project-specific modules
from config import ACTIONS_LIST_FILE_PATH
from models.action import Action


class ActionsList:
    """Represents the actions list"""

    def __init__(self):
        self.actions: list[Action] = []
        self.file_path = ACTIONS_LIST_FILE_PATH
        self.load_actions()

    def add(self, action: Action):
        self._actions.append(action)


    def load_actions(self):
        """Load all actions from CSV file"""
        try:
            with open(self.file_path, newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)  # skip header

                self.actions = []
                for row in reader:
                    try:
                        action = Action(
                            row[0].strip(),
                            float(row[1]),
                            float(row[2].strip('%')) / 100
                        )
                        self.actions.append(action)
                    except IndexError:
                        print(f"Row incomplete, skipping: {row}")
                    except ValueError:
                        print(f"Skipping invalid row {row}: {row}")

        except FileNotFoundError:
            print(f"CSV file not found: {self.file_path}")
