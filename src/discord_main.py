"""Main file to invoke the Discord Bot
"""

# Standard libraries.
import sys
import os
import asyncio
import json
import time
from datetime import datetime, timezone

# Third-party libraries.
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio

# from services import chat_gpt
import requests

# Local libraries
from src.config import COMMAND_PERFIX, ANANT_BOT_KEY, LOG_PATH, PROJECT_DIR
from src import api_header
from services import chat_gpt


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = commands.Bot(command_prefix=COMMAND_PERFIX, intents=intents)


def _logger(command, message=None, author=None):
    called_at = datetime.now(timezone.utc)
    with open(LOG_PATH, "a", encoding="utf-8") as logger:
        log = f"{called_at}: !{command}: {message}, By:{author}"
        logger.write(f"{log}\n")
        print(log)


# Event triggers actions based on the actions happening in discord channel.
@client.event
async def on_ready():
    """Event triggers when the discord server gets clean start."""
    print("===========================================")
    print("Getting the Bot ready for use!")


@client.event
async def on_member_join(member):
    """Event triggers when a new member joins."""
    username = member.name
    userid = member.id
    channel = member.guild.system_channel
    if channel is not None:
        _logger(
            "Join Server",
            f"In channel: {channel}",
            f"{username}",
        )
        response = requests.request(
            "GET",
            api_header.quote_api["url"],
            headers=api_header.quote_api["headers"],
            timeout=5,
        )
        quote = json.loads(response.text)
        await channel.send(
            f"Welcome to the server, <@{userid}> !\n  # {quote['content']}"
        )
        with open(os.path.join(PROJECT_DIR, r"data\gifs\night.gif"), "rb") as file:
            picture = discord.File(file)
            await channel.send(file=picture)
            await asyncio.sleep(5)


@client.event
async def on_member_remove(member):
    """Event triggers when any member leave the server
    Informs the users with a message.
    """
    username = member.name
    userid = member.id
    channel = member.guild.system_channel
    if channel is not None:
        _logger(
            "Leave Server",
            f"In channel: {channel}",
            f"{username}",
        )
        await channel.send(f"Goodbye <@{userid}> !")
        with open(os.path.join(PROJECT_DIR, r"data\gifs\deer.gif"), "rb") as file:
            picture = discord.File(file)
            await channel.send(file=picture)
        await asyncio.sleep(5)


# ================================================================================
# ----------------- ADDING ALL THE COMMANDS --------------------------------------
# ================================================================================

client.remove_command("help")


@client.command(brief="Greet...")
async def hello(ctx, *args):
    """Greet messgae."""
    _logger("!hello", " ".join(args), ctx.author.mention)
    await ctx.send(f"Hello {ctx.author.mention} I am a BOT.")


@client.command(brief="Leaving notification.")
async def bye(ctx, *args):
    """Bye message..."""
    _logger("!bye", " ".join(args), ctx.author.mention)
    await ctx.send(f"Goodbye {ctx.author.mention}, Have a good day!")


@client.command(brief="To send HBar.")
async def send_hbar(ctx, *args):
    """Dummy for sending the HBar - Will need to setup a complete server for the Chain"""
    _logger("!send_hbar", " ".join(args), ctx.author.mention)
    await ctx.send(f"SUCCESS! {ctx.author.mention} >> {args[0]} : {args[1]}HBAR")


@client.command(brief="Use it to invoke ChatGPT.")
async def gpt(ctx, *args):
    """To invoke chat_gpt and get responce to the queries"""
    _logger("!gpt", " ".join(args), ctx.author.mention)
    result = chat_gpt.gpt(" ".join(args))

    await ctx.send(f">> {result}")


def main() -> int:
    """To run the BOT"""
    client.run(ANANT_BOT_KEY)


if __name__ == "__main__":
    sys.exit(main())
