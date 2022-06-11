from Domain.Connection.DiscordBot.Secrets.GetSecrets import Secrets
import discord, tracemalloc
from Features.Tools.getLogs import logsFabric
from Features.Tools.embedWithinContent import embedWithinContent
from Features.Tools.validateGuild import validateGuild


# Secrets Data
SecretsData = Secrets('C:/Users/Pichau/Desktop/Python/Area_de_Testes/Programas/Discord/BatCaverna/Robin-do-Hood/RobinDoHood/Domain/Connection/DiscordBot/Secrets/Secrets.json')
Token_DiscordBot = SecretsData.returnToken_DiscordBot().Token()
Server_OficialServer = SecretsData.returnId_Server_OficialServer()
Server_TestServer = SecretsData.returnId_Server_TestServer()
Id_ChannelLogs = SecretsData.returnId_Channel_Logs()
Id_UserAdministrator = SecretsData.returnId_User_Administrator()


# Initialize Discord Bot and Define Behaviors
Client = discord.Client(command_prefix='>')

@Client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(Client))
    await logsFabric(
        Client, Id_ChannelLogs.Id,
        'Client connected with success', '#Success',
        'Logged in as user', f'{Client.user}\nwith id \n{Client.user.id}'
    )
    
@Client.event
async def on_message(message):
    GuildName = message.guild
    GuildId = message.guild.id
    ChannelName = message.channel
    ChannelId = message.channel.id
    Author = message.author
    AuthorId = message.author.id
    Content = message.content
    Embeds = await embedWithinContent(message.embeds)
    
    if await validateGuild(GuildId, Server_TestServer.Id):
        if message.author != Client.user:
            await logsFabric(
                Client, Id_ChannelLogs.Id,
                'GuildName', GuildName,
                'GuildId', GuildId,
                'ChannelName', ChannelName,
                'ChannelId', ChannelId,
                'Author', Author,
                'AuthorId', AuthorId,
                'Content', Content,
                'Embeds', Embeds['embeds']
            )
            
            if message.content.startswith('$hello'):
                await message.channel.send('Hello!')
                return


# Run Discord Bot
Client.run(Token_DiscordBot)
