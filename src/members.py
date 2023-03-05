"""Managing the users in the server"""


# Third-party libraries.
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

from src.discord_main import client
from src.discord_main import _logger


@client.command(pass_context=True, brief="To kick the member.")
@has_permissions(kick_members=True)
async def kick(context, member: discord.Member, *, reason=None):
    """Kick a member based on some reason.

    Args:
        context (_type_): Context of the discord serever to handle various operations
        member (discord.member): Mentiopned usert to be kicked
        reason (Str, optional): Reason why to kick. Defaults to None.
    """
    msg = f"User {member} has been kicked"
    print("-------------------------------------------")
    try:
        await member.kick(reason=reason)
        await context.send(msg)
    except Exception as ex:
        msg = f"Error: {ex}"
    finally:
        _logger("kick", msg, context.author.mention)


@kick.error
async def kick_error(context, error):
    """Handling the permission error for the kick command"""
    if isinstance(error, commands.MissingPermissions):
        msg = "You dont have the permissions to kick people!"
        await context.send(msg)
        _logger("kick", msg, context.author.mention)


@client.command(pass_context=True, brief="To ban the member.")
@has_permissions(ban_members=True)
async def ban(context, member: discord.Member, *, reason=None):
    """ban a member based on some reason.

    Args:
        context (_type_): Context of the discord serever to handle various operations
        member (discord.member): Mentiopned usert to be baned
        reason (Str, optional): Reason why to ban. Defaults to None.
    """
    msg = f"User {member} has been baned"
    try:
        await member.ban(reason=reason)
        await context.send(msg)
    except Exception as ex:
        msg = f"Error: {ex}"
    finally:
        _logger("ban", msg, context.author.mention)


@ban.error
async def ban_error(context, error):
    if isinstance(error, MissingPermissions):
        msg = "You dont have the permissions to ban people!"
        await context.send(msg)
        _logger("ban_error", msg, context.author.mention)
