from Domain.Interfaces.Connection.DiscordBot.ITokenDiscordBot import ITokenDiscordBot


class Lazarus_TokenDiscordBot(ITokenDiscordBot):
    def __init__(self, Token_DiscordBot) -> None:
        isToken_String = type(Token_DiscordBot) == str
        if isToken_String:
            isToken_SeventyLong = len(Token_DiscordBot) == 70
            if isToken_SeventyLong:
                Lazarus_TokenDiscordBot._Token = Token_DiscordBot
