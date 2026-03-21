def typecounter(thelist):
    STR=0
    TUPLE=0
    INT=0
    FLOAT=0
    LIST=0

    for i in thelist:
        if type(i)==str:
            STR=STR+1
        if type(i)==tuple:
            TUPLE=TUPLE+1
        if type(i)==int:
            INT=INT+1
        if type(i)==float:
            FLOAT=FLOAT+1
        if type(i)==list:
            LIST=LIST+1
    D = {list: LIST, int: INT, float: FLOAT, str: STR, tuple: TUPLE }
    print(D)
    return D