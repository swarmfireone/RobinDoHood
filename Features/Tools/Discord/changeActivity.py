from itertools import cycle
import discord
from discord.ext import commands
from discord.abc import Messageable


async def changeActivity(_Client:commands.Bot, _ListOf_Status:cycle, _LogChannel:Messageable) -> None:
    # Check current Activity
    currentActivity = _Client.activity
    newActivity = next(_ListOf_Status)
    await _Client.change_presence(
        activity=discord.Game(newActivity)
    )
    return
    