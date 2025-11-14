#----------------------------------------------------------------------
# wikibooks.py
#
# App that extract books information from the web site: https://books.toscrape.com/index.html
# ---------------------------------------------------------------------

# Standard library imports - built-in modules that come with Python
import csv
import os
import re
import sys
from urllib.parse import urljoin, urlparse

# External libraries installed via pip
import requests
from bs4 import BeautifulSoup

# Local Librairies : project-specific modules
from data_cleaner import clean_number, clean_repository_name
from log_config import logger
from requests_tools import make_requests
