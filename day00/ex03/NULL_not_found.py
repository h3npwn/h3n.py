def NULL_not_found(object: any) -> int:
    match object:
        case None:
            print('Nothing:', object, type(object))
        case x if isinstance(x, float) and x != x:
            print('Cheese:', x, type(x))
        case 0 if isinstance(object, int):
            print('Zero:', object, type(object))
        case "" if isinstance(object, str):
            print('Empty:', type(object))
        case False if isinstance(object, bool):
            print('Fake:', object, type(object))
        case _:
            print('Type not Found')
            return 1
    return 0