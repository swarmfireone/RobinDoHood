from discord.ext.commands.context import Context
from discord import Member, Permissions
from discord.abc import Messageable
from Features.Tools.Discord.makeEmbed import makeEmbed
from Features.Tools.Utils.getMoment import getMoment


async def warnUser(_Context:Context, _Member:Member, _Reason:str, _LogChannel:Messageable) -> None:
    # Check if it is a use for tests purposes
    IsARegularCall = _Reason.find('DDD021') == -1
    if IsARegularCall:
        # Check if the member has the permissions to invoke that command
        CanBanOrKickMembers:Permissions = _Context.author.permissions_in(channel=_Context.channel)
        CanBanOrKickMembers:bool = CanBanOrKickMembers.kick_members or CanBanOrKickMembers.kick_members
        if CanBanOrKickMembers != True:
            await _Context.send('Me respeita, rapá! Você não pode fazer isso, quero ver estalar dois dedos na tua oreia.')
            return
        
        # Check if the member to be kicked is the same as the administrator and has the rights permissions
        CanBanOrKickMembers:Permissions = _Member.permissions_in(channel=_Context.channel)
        CanBanOrKickMembers:bool = CanBanOrKickMembers.kick_members or CanBanOrKickMembers.kick_members
        if CanBanOrKickMembers or _Member == _Context.author:
            await _Context.send('You can\' warn yourself or people with kick / ban permissions')
            return
    
    
    WarnedMessage = ':bat: :bat: :bat:' + f'\n<@{_Member.id}>' + ' foi avisado!'
    Date = await getMoment(_IsoFormat=False, _KindOfSeparatorDate="/", _WithHours=False)
    Reason = f'**({Date}) - {_Reason}**'
    newEmbed = await makeEmbed(
        _Title='The Bruce Wayne has spoken',
        _Description=WarnedMessage,
        _Author_Name='Robin do Hood',
        _Author_Icon='https://cdn.discordapp.com/attachments/981836514579329064/986079281975267338/unknown.png',
        _Fields=[
            ['Motivo', Reason, False]
        ]
    )
    await _LogChannel.send(embed=newEmbed)
    await _Member.send(content='', embed=newEmbed)
    return
