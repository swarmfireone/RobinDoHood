from Domain.Interfaces.Discord.Utils.IUser import IUser


class Lazarus_User(IUser):
    def __init__(self, _User_Id) -> None:
        isIdUser_StringOrInteger = type(_User_Id) == str or type(_User_Id) == int
        if isIdUser_StringOrInteger:
            isIdUser_EighteenLong = len(_User_Id) == 18
            if isIdUser_EighteenLong:
                Lazarus_User._Id = int(_User_Id)
