from Features.Tools.Utils.checkType import checkType
from discord import Attachment


async def readAttachments(_List_Attachments:list[Attachment], _Type = Attachment):
    ValidateType = await checkType(_List_Attachments, list, True, _Type)
    if ValidateType == False:
        return
    
    # Lê as informações do message.attachments
    listOfAttachments = []
    for Attachment in _List_Attachments:
        listOfAttachments.append(
            {
                "Attachment_ContentType" : Attachment.content_type,
                "Attachment_Filename" : Attachment.filename,
                "Attachment_Height" : Attachment.height,
                "Attachment_Id" : Attachment.id,
                "Attachment_ProxyUrl" : Attachment.proxy_url,
                "Attachment_Size" : Attachment.size,
                "Attachment_Url" : Attachment.url,
                "Attachment_Width" : Attachment.width,
                "Attachment_IsSpoiler" : Attachment.is_spoiler()
            })
    dictOfAttachments = {"counter" : len(listOfAttachments), "Attachments" : listOfAttachments}
    return dictOfAttachments
        