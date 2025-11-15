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


class HTMLGenerator:
    """Create the output HTML file"""

    def __init__(self,
                 actions: list[Action],
                 file_path: str = HTML_FILE_PATH):
        self.actions = actions
        self.file_path = file_path

    def generate(self):
        """Generate the HTML page"""
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        title = "Invest & Trade"

        innerHTML = ""
        text = ""

        """ Generate page top"""
        text = f"""
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

        <table>
            <tr>
                <th>Name</th>
                <th>Value</th>
                <th>Percentage</th>
                <th>Profit</th>
            </tr>
        """
        innerHTML = innerHTML + text

        """Generate the actions tab"""
        text = ""
        for action in self.actions:
            text = text + f"""
            <tr>
                <td>{action.name}</td>
                <td>{action.value}</td>
                <td>{action.return_percentage}</td>
                <td>{action.profit}</td>

            </tr>
        """
        innerHTML = innerHTML + text

        innerHTML = innerHTML + f"""
        </table>
    </main>

</body>

</html>
"""


        with open(self.file_path, "w", encoding="utf-8") as f:
            f.write(innerHTML)