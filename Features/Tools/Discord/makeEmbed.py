from Features.Tools.Utils.validateEmbedFields import validateEmbedFields
from datetime import datetime
from discord import Embed, Colour


async def makeEmbed(
    title:str,                      # Needed.
    description:str,                # Needed.
    author_name:str = '',
    author_url:str = '',
    author_icon:str = '',
    color:Colour = Colour.blurple(),
    fields:list = None,             # Must be validate every time
    footer_text:str = 'UTC-6 or CST',
    footer_iconUrl:str = '',      # The URL of the footer icon. Only HTTP(S) is supported.
    image:str = '',
    provider = '',                # What is this? https://discordpy.readthedocs.io/en/stable/api.html#embed
    thumbnail:str = '',
    timestamp:datetime = '',
    type = '',                    # It will be deprecated
    url:str = '',
    video:str = ''                # Video isn't the same as Image??
) -> Embed:

    newEmbed = Embed(title=title, description=description, url=url, timestamp=datetime.today(), colour=color)
    if await validateEmbedFields(fields) == True:
        for field in fields:
            if field != None : newEmbed.add_field(name = field[0], value = field[1], inline = field[2])
    if author_name != None : newEmbed.set_author(name = author_name, url = author_url, icon_url = author_icon)
    if footer_text != None : newEmbed.set_footer(text = footer_text, icon_url = footer_iconUrl)
    if image != None : newEmbed.set_image(url = image)
    if thumbnail != None : newEmbed.set_thumbnail(url = thumbnail)
    return newEmbed
