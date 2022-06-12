async def checkType(_Target, _Type, _WhatIsInsideMatters = False, _InsideType = None):
    if _Type == list:
        if _WhatIsInsideMatters == True and _InsideType == None:
            print('CheckType Function Exception: _InsideType variable is None, although _Type is List and _WhatIsInsideMatters is True')
            return
        IsTargetList = type(_Target) == list
        IsAnythingInside = len(_Target) > 0
        if IsTargetList and IsAnythingInside:
            for _itemInside in _Target:
                if type(_itemInside) != _InsideType:
                    print('CheckType Function Failed: _itemInside {0} isn\'t _InsideType {1}'.format(_Target.index(_itemInside), _InsideType))
            return True

    if _Target == _Type:
        return True
