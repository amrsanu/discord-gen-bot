"""Script to save the config variables
For easy modification of the script behaivour and settings"""

import os

# -------------------- DISCORD SERVER SETTINGs ------------
COMMAND_PERFIX = "."
BOT_NAME = "ANANT-Bot"
ANANT_BOT_KEY = os.environ["ANANT-BOT-KEY"]
INVITE_LINK = r"https://discord.gg/EJyCvjcm"
SERVER_ID = 1076579343301607434

RAPID_API_KEY = os.environ["X-RapidAPI-Key"]

# -------------------- FILE PATHs ------------
PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
# PROJECT_DIR = r"C:\dev\dev.py\discord-gen-bot"
LOG_PATH = f"{os.path.join(PROJECT_DIR, 'logs', 'command_history.txt')}"


# -------------------- MESSAGE FILTER ------------
# Block after LIMIT count.
ABUSIVE_WORD_COUNT_LIMIT = 5
# Give strict warning after Warning count.
ABUSIVE_WORD_COUNT_WARNING = 3
