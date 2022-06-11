from Features.Discord.Utils.Objects.Channel import Lazarus_Channel
from Features.Discord.Utils.Objects.Server import Lazarus_Server
from Domain.Connection.DiscordBot.Secrets.Objects.TokenDiscordBot import Lazarus_TokenDiscordBot
from Features.Discord.Utils.Objects.User import Lazarus_User


class Secrets:
    __ListOfVariables = {}
    
    def __init__(self, SecretsPath:str):
        import json
        with open(SecretsPath, 'r') as secrets_json:
            SecretsJson = json.load(secrets_json)
            # Declaração de variáveis
            self.__ListOfVariables['Token_DiscordBot'] = Lazarus_TokenDiscordBot(SecretsJson["Token_DiscordBot"])
            self.__ListOfVariables['Id_Server_OficialServer'] = Lazarus_Server(SecretsJson["Id_Server_OficialServer"])
            self.__ListOfVariables['Id_Server_TestServer'] = Lazarus_Server(SecretsJson["Id_Server_TestServer"])
            self.__ListOfVariables['Id_Channel_Logs'] = Lazarus_Channel(SecretsJson["Id_Channel_Logs"], SecretsJson["Id_Server_TestServer"])
            self.__ListOfVariables['Id_User_Administrator'] = Lazarus_User(SecretsJson["Id_User_Administrator"])

            # Verificação se os dados foram encontrados e carregados
            isThereAnyDiscordBotToken = self.__ListOfVariables['Token_DiscordBot'] != None
            isThereAnyOficialServer = self.__ListOfVariables['Id_Server_OficialServer'] != None
            isThereAnyTestServer = self.__ListOfVariables['Id_Server_TestServer'] != None
            isThereAnyLogsChannel = self.__ListOfVariables['Id_Channel_Logs'] != None
            isThereAnyAdministratorUser = self.__ListOfVariables['Id_User_Administrator'] != None
            if False in (isThereAnyDiscordBotToken, isThereAnyTestServer, isThereAnyLogsChannel, isThereAnyAdministratorUser) :
                print('Inconsistência nos dados das Secrets, parando aplicação.')
                exit()
            secrets_json.close()
      
    # Return all objects
    def returnVariables(self) -> list:
        return self.__ListOfVariables
    # Return especific object
    def returnToken_DiscordBot(self) -> Lazarus_TokenDiscordBot:
        return self.__ListOfVariables['Token_DiscordBot']
    def returnId_Server_OficialServer(self) -> Lazarus_Server:
        return self.__ListOfVariables['Id_Server_OficialServer']
    def returnId_Server_TestServer(self) -> Lazarus_Server:
        return self.__ListOfVariables['Id_Server_TestServer']
    def returnId_Channel_Logs(self) -> Lazarus_Channel:
        return self.__ListOfVariables['Id_Channel_Logs']
    def returnId_User_Administrator(self) -> Lazarus_User:
        return self.__ListOfVariables['Id_User_Administrator']
