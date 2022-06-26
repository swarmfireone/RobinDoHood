from discord import Member
from discord.abc import Messageable


async def greetUser(_Member:Member, _LogChannel:Messageable):
    AccountMemberId = _Member.id
    
    GreetingGuild = 'Salveee <@{0}>, bem vindo(a) a Batcaverna! Vamos todos dar uma saudação sombria :bat::bat:'.format(AccountMemberId)
    GreetingDm = 'Seja bem-vindo, {0}!\nPara saber mais do server e se habituar bem, sugerimos que leia o canal <#{1}> :bat::bat:'.format(_Member.display_name, _LogChannel.id)
    
    await _LogChannel.send(GreetingGuild)
    await _Member.send(GreetingDm)
