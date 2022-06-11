from Domain.Interfaces.Discord.Utils.IUser import IUser


class Lazarus_User(IUser):
    def __init__(self, User_Id) -> None:
        isIdUser_StringOrInteger = type(User_Id) == str or type(User_Id) == int
        if isIdUser_StringOrInteger:
            isIdUser_EighteenLong = len(User_Id) == 18
            if isIdUser_EighteenLong:
                Lazarus_User._Id = int(User_Id)
