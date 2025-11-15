# ----------------------------------------------------------------------
# invest_trade.py
#
# Util fonctions related with file management
# ----------------------------------------------------------------------

# Local Librairies : project-specific modules
from models.actions_list import ActionsList
from views.show_results import HTMLGenerator


class Main:
    """Initialize app """

    def __init__(self):
        self.actions_list = ActionsList()
        self.actions_list.load_actions()
        self.show_actions()
    #    self.suggest_invest()

    def show_actions(self):
        """Generate the HTML page with the actions list"""
        pageHTML = HTMLGenerator(self.actions_list.actions)
        pageHTML.generate()


if __name__ == "__main__":
    # Start the program
    Main()
