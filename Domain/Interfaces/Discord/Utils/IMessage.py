from Features.Discord.Utils.Objects.Server import Lazarus_Server
from Features.Discord.Utils.Objects.Channel import Lazarus_Channel


class IMessage:
    def __str__(self) -> str:
        return str(self._Id)
    def Server(self) -> int:
        return self._Server
    def Channel(self) -> int:
        return self._Channel
    def Id(self) -> int:
        return self._Id
    
    def validateServer(self, _Server:Lazarus_Server):
        return self._Server == _Server._Id
    def validateChannel(self, _Channel:Lazarus_Channel):
        return self._Channel == _Channel._Id
    
    def __validateMessage(_Id) -> bool:
        isId_StringOrInteger = type(_Id) == str or type(_Id) == int
        if isId_StringOrInteger:
            isId_EighteenLong = len(_Id) == 18
            if isId_EighteenLong : return True
        return False
    
    def validate(self, _Id_Message, _Id_Channel, _Id_Server) -> bool:
        for Id in [_Id_Message, _Id_Channel, _Id_Server]:
            if self.__validateMessage(Id) == False : return False
        return True
