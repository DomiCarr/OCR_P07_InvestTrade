# ----------------------------------------------------------------------
# liste_actions.py
#
# Model for the list of actions
# ----------------------------------------------------------------------

# Standard library
from itertools import combinations
import csv

# Local Librairies : project-specific modules
from config import ACTIONS_LIST_FILE_PATH
from config import MAX_INVEST
from models.action import Action


class ActionsList:
    """Represents a list of actions"""

    def __init__(self):
        self.actions: list[Action] = []
        self.new_portfolio = None

    # self.load_actions()
    def add(self, action: Action):
        self.actions.append(action)

    def load_actions(self):
        """Load actions from CSV file"""
        try:
            with open(ACTIONS_LIST_FILE_PATH, newline='', encoding='utf-8') as f:
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

    def calc_invest(self):
        """Return a new action list for best invest and max amount """

        best_profit = 0.0
        best_portfolio = None

        temp_actions = self.actions[:]
        nb_actions = len(temp_actions)

        new_portfolio = ActionsList()  # create instance

        # Test all subsets
        for r in range(1, nb_actions+1):
            for subset in combinations(temp_actions, r):
                # subsets with total_value > MAX_INVEST are ignored
                total_value = sum(a.value for a in subset)

                # compute the profit of the subset:
                profit = sum(a.value * a.return_percentage for a in subset)

                # save the best combinaison
                if total_value <= MAX_INVEST and profit > best_profit:
                    best_profit = profit
                    best_portfolio = subset

                    # DEBUG : Print subset values:
                    subset_values = ", ".join(str(a.value) for a in subset)
                    print(f"Subset values {subset_values} | "
                        f"Total : {total_value} | "
                        f"Profit : {profit} ")

        new_portfolio.actions = list(best_portfolio)
        self.new_portfolio = new_portfolio
        self.total_invest = sum(a.value for a in best_portfolio)

