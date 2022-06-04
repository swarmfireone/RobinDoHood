import json
with open('Componentes/Secrets/Secrets.json', 'r') as secrets_json:
    SecretsJson = json.load(secrets_json)
    # Declaração de variáveis
    TokenRobinDoHood = str(SecretsJson["TokenRobinDoHood"])
    IdServerOficial = int(SecretsJson["IdServerOficial"])
    IdServerTeste = int(SecretsJson["IdServerTeste"])
    IdChannelLogs = int(SecretsJson["IdChannelLogs"])
    IdContaSwarmfire = int(SecretsJson["IdContaSwarmfire"])
    IdContaDevpobrerico = int(SecretsJson["IdContaDevpobrerico"])
    
    # Verificação se os dados foram encontrados e carregados
    if IdContaSwarmfire != 484053771203379210:
        print('Inconsistência nos dados das Secrets, parando aplicação.')
        exit()
    
    secrets_json.close()



# Funções


import discord, tracemalloc
# Funções
from Componentes.Logs.GetLogs import logsFabric
from Funcionalidades.Ferramentas.ValidateGuild import validateGuild
from Funcionalidades.Ferramentas.EmbedWithinContent import embedWithinContent


Client = discord.Client(command_prefix='>')

@Client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(Client))
    await logsFabric(
        Client, IdChannelLogs,
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
    
    if await validateGuild(GuildId, IdServerTeste):
        if message.author != Client.user:
            await logsFabric(
                Client, IdChannelLogs,
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
        


Client.run(TokenRobinDoHood)