"""Script to handle all the commands related to voice channel"""

import os

import discord
from discord import FFmpegPCMAudio

from src.discord_main import client
from src.discord_main import _logger
from data.audio.audio_list import AUDIO

song_queues = {}


def check_queue(context, id):
    """Helper function to play song from the queue."""
    if id in song_queues.keys() and song_queues[id]:
        voice = context.guild.voice_client
        source = song_queues[id].pop()
        player = voice.play(source)


@client.command(pass_context=True, brief="To pause the playing audio.")
async def pause(context):
    """To pause the audio."""
    msg = "Pause the the audio."
    try:
        # To get the voice client
        if context.author.voice:
            voice = discord.utils.get(client.voice_clients, guild=context.guild)
            if voice.is_playing():
                voice.pause()
            else:
                msg = "No audio is playing in Voice channel."
        else:
            msg = "You are not in voice channel. Join the voice channel and then run the command."

    except discord.errors.ClientException as ex:
        msg = f"Command error: {ex}"
    finally:
        await context.send(msg)
        _logger("pause", msg, context.author.mention)


@client.command(pass_context=True, brief="To resume the playing audio.")
async def resume(context):
    """To resume the audio."""
    msg = "resume the the audio."
    try:
        if context.author.voice:
            # To get the voice client
            voice = discord.utils.get(client.voice_clients, guild=context.guild)
            if voice.is_paused():
                voice.resume()
            else:
                msg = "No audio is playing/paused in Voice channel."
        else:
            msg = "You are not in voice channel. Join the voice channel and then run the command."
    except discord.errors.ClientException as ex:
        msg = f"Command error: {ex}"
    finally:
        await context.send(msg)
        _logger("resume", msg, context.author.mention)


@client.command(pass_context=True, brief="To stop the playing/paused audio.")
async def stop(context):
    """To stop the audio."""
    msg = "Stop the current audio."
    try:
        if context.author.voice:
            # To get the voice client
            voice = discord.utils.get(client.voice_clients, guild=context.guild)
            if voice.is_paused() or voice.is_playing():
                voice.stop()
            else:
                msg = "No audio is playing/paused in Voice channel."
        else:
            msg = "You are not in voice channel. Join the voice channel and then run the command."
    except discord.errors.ClientException as ex:
        msg = f"Command error: {ex}"
        await context.send(msg)
    finally:
        await context.send(msg)
        _logger("stop", msg, context.author.mention)


@client.command(pass_context=True, brief="To play audio.")
async def play(context, song_number: int):
    """To pause the audio."""
    msg = f"Play the song num: {song_number}"
    try:
        if context.author.voice:
            if len(AUDIO) > song_number:
                msg = f"Playing song num{song_number}: {AUDIO[song_number].split(os.path.sep)[-1]}"

                voice_state = context.guild.voice_client
                if not voice_state:
                    await context.message.author.voice.channel.connect()
                    voice_state = context.guild.voice_client

                voice = voice_state
                source = FFmpegPCMAudio(AUDIO[song_number])
                player = voice.play(
                    source,
                    after=lambda x=None: check_queue(context, context.message.guild.id),
                )
            else:
                msg = f"Error: song num: {song_number} not found."
        else:
            msg = "You are not in voice channel. Join the voice channel and then run the command."

    except discord.errors.ClientException as ex:
        msg = f"Command error: {ex}"
    finally:
        await context.send(msg)
        _logger("play", msg, context.author.mention)


@client.command(pass_context=True, brief="To queue the songs.")
async def queue(context, song_number: int):
    """To queue the songs."""
    msg = f"Queuing the song num{song_number}"
    try:
        if context.author.voice:

            if len(AUDIO) > song_number:
                msg = f"Queuing song num{song_number}: {AUDIO[song_number].split(os.path.sep)[-1]}"
                source = FFmpegPCMAudio(AUDIO[song_number])
                guild_id = context.message.guild.id

                if guild_id in song_queues:
                    song_queues[guild_id].append(source)
                else:
                    song_queues[guild_id] = [
                        source,
                    ]
        else:
            msg = "You are not in voice channel. Join the voice channel and then run the command."
    except discord.errors.ClientException as ex:
        msg = f"Command error: {ex}"
    finally:
        await context.send(msg)
        _logger("queue", msg, context.author.mention)
