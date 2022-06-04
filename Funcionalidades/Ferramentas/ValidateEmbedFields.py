async def validateEmbedFields(
    fields:list
) -> bool:
    """
    Validate the fields list for emebed's construction
    Rules: 
    + [0] field_name is string
    + [1] field_text is string
    + [2] field_inline is bool
    """
    if fields == None or fields == []:
        print('Validate Embed Fields: fields None')
        return False
    for field in fields:
        haveThreeFields = len(field) == 3
        if haveThreeFields:
            firstFieldString =  isinstance(field[0], str)
            secondFieldString =  isinstance(field[1], str)
            thirdFieldBoolean =  isinstance(field[2], bool)
            if firstFieldString and secondFieldString and thirdFieldBoolean:
                continue
            print('Validate Embed Fields: failed at iteration ' + str(fields.index(field)))
            print(f'First Field - {type(field[0])} : {firstFieldString}, SecondField - {type(field[1])} : {secondFieldString}, ThirdField - {type(field[2])} : {thirdFieldBoolean}')
            return False
    return True