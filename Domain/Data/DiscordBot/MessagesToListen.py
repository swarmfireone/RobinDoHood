from Features.Discord.Utils.Objects.Message import Lazarus_Message


class Lazarus_MessagesToListen:
    __MessagesListened = {}
    
    def __init__(self, _MessagesListened:list[Lazarus_Message]):
        Counter = len(_MessagesListened)
        if Counter > 0:
            DictMessages = {"Counter" : Counter, "MessagesListened" : []}
            ListMessages = []
            for Message in _MessagesListened:
                ListMessages.append(Message)
            DictMessages["MessagesListened"] = ListMessages
            self.__MessagesListened = DictMessages
        return self
    
    
    def addMessage(self, _Id_Message, _Id_Channel, _Id_Server):
        if Lazarus_Message.validate(_Id_Message, _Id_Channel, _Id_Server) != True : return False
        self.__MessagesListened["MessagesListened"].append(
           Lazarus_Message(_Id_Message, _Id_Channel, _Id_Server)
        )
        self.__MessagesListened["Counter"] = self.__MessagesListened["Counter"] + 1
        return self
        
        
    def deleteMessage(self, _Id_Message, _Id_Channel, _Id_Server):
        if Lazarus_Message.validate(_Id_Message, _Id_Channel, _Id_Server) != True : return False
        self.__MessagesListened["MessagesListened"].remove(
           Lazarus_Message(_Id_Message, _Id_Channel, _Id_Server)
        )
        self.__MessagesListened["Counter"] = self.__MessagesListened["Counter"] - 1
        return self
    
    
    def returnMessages(self) -> list:
        return self.__MessagesListened["MessagesListened"]
    
    
    def countMessages(self) -> int:
        return self.__MessagesListened["Counter"]
    
    
    async def beingListen(self, _Id_Message, _Id_Channel, _Id_Server) -> bool:
        if Lazarus_Message.validate(_Id_Message, _Id_Channel, _Id_Server) != True : return False
        validateMessage = self.__MessagesListened["MessagesListened"].find(
            Lazarus_Message(_Id_Message, _Id_Channel, _Id_Server)
        )
        if validateMessage != 0:
            return True
        return False
