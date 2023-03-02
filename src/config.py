import os


command_prefix = "$"
BOT_NAME = "ANANT-Bot"
ANANT_BOT_KEY = os.environ["ANANT-BOT-KEY"]

PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))

command_logging_file_path = (
    f"{os.path.join(PROJECT_DIR, 'logs', 'command_history.txt')}"
)
