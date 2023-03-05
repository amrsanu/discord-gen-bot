"""Main file to invoke the Discord Bot
"""

import sys
from src.discord_main import client
from src.config import ANANT_BOT_KEY
from src.voice import voice_channel, voice_channel_utils
from src import message


def main() -> int:
    """To run the BOT"""
    client.run(ANANT_BOT_KEY)


if __name__ == "__main__":
    sys.exit(main())
