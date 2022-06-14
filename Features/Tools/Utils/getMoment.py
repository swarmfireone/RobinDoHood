from datetime import datetime


async def getMoment(_IsoFormat:bool = True, _KindOfSeparatorDate:str = '.', _KindOfSeparatorTime:str = ':', _WithHours:bool = True) -> str:
    KosD = _KindOfSeparatorDate
    KosT = _KindOfSeparatorTime
    if _IsoFormat:
        datetimeFormated = datetime.now().isoformat()
    elif _WithHours:
        Format = '%d{0}%b{1}%Y, %H{2}%M{3}%S'.format(KosD, KosD, KosT, KosT)
        datetimeFormated = datetime.now().strftime(Format)
    else:
        Format = '%d{0}%b{1}%Y'.format(KosD, KosD)
        datetimeFormated = datetime.now().strftime(Format)
    return datetimeFormated