from Features.Discord.Utils.Objects.User import Lazarus_User


class Lazarus_Administrators:
    __Administrators = {}
    
    def __init__(self, _Administrators:list[Lazarus_User]):
        Counter = len(_Administrators)
        if Counter > 0:
            DictAdministrator = {"Counter" : Counter, "Administrators" : []}
            ListAdministrator = []
            for User in _Administrators:
                ListAdministrator.append(User)
            DictAdministrator["Administrators"] = ListAdministrator
            self.__Administrators = DictAdministrator
        return self

    
    def addAdministrator(self, _User:Lazarus_User):
        self.__Administrators["Administrators"].append(_User)
        self.__Administrators["Counter"] = self.__Administrators["Counter"] + 1
        return self
        
    def deleteAdministrator(self, _User:Lazarus_User):
        self.__Administrators["Administrators"].remove(_User)
        self.__Administrators["Counter"] = self.__Administrators["Counter"] - 1
        return self
    
    def returnAdministrators(self) -> list[Lazarus_User]:
        return self.__Administrators["Administrators"]
    
    def countAdministrators(self) -> int:
        return self.__Administrators["Counter"]
    
    def isAdmin(self, _User:Lazarus_User) -> bool:
        validateAdmin = self.__Administrators["Administrators"].find(_User)
        if validateAdmin != 0:
            return True
        return False