from discord import Client
from Features.Tools.Discord.makeEmbed import makeEmbed
from Features.Tools.Utils.getMoment import getMoment
import datetime


async def logsFabric(
    _Client:Client, _Id_Channel_Logs:int,
    _Arg1, _Value1,
    _Arg2 = None, _Value2 = None,
    _Arg3 = None, _Value3 = None,
    _Arg4 = None, _Value4 = None,
    _Arg5 = None, _Value5 = None,
    _Arg6 = None, _Value6 = None,
    _Arg7 = None, _Value7 = None,
    _Arg8 = None, _Value8 = None,
    _Arg9 = None, _Value9 = None,
    _Arg10 = None, _Value10 = None,
    _Arg11 = None, _Value11 = None,
    _Arg12 = None, _Value12 = None,
    _Arg13 = None, _Value13 = None,
    _Arg14 = None, _Value14 = None
) -> None:
    args = [_Arg1, _Arg2, _Arg3, _Arg4, _Arg5, _Arg6, _Arg7, _Arg8, _Arg9, _Arg10, _Arg11, _Arg12, _Arg13, _Arg14]
    values = [_Value1, _Value2, _Value3, _Value4, _Value5, _Value6, _Value7, _Value8, _Value9, _Value10, _Value11, _Value12, _Value13, _Value14]
    log = []
    for argNumber in range(0, len(args)):
        if args[argNumber] != None:
            if values[argNumber] not in (None, ''):
                log.append([str(args[argNumber]), str(values[argNumber]), False])
                continue
            elif args[argNumber] == 'Content' and values[argNumber] in (None, ''):
                log.append([str(args[argNumber]), 'There\'s no content', True])
                continue
            log.append([str(args[argNumber]), 'Ocourred an problem with this value', True])
            
    ChannelLog = _Client.get_channel(_Id_Channel_Logs)
    if (ChannelLog == None):
        print('Inconsistência ao procurar o canal de logs.')
        await _Client.close()
        exit()
    # Criação de um embed com as informações para facilitar visualização
    newEmbed = await makeEmbed(
        _Title = await getMoment(_IsoFormat=True),
        _Description = '',
        _Fields = log
    )
    await ChannelLog.send(embed=newEmbed)
    return
