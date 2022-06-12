async def validateGuild(
    _GuildId:int, _TargetGuild_Id:int
) -> bool:
    """
    Validate the message's guild 
    """ 
    print(f'\nMessage\'s Guild: {_GuildId} \nTarget Guild: {_TargetGuild_Id}')
    if _GuildId == _TargetGuild_Id:
        return True
    return False
