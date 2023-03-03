"""Main file to invoke the Discord Bot
"""

# Standard libraries.
import sys
import os
import asyncio
import json
import pyautogui
import time
from datetime import datetime, timezone

# Third-party libraries.
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio

# from services import chat_gpt
import requests

# Local libraries
from src.config import COMMAND_PERFIX, ANANT_BOT_KEY, LOG_PATH, SERVER_ID
from src import api_header
from services import chat_gpt


CWD = os.path.dirname(os.path.realpath(__file__))

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
        with open(os.path.join(CWD, r"data\gifs\night.gif"), "rb") as file:
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
        with open(os.path.join(CWD, r"data\gifs\deer.gif"), "rb") as file:
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


@client.command(pass_context=True, brief="Send invite message to a user.")
async def invite(context, user: discord.Member):
    """To invite the BOT to the voice server

    Args:
        context (_type_): Allows to comminicate with your discord server.
            - Also provdes with the information related to user executing the command.
    """
    try:
        channel = context.message.author.voice.channel
        if channel:
            await channel.connect()
            _user = await client.fetch_user(user.id)
            server = client.get_guild(SERVER_ID)
            invite_message = f"Hi {user.name}, come join our server! Here's a invite link: {await server.text_channels[0].create_invite()}"
            await _user.send(invite_message)
            with open(os.path.join(CWD, r"data\gifs\view_yellow.gif"), "rb") as file:
                picture = discord.File(file)
                await _user.send(file=picture)
            time.sleep(4)

        else:
            msg = f"Channel: {channel} does not exist."
            await context.send(msg)
    except discord.errors.ClientException as ex:
        msg = f"Error: {ex}"
        await context.send(msg)
    finally:
        _logger("invite", msg, context.author.mention)


@client.command(pass_context=True, brief="Add Bot to the Voice channel.")
async def join_voice(context):
    """To invite the BOT to the voice server

    Args:
        context (_type_): Allows to comminicate with your discord server.
            - Also provdes with the information related to user executing the command.
    """
    msg = "Joining the Voice channel."
    try:
        if context.author.voice:
            channel = context.message.author.voice.channel
            await channel.connect()
            await context.send(msg)
            with open(os.path.join(CWD, r"data\gifs\welcome-banner.gif"), "rb") as file:
                picture = discord.File(file)
                await context.send(file=picture)
            time.sleep(4)

        else:
            msg = "You are not in voice channel. Join the voice channel and then run the command."
            await context.send(msg)
    except discord.errors.ClientException as ex:
        msg = f"Error: {ex}"
        await context.send(msg)
    finally:
        _logger("join_voice", msg, context.author.mention)


@client.command(pass_context=True, brief="Remove the Bot from the Voice channel.")
async def leave_voice(context):
    """To remove the BOT from voice channel."""
    msg = "Leaving the Voice channel."
    try:
        if context.voice_client:
            await context.guild.voice_client.disconnect()
            await context.send(msg)
        else:
            msg = "I am not in any voice channel."
            await context.send(msg)
    except discord.errors.ClientException as ex:
        msg = f"Command error: {ex}"
        await context.send(msg)
    finally:
        _logger("leave_voice", msg, context.author.mention)


@client.command(brief="Invite user to Voice channel.")
async def send_invite(ctx, channel_name: str, user: discord.Member):
    """To send voice invite link to a channel"""
    voice_channel = discord.utils.get(ctx.guild.voice_channels, name=channel_name)
    if not voice_channel:
        await ctx.send(f"Voice channel {channel_name} not found.")
        return
    _invite = await voice_channel.create_invite()
    await user.send(
        f"""You have been invited to join {voice_channel.name}! 
        Use this invite link to join: {_invite.url}"""
    )
    await ctx.send(f"Invite link sent to {user.name}.")


def main() -> int:
    """To run the BOT"""
    client.run(ANANT_BOT_KEY)


if __name__ == "__main__":
    sys.exit(main())
