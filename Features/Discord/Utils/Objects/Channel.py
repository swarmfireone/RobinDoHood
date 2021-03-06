from Domain.Interfaces.Discord.Utils.IChannel import IChannel

class Lazarus_Channel(IChannel):
    def __init__(self, _Id_Channel, Id_Server) -> None:
        isIdChannel_StringOrInteger = type(_Id_Channel) == str or type(_Id_Channel) == int
        isIdServer_StringOrInteger = type(Id_Server) == str or type(Id_Server) == int
        if isIdChannel_StringOrInteger and isIdServer_StringOrInteger:
            isIdChannel_EighteenLong = len(_Id_Channel) == 18
            isIdServer_EighteenLong = len(Id_Server) == 18
            if isIdChannel_EighteenLong and isIdServer_EighteenLong:
                Lazarus_Channel._Id = int(_Id_Channel)
                Lazarus_Channel._Server = int(Id_Server)
