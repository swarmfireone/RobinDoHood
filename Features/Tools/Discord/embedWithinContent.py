from discord import Embed


async def embedWithinContent(
    _ListOf_Embeds:list[Embed]
) -> dict:
    # Lê as informações do message.embeds
    listOfEmbeds = []
    for embed in _ListOf_Embeds:
        if embed.Empty != True:
            listOfEmbeds.append(
                {
                    "Embed_Author" : embed.author,
                    "Embed_Colour" : embed.colour,
                    "Embed_Description" : embed.description,
                    "Embed_Fields" : embed.fields,
                    "Embed_Footer" : embed.footer,
                    "Embed_Image" : embed.image,
                    "Embed_Provider" : embed.provider,
                    "Embed_Thumbnail" : embed.thumbnail,
                    "Embed_Timestamp" : embed.timestamp,
                    "Embed_Title" : embed.title,
                    "Embed_Type" : embed.type,
                    "Embed_URl" : embed.url,
                    "Embed_Video" : embed.video
                })
    dictOfEmbeds = {"counter" : len(listOfEmbeds), "embeds" : listOfEmbeds}
    return dictOfEmbeds
