from discord import Intents

class ConfigureIntents:
    """
    Default: 
    
    Dm -> messages, reactions
    
    Guild -> messages, reactions
    
    Guilds
    
    Members
    """
    
    def Default() -> Intents:
        ClientIntents = Intents.none()
        ClientIntents.dm_messages = True
        ClientIntents.dm_reactions = True
        ClientIntents.guild_messages = True
        ClientIntents.guild_reactions = True
        ClientIntents.guilds = True
        ClientIntents.members = True
        return ClientIntents

    def new(self):
        self.ClientIntents = Intents.none()
        return self
    
    def active_dm(self):
        self.ClientIntents.dm_messages = True
        self.ClientIntents.dm_reactions = True
        return self
    
    def active_guild(self):
        self.ClientIntents.guild_messages = True
        self.ClientIntents.guild_reactions = True
        return self
    
    def active_guilds(self):
        self.ClientIntents.guilds = True
        return self
    
    def active_members(self):
        self.ClientIntents.members = True
        return self
    
    def returnIntents(self) -> Intents:
        return self.ClientIntents
