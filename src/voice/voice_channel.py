"""Main script to handle the Voice channel commands"""

import os
import time

import discord
from discord import FFmpegPCMAudio

from src.discord_main import client
from src.discord_main import _logger
from src.config import SERVER_ID, PROJECT_DIR


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
            with open(
                os.path.join(PROJECT_DIR, r"data\gifs\view_yellow.gif"), "rb"
            ) as file:
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


@client.command(brief="Invite user to specific Voice channel.")
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
            voice = await channel.connect()
            await context.send(msg)
            with open(
                os.path.join(PROJECT_DIR, r"data\gifs\welcome-banner.gif"), "rb"
            ) as file:
                picture = discord.File(file)
                await context.send(file=picture)
            time.sleep(4)
            source = FFmpegPCMAudio(r"data\audio\Aathma-Raama(PagalWorld).mp3")
            player = voice.play(source)

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
