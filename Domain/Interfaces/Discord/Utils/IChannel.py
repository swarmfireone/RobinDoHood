class IChannel:
    def __str__(self) -> str:
        return str(IChannel._Id)
    def Server() -> int:
        return IChannel._Server
    def Id() -> int:
        return IChannel._Id