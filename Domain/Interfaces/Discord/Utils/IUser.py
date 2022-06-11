class IUser():
    def __str__(self) -> str:
        return str(IUser._Id)
    def Id() -> int:
        return IUser._Id