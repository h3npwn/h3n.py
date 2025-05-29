def all_thing_is_obj(obj: any) -> int:
    match obj:
        case list():
            print("List :", type(obj))
        case tuple():
            print("Tuple :", type(obj))
        case set():
            print("Set :", type(obj))
        case dict():
            print("Dict :", type(obj))
        case str():
            print(f"{obj} is in the kitchen :", type(obj))
        case _:
            print("Type not found")
    return 1337
