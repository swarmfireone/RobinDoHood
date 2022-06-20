from itertools import cycle
import discord
from discord.ext.commands.context import Context
from discord.ext import commands
from discord.abc import Messageable


async def changeActivity(_Client:commands.Bot, _Ctx:Context, _NewActivity:str, _ListOf_Status:cycle, _LogChannel:Messageable) -> None:
    # Check if the change is for the content of the message
    if _NewActivity != None : newActivity = _NewActivity
    else : newActivity = next(_ListOf_Status)

    await _Client.change_presence(
        activity=discord.Game(newActivity)
    )
    return
    