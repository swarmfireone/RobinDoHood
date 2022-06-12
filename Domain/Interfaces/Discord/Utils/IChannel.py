class IChannel:
    def __str__(self) -> str:
        return str(self._Id)
    def Server(self) -> int:
        return self._Server
    def Id(self) -> int:
        return self._Id