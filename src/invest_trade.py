# ----------------------------------------------------------------------
# invest_trade.py
#
# Util fonctions related with file management
# ----------------------------------------------------------------------


class Main:
    """Initialize app directories, controllers et main menu"""

    # Read Liste_Actions file
    liste_actions = ListeActions()

    # Print lise actions
    liste_actions.show_actions()


if __name__ == "__main__":
    # Start the program
    Main()