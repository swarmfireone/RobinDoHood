from Domain.Connection.DiscordBot.Secrets.GetSecrets import Secrets
import discord, tracemalloc
from Features.Tools.Discord.readAttachments import readAttachments
from Features.Tools.Utils.getLogs import logsFabric
from Features.Tools.Discord.embedWithinContent import embedWithinContent
from Features.Tools.Utils.validateDmUser import validateDmUser
from Features.Tools.Utils.validateGuild import validateGuild


# Secrets Data
SecretsData = Secrets('C:/Users/Pichau/Desktop/Python/Area_de_Testes/Programas/Discord/BatCaverna/Robin-do-Hood/RobinDoHood/Domain/Connection/DiscordBot/Secrets/Secrets.json')
Token_DiscordBot = SecretsData.returnToken_DiscordBot().Token()
Server_OficialServer = SecretsData.returnId_Server_OficialServer()
Server_TestServer = SecretsData.returnId_Server_TestServer()
Id_ChannelLogs = SecretsData.returnId_Channel_Logs()
Id_UserAdministrator = SecretsData.returnId_User_Administrator()


# Initialize Discord Bot and Define Behaviors
Client = discord.Client(command_prefix='$')

@Client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(Client))
    await logsFabric(
        Client, Id_ChannelLogs._Id,
        'Client connected with success', '#Success',
        'Logged in as user', f'{Client.user}\nwith id \n{Client.user.id}'
    )
    
    
@Client.event
async def on_message(message):
    # Para mensagens enviadas pela DM, nem sempre terão Guild
    if message.guild != None:
        GuildName = message.guild
        GuildId = message.guild.id
    else:
        GuildName = 'It\'s not a server\'s message'
        GuildId = 'It\'s a direct message'
    ChannelName = message.channel
    ChannelId = message.channel.id
    Author = message.author
    AuthorId = message.author.id
    Content = message.content
    Attachment = await readAttachments(message.attachments)
    Embeds = await embedWithinContent(message.embeds)
    
    if await validateGuild(GuildId, Server_TestServer._Id) or await validateDmUser(AuthorId, Id_UserAdministrator):
        if message.author != Client.user:
            await logsFabric(
                Client, Id_ChannelLogs._Id,
                'GuildName', GuildName,
                'GuildId', GuildId,
                'ChannelName', ChannelName,
                'ChannelId', ChannelId,
                'Author', Author,
                'AuthorId', AuthorId,
                'Content', Content,
                'Attachment', Attachment,
                'Embeds', Embeds['embeds']
            )
            
            if message.content.startswith('$hello'):
                await message.channel.send('Hello!')
                return
            
            if message.content.startswith('$close'):
                await message.channel.send('Closing the application right away, sir!')
                await Client.close()
                return



# Run Discord Bot
Client.run(Token_DiscordBot)
