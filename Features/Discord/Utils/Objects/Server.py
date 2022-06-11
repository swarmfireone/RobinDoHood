from Domain.Interfaces.Discord.Utils.IServer import IServer

class Lazarus_Server(IServer):
    def __init__(self, Id_Server) -> None:
        isIdServer_StringOrInteger = type(Id_Server) == str or type(Id_Server) == int
        if isIdServer_StringOrInteger:
            isIdServer_EighteenLong = len(Id_Server) == 18
            if isIdServer_EighteenLong:
                Lazarus_Server._Id = int(Id_Server)
