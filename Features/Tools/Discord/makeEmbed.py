from Features.Tools.Utils.getMoment import getMoment
from Features.Tools.Utils.validateEmbedFields import validateEmbedFields
from datetime import datetime
from discord import Embed, Colour


async def makeEmbed(
    _Title:str,                      # Needed.
    _Description:str,                # Needed.
    _Author_Name:str = '',
    _Author_Url:str = '',
    _Author_Icon:str = '',
    _Color:Colour = Colour.blurple(),
    _Fields:list = None,             # Must be validate every time
    _Footer_Text:str = await getMoment(_IsoFormat=False),
    _Footer_IconUrl:str = '',      # The URL of the footer icon. Only HTTP(S) is supported.
    _Image:str = '',
    _Provider = '',                # What is this? https://discordpy.readthedocs.io/en/stable/api.html#embed
    _Thumbnail:str = '',
    _Timestamp:datetime = datetime.today(),
    _Type = '',                    # It will be deprecated
    _Url:str = '',
    _Video:str = ''                # Video isn't the same as Image??
) -> Embed:

    newEmbed = Embed(title=_Title, description=_Description, url=_Url, timestamp=_Timestamp, colour=_Color)
    if await validateEmbedFields(_Fields) == True:
        for field in _Fields:
            if field != None : newEmbed.add_field(name = field[0], value = field[1], inline = field[2])
    if _Author_Name != None : newEmbed.set_author(name = _Author_Name, url = _Author_Url, icon_url = _Author_Icon)
    if _Footer_Text != None : newEmbed.set_footer(text = _Footer_Text, icon_url = _Footer_IconUrl)
    if _Image != None : newEmbed.set_image(url = _Image)
    if _Thumbnail != None : newEmbed.set_thumbnail(url = _Thumbnail)
    return newEmbed
