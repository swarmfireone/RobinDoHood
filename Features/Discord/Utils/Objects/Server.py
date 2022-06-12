from Domain.Interfaces.Discord.Utils.IServer import IServer

class Lazarus_Server(IServer):
    def __init__(self, _Id_Server) -> None:
        isIdServer_StringOrInteger = type(_Id_Server) == str or type(_Id_Server) == int
        if isIdServer_StringOrInteger:
            isIdServer_EighteenLong = len(_Id_Server) == 18
            if isIdServer_EighteenLong:
                Lazarus_Server._Id = int(_Id_Server)
