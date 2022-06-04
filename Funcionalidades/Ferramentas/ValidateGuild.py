async def validateGuild(
    guildId:int, targetGuildId:int
) -> bool:
    """
    Validate the message's guild 
    """ 
    print(f'\nMessage\'s Guild: {guildId} \nTarget Guild: {targetGuildId}')
    if guildId == targetGuildId:
        return True
    return False