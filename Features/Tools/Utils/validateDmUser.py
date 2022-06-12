async def validateDmUser(
    _User_Id:int, _TagetUser_Id:int
) -> bool:
    """
    Validate the message's author
    """ 
    print(f'\nMessage\'s Author: {_User_Id} \nTarget Author: {_TagetUser_Id}')
    if _User_Id == _TagetUser_Id:
        return True
    return False
