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

load
class ActionsList:
    """Represents a list of actions"""

    def __init__(self, file_path: str = ACTIONS_LIST_FILE_PATH):
        self.actions: list[Action] = []
        self.file_path = file_path
        # self.load_actions()  # plus automatique

    def add(self, action: Action):
        self.actions.append(action)

    def load_actions(self):
        """Load actions from CSV file"""
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
                        self.add(action)
                    except IndexError:
                        print(f"Row incomplete, skipping: {row}")
                    except ValueError:
                        print(f"Skipping invalid row {row}: {row}")
        except FileNotFoundError:
            print(f"CSV file not found: {self.file_path}")

