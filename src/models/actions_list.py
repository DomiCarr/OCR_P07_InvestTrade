# ----------------------------------------------------------------------
# liste_actions.py
#
# Model for the list of actions
# ----------------------------------------------------------------------

# Standard library
from itertools import combinations
import csv
import time
# Local Librairies : project-specific modules
from config import ACTIONS_LIST_FILE_PATH
from config import MAX_INVEST
from config import ALGO_MODE
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
        """Select algorithm: knapsack or brute-force"""

        mode = ALGO_MODE

        if mode == "force_brute":
            return self.calc_invest_force_brute()

        return self.calc_invest_knapsack()

    # -----------------------------------------------------------------------------
    def calc_invest_knapsack(self):
        """Compute optimal portfolio using dynamic programming knapsack approach"""
    # -----------------------------------------------------------------------------

        # CONSOLE LOG :
        print("\n==================================>>>>>>> KNAPSACK ALGO ===")

        #  # CONSOLE LOG : ---- timers & counters ----
        start_time = time.time()
        iterations = 0

        # Extract values and profits
        values = [int(a.value) for a in self.actions]  # DP uses int weights
        profits = [a.profit for a in self.actions]

        n = len(values)
        capacity = int(MAX_INVEST)

        # CONSOLE LOG :
        print(f"Number of actions: {n}")
        print(f"MAX_INVEST: {capacity}\n")

        # Create an empty DP table filled with zeros.
        # Each row represents "using the first i actions"
        # Each column represents "budget from 0 to capacity"
        #
        # Example if n = 2 and capacity = 2:
        # [
        #   [0.0, 0.0, 0.0],   # i = 0 (no actions)
        #   [0.0, 0.0, 0.0],   # i = 1
        #   [0.0, 0.0, 0.0],   # i = 2
        # ]
        #
        # We initialize the DP table everything to 0 before filling the table.
        dp = [[0.0] * (capacity + 1) for i in range(0, n + 1)]

        # --- Fill the DP table ---
        for i in range(1, n + 1):
            # Select the current action from the list.
            # We use i-1 because the loop index i starts at 1 to keep dp[0][...]
            # as the base case representing "no actions chosen".
            # This aligns with the standard knapsack dynamic programming approach:
            # dp[i][w] represents the maximum profit achievable using the first i actions
            # with a total budget w. Using i-1 here retrieves the correct action from the list.

            action = self.actions[i - 1]
            action_value = values[i - 1]
            action_profit = profits[i - 1]

            # Iterate over all possible total values from 0 to MAX_INVEST.
            # 'w' represents the current total value we are considering for this step.
            for w in range(capacity + 1):
                # CONSOLE LOG : count every loop step for performance tracking
                iterations += 1

                if action_value > w:
                    # Current action is too expensive to include in this capacity (w)
                    # We cannot take it, so the profit stays the same as without this action
                    dp[i][w] = dp[i - 1][w]
                else:
                    # Option 1: Include the current action
                    # Profit = profit of this action + best profit with remaining capacity
                    profit_including_action = action_profit + dp[i - 1][w - action_value]

                    # Option 2: Exclude the current action
                    # Profit = best profit without taking this action
                    profit_excluding_action = dp[i - 1][w]

                    # Take the better option (maximum profit)
                    dp[i][w] = max(profit_excluding_action, profit_including_action)



        # CONSOLE LOG : --- Backtracking ---
        print("\n=== BACKTRACKING ===")
        w = capacity
        selected_indexes = []

        for i in range(n, 0, -1):
            if dp[i][w] != dp[i - 1][w]:
                action = self.actions[i - 1]
                selected_indexes.append(i - 1)
                print(f"Selected: {action.name} "
                    f"(value={action.value}, profit={action.profit})")
                w -= values[i - 1]

        selected_indexes.reverse()

        # Build the new portfolio
        new_portfolio = ActionsList()
        new_portfolio.actions = [self.actions[i] for i in selected_indexes]

        self.new_portfolio = new_portfolio
        self.total_invest = sum(a.value for a in new_portfolio.actions)

        # CONSOLE LOG :
        print("\n=== FINAL PORTFOLIO ===")

        for a in new_portfolio.actions:
            print(f"- {a.name} | value={a.value} | profit={a.profit}")

        # CONSOLE LOG :
        print(f"TOTAL INVESTED: {self.total_invest}")

        # ---- end timer ----
        elapsed = time.time() - start_time

        # CONSOLE LOG :
        print(f"\nIterations: {iterations}")
        print(f"Elapsed time: {elapsed:.4f} seconds")
        print("=== END CALC_INVEST ===\n")

    # -----------------------------------------------------------------------------
    def calc_invest_force_brute(self):
        """Return a new action list for best invest and max amount """
    # -----------------------------------------------------------------------------

        # CONSOLE LOG :
        print("\n==================================>>>>>>> FORCE BRUTE ALGO ===")

        #  # CONSOLE LOG : ---- timers & counters ----
        start_time = time.time()
        iterations = 0

        best_profit = 0.0
        best_portfolio = None

        temp_actions = self.actions[:]
        nb_actions = len(temp_actions)

        new_portfolio = ActionsList()  # create instance

        # Test all subsets
        for r in range(1, nb_actions+1):
            for subset in combinations(temp_actions, r):
                iterations += 1  # count every subset
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
                    # CONSOLE LOG : ---- timers & counters ----
                    print(f"Subset values {subset_values} | "
                        f"Total : {total_value} | "
                        f"Profit : {profit} ")

        new_portfolio.actions = list(best_portfolio)
        self.new_portfolio = new_portfolio
        self.total_invest = sum(a.value for a in best_portfolio)

        # ---- timers & iteration count ----
        elapsed = time.time() - start_time
        #  CONSOLE LOG : ---- timers & counters ----
        print(f"\nIterations: {iterations}")
        print(f"Elapsed time: {elapsed:.4f} seconds")