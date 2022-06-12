class IServer:
    def __str__(self) -> str:
        return str(self._Id)
    def Id(self) -> int:
        return self._Id