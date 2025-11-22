# ----------------------------------------------------------------------
# config.py
#
# Configuration for InestTrade app
# ----------------------------------------------------------------------

# Standard library imports - built-in modules that come with Python
import os

# Input: Actions file path
ACTIONS_LIST_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'Liste_Actions.csv')
# ACTIONS_LIST_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'dataset1.csv')
# ACTIONS_LIST_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'dataset2.csv')

# Output: index.html file path
HTML_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'html', 'index.html')

# max invest
MAX_INVEST = 500

# ALGO_MODE: choose the algorithm for computing optimal portfolio
# "knapsack" = knapsack dynamic approach
# "force_brute" = brute-force all subsets
ALGO_MODE = "knapsack"
# ALGO_MODE = "force_brute"

