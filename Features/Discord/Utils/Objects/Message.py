from Domain.Interfaces.Discord.Utils.IMessage import IMessage


class Lazarus_Message(IMessage):
    def __init__(self, _Id_Message, _Id_Channel, Id_Server) -> None:
        isIdMessage_StringOrInteger = type(_Id_Message) == str or type(_Id_Message) == int
        isIdChannel_StringOrInteger = type(_Id_Channel) == str or type(_Id_Channel) == int
        isIdServer_StringOrInteger = type(Id_Server) == str or type(Id_Server) == int
        if isIdMessage_StringOrInteger and isIdChannel_StringOrInteger and isIdServer_StringOrInteger:
            isIdMessage_EighteenLong = len(_Id_Message) == 18
            isIdChannel_EighteenLong = len(_Id_Channel) == 18
            isIdServer_EighteenLong = len(Id_Server) == 18
            if isIdMessage_EighteenLong and isIdChannel_EighteenLong and isIdServer_EighteenLong:
                Lazarus_Message._Id = int(_Id_Message)
                Lazarus_Message._Channel = int(_Id_Channel)
                Lazarus_Message._Server = int(Id_Server)
