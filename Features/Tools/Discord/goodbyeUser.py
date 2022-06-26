from discord import Member
from discord.abc import Messageable


async def goodbyetUser(_Member:Member, _LogChannel:Messageable):
    AccountMemberId = _Member.id
    
    GoodbyeGuild = 'Vá em paz <@{0}>. Quero jabuticaba, perna de anão, agora que saiu do server, nunca mais vai ganhar um aumento não!!!!'.format(AccountMemberId)
    
    await _LogChannel.send(GoodbyeGuild)
