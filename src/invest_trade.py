# ----------------------------------------------------------------------
# invest_trade.py
#
# Util fonctions related with file management
# ----------------------------------------------------------------------

# Local Librairies : project-specific modules
from models.action import Action
from models.actions_list import ActionList

class Main:
    """Initialize app directories, controllers et main menu"""

    # Read Liste_Actions file
    actions = ActionsList()

    # Print lise actions
    #liste_actions.show_actions()


if __name__ == "__main__":
    # Start the program
    Main()