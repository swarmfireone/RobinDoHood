from discord import Client
from Features.Tools.makeEmbed import makeEmbed
import datetime


async def logsFabric(
    client:Client, IdChanneLogs:int,
    arg1, value1,
    arg2 = None, value2 = None,
    arg3 = None, value3 = None,
    arg4 = None, value4 = None,
    arg5 = None, value5 = None,
    arg6 = None, value6 = None,
    arg7 = None, value7 = None,
    arg8 = None, value8 = None,
    arg9 = None, value9 = None,
    arg10 = None, value10 = None,
    arg11 = None, value11 = None,
    arg12 = None, value12 = None,
    arg13 = None, value13 = None,
    arg14 = None, value14 = None
) -> None:
    args = [arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14]
    values = [value1, value2, value3, value4, value5, value6, value7, value8, value8, value9, value10, value11, value12, value13, value14]
    log = []
    for argNumber in range(0, len(args)):
        if args[argNumber] != None:
            log.append([str(args[argNumber]), str(values[argNumber]), False])
            
    ChannelLog = client.get_channel(IdChanneLogs)
    if (ChannelLog == None):
        print('Inconsistência ao procurar o canal de logs.')
        exit()
    # Criação de um embed com as informações para facilitar visualização
    newEmbed = await makeEmbed(
        title = f'{datetime.datetime.today()}',
        description = '',
        fields = log
    )
    await ChannelLog.send(embed=newEmbed)
    return
