# ----------------------------------------------------------------------
# config.py
#
# Configuration for InestTrade app
# ----------------------------------------------------------------------

# Standard library imports - built-in modules that come with Python
import os

# Input: Actions file path
ACTIONS_LIST_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'Liste_Actions.csv')

# Output: index.html file path
HTML_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'html', 'index.html')

# max invest
MAX_INVEST = 500
