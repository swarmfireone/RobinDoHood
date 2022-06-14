from discord.ext.commands.context import Context
from discord import Member, Permissions
from discord.abc import Messageable
from Features.Tools.Discord.makeEmbed import makeEmbed
from Features.Tools.Utils.getMoment import getMoment


async def banUser(_Context:Context, _Member:Member, _Reason:str, _LogChannel:Messageable) -> None:
    # Check if the member has the permissions to invoke that command
    CanBanOrKickMembers:Permissions = _Context.author.permissions_in(channel=_Context.channel)
    CanBanOrKickMembers:bool = CanBanOrKickMembers.ban_members or CanBanOrKickMembers.kick_members
    if CanBanOrKickMembers != True:
        await _Context.send('Me respeita, rapá! Você não pode fazer isso, quero ver estalar dois dedos na tua oreia.')
        return
    
    # Check if the member to be banned is the same as the administrator and has the rights permissions
    CanBanOrKickMembers:Permissions = _Member.permissions_in(channel=_Context.channel)
    CanBanOrKickMembers:bool = CanBanOrKickMembers.ban_members or CanBanOrKickMembers.kick_members
    if CanBanOrKickMembers or _Member == _Context.author:
        await _Context.send('You can\' ban yourself or people with kick / ban permissions')
        return
        
    else:
        BannedMessage = ':bat: RIP :bat:' + f'\n<@{_Member.id}>' + ' foi banido!'
        Date = await getMoment(_IsoFormat=False, _KindOfSeparatorDate="/", _WithHours=False)
        Reason = f'**({Date}) - {_Reason}**'
        newEmbed = await makeEmbed(
            _Title='The ban hammer has spoken',
            _Description=BannedMessage,
            _Author_Name='Robin do Hood',
            _Author_Icon='https://cdn.discordapp.com/attachments/981836514579329064/986079281975267338/unknown.png',
            _Fields=[
                ['Motivo', Reason, False]
            ]
        )
        await _LogChannel.send(embed=newEmbed)
        await _Member.send(content='Toma jeito agora, né.' ,embed=newEmbed)
        await _Member.ban()
        return
