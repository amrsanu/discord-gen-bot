"""Script to save the config variables
For easy modification of the script behaivour and settings"""

import os

COMMAND_PERFIX = "$"
BOT_NAME = "ANANT-Bot"
ANANT_BOT_KEY = os.environ["ANANT-BOT-KEY"]

PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))

LOG_PATH = (
    f"{os.path.join(PROJECT_DIR, 'logs', 'command_history.txt')}"
)

INVITE_LINK = r"https://discord.gg/EJyCvjcm"
SERVER_ID = 1076579343301607434
