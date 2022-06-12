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
async def on_message(message:discord.Message):
    # Para mensagens enviadas pela DM, nem sempre terão Guild
    if message.guild != None : GuildName = message.guild; GuildId = message.guild.id
    else : GuildName = 'It\'s not a server\'s message'; GuildId = 'It\'s a direct message'
    ChannelName = message.channel
    ChannelId = message.channel.id
    Author = message.author
    AuthorId = message.author.id
    MessageId = message.id
    JumpUrl = message.jump_url
    if message.reference != None : MessageReference = message.reference
    else : MessageReference = 'There\'s not a Reference field'
    Content = message.content
    Attachments = await readAttachments(message.attachments)
    Embeds = await embedWithinContent(message.embeds)
    
    if message.author != Client.user:
        IsGuildOkay = await validateGuild(GuildId, Server_TestServer._Id)
        if IsGuildOkay:
            await logsFabric(
                Client, Id_ChannelLogs._Id,
                'GuildName', GuildName,
                'GuildId', GuildId,
                'ChannelName', ChannelName,
                'ChannelId', ChannelId,
                'Author', Author,
                'AuthorId', AuthorId,
                'MessageId', MessageId,
                'MessageReference', MessageReference,
                'Content', Content,
                'Attachments', Attachments,
                'Embeds', Embeds,
                'JumpUrl', JumpUrl
            )
            if message.content.startswith('$hello'):
                await message.channel.send('Hello!')
                return
            
            elif message.content.startswith('$close'):
                await message.channel.send('Closing the application right away, sir!')
                await Client.close()
                return
        else:
            IsDmUserOkay = await validateDmUser(AuthorId, Id_UserAdministrator._Id)
            if IsDmUserOkay:
                await logsFabric(
                Client, Id_ChannelLogs._Id,
                'ChannelName', ChannelName,
                'ChannelId', ChannelId,
                'Author', Author,
                'AuthorId', AuthorId,
                'MessageId', MessageId,
                'MessageReference', MessageReference,
                'Content', Content,
                'Attachments', Attachments,
                'Embeds', Embeds,
                'JumpUrl', JumpUrl
                )
                if Content != None and Attachments['Attachments'] == Embeds['Embeds']:
                    await message.channel.send('Message processed with success!')
                    await message.channel.send(Content)
                    return
                



# Run Discord Bot
Client.run(Token_DiscordBot)
