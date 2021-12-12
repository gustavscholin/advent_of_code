def read_input(path: str, type: str = "str"):
    with open(path, "r") as f:
        if type == "str":
            return f.read().splitlines()
        elif type == "int":
            return [int(i) for i in f.read().splitlines()]
        else:
            raise Exception(f'Invalid type "{type}", should be "str" or "int"')


def read_input_single_line(path: str, type: str = "str", sep: str = ","):
    with open(path, "r") as f:
        if type == "str":
            return f.read().split(sep)
        elif type == "int":
            return [int(i) for i in f.read().split(sep)]
        else:
            raise Exception(f'Invalid type "{type}", should be "str" or "int"')


def read_input_as_matrix(path: str, type: str = "str"):
    with open(path, "r") as f:
        if type == "str":
            return [[i for i in row] for row in f.read().splitlines()]
        elif type == "int":
            return [[int(i) for i in row] for row in f.read().splitlines()]
        else:
            raise Exception(f'Invalid type "{type}", should be "str" or "int"')
