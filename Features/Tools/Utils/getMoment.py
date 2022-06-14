from datetime import datetime


async def getMoment(_IsoFormat = True) -> str:
    if _IsoFormat:
        datetimeFormated = datetime.now().isoformat()
    else:
        datetimeFormated = datetime.now().strftime("%d.%b.%Y, %H:%M:%S")
    return datetimeFormated