# ----------------------------------------------------------------------
# invest_trade.py
#
# Util fonctions related with file management
# ----------------------------------------------------------------------

# Local Librairies : project-specific modules
from models.actions_list import ActionsList
from views.show_results import HTMLGenerator
from config import MAX_INVEST


class Main:
    """Initialize app """

    def __init__(self):
        self.actions_list = ActionsList()
        self.actions_list.load_actions()
        self.actions_list.calc_invest()
        self.show_actions()

    def show_actions(self):
        """Generate the HTML page with the actions list"""
        pageHTML = HTMLGenerator(
            self.actions_list.actions,
            self.actions_list.new_portfolio.actions,
            self.actions_list.total_invest,
            self.actions_list.total_profit
            )
        pageHTML.generate()


if __name__ == "__main__":
    # Start the program
    Main()
