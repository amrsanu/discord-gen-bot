"""Main script to handle the general messages without commands."""

import os
import time
import json

import discord
from discord import FFmpegPCMAudio

from src.discord_main import client
from src.discord_main import _logger
from src.config import PROJECT_DIR, COMMAND_PERFIX
from data.bad_words import BAD_WORDS, BAD_WORDS_WITH_SPACE


def is_bad_swear_in_message(message: str, user: str):
    """To check if the message contains any bad/swear/abusive words

    Args:
        message (str): Message from the chat.
    Returns:
        bool: Retuen True if message contains any bad words. Otherwise, False
    """
    abusive_users = {}
    message = message.lower()
    is_bad_phrase = any(bad_word in message for bad_word in BAD_WORDS_WITH_SPACE)
    message = message.split()
    is_bad_word = any(bad_word in message for bad_word in BAD_WORDS)

    if is_bad_word or is_bad_phrase:
        with open(
            os.path.join(PROJECT_DIR, r"data\abusive_user.json"), "r", encoding="utf-8"
        ) as file:
            abusive_users = json.load(file)

        if user in abusive_users.keys():
            abusive_users[user] += 1
        else:
            abusive_users[user] = 1

        json_object = json.dumps(abusive_users, indent=4)
        with open(
            os.path.join(PROJECT_DIR, r"data\abusive_user.json"), "w", encoding="utf-8"
        ) as outfile:
            outfile.write(json_object)
    return is_bad_word or is_bad_phrase


@client.event
async def on_message(message):
    """To invoke this function on every normal message
    <Message id=1081825618301300766
        channel=<TextChannel id=1076579343884628020 name='general' position=0 nsfw=False news=False category_id=1076579343884628018>
        type=<MessageType.default: 0>
        author=<Member id=1070764117029290005 name='knight_sun' discriminator='2725' bot=False nick=None guild=<Guild id=1076579343301607434 name='knight_Funtoosh' shard_id=0 chunked=True member_count=4>>
        flags=<MessageFlags value=0>
    >"""
    try:
        msg = f"{message.content}"
        if message.content.startswith(COMMAND_PERFIX):
            await client.process_commands(message)
        if message.author.bot:
            return
        user = message.author.mention
        if is_bad_swear_in_message(message.content, user):
            await message.delete()
            await message.channel.send(
                "WARNING: Never try abusive words, Actions will be taken."
            )
            msg = f"WARNING:  abusive words."
    except Exception as ex:
        msg = f"Command error: {ex}"
        await message.channel.send(msg)
    finally:
        _logger("on_message", msg, message.author.mention)


@client.command(pass_context=True, brief="To send a message dorectly to user from bot")
async def message(context, user: discord.Member, *, msg=None):
    """To send a message dorectly to user from bot"""
    if msg == None:
        msg = "Hello there! This is a direct message from bot."
    embed = discord.Embed(title=msg)
    await user.send(embed=embed)
