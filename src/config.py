"""Script to save the config variables
For easy modification of the script behaivour and settings"""

import os

PROJECT_DIR = r"C:\dev\dev.py\discord-gen-bot"

COMMAND_PERFIX = "$"
BOT_NAME = "ANANT-Bot"
ANANT_BOT_KEY = os.environ["ANANT-BOT-KEY"]

PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))

LOG_PATH = f"{os.path.join(PROJECT_DIR, 'logs', 'command_history.txt')}"

INVITE_LINK = r"https://discord.gg/EJyCvjcm"
SERVER_ID = 1076579343301607434


AUDIO = [
    r"data\audio\Aathma-Raama(PagalWorld).mp3",
    r"data\audio\hello, the bot is joining.mp3",
    r"data\audio\ting.mp3",
]

