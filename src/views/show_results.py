# ----------------------------------------------------------------------
# show_results.py
#
# Generate the HTML file
# ----------------------------------------------------------------------

# Standard library
import os

# Local Librairies : project-specific modules
from config import HTML_FILE_PATH
from models.action import Action
from models.actions_list import ActionsList


class HTMLGenerator:
    """Create the output HTML file"""

    def __init__(self,
                 actions: list[Action],
                 new_portfolio: list[Action],
                 total_invest,
                 file_path: str = HTML_FILE_PATH):
        self.actions = actions
        self.new_portfolio = new_portfolio
        self.total_invest = total_invest
        self.file_path = file_path

    def generate(self):
        """Generate the HTML page"""
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        title = "Invest & Trade"

        innerHTML = ""

        innerHTML = f"""
        <!DOCTYPE html>
        <html lang="en">

        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="./style/style.css">
            <title>{title}</title>
        </head>


        <body>
            <header>
                <h1>Invest & Trade</h1>
            </header>

        <main>
                <div class="tab_actions">
            <div class="title">Portefeuille d'actions</div>
        <table>
            <tr>
                <th>Name</th>
                <th>Value</th>
                <th>Percentage</th>
                <th>Profit</th>
            </tr>
        """

        """Generate the actions table"""
        sorted_list = sorted(self.actions, key=lambda a: a.return_percentage, reverse=True)
        for action in sorted_list:
            innerHTML = innerHTML + f"""
            <tr>
                <td>{action.name}</td>
                <td>{action.value}</td>
                <td>{action.return_percentage}</td>
                <td>{action.profit}</td>

            </tr>
        """

        innerHTML = innerHTML + f"""
                </table>
        </div>

                <div class="tab_actions">
            <div class="title">Propositions d'investissement</div>
            <table>
                <tr>
                    <th>Name</th>
                    <th>Value</th>
                    <th>Percentage</th>
                    <th>Profit</th>
                </tr>

"""

        """Generate the portfolio table"""
        for action in self.new_portfolio:
            innerHTML = innerHTML + f"""
            <tr>
                <td>{action.name}</td>
                <td>{action.value}</td>
                <td>{action.return_percentage}</td>
                <td>{action.profit}</td>

            </tr>
        """
        innerHTML = innerHTML + f"""
        </table>
            <div class="total">
                Total investi : {self.total_invest}
            </div>
        </div>
        </main>

        </body>

        </html>
        """

        with open(self.file_path, "w", encoding="utf-8") as f:
            f.write(innerHTML)