from utils.read_input import read_input


class Node(object):
    def __init__(self, name, parent=None):
        self.name = name
        self.data = 0
        self.parent = parent
        self.children = []

    def add_data(self, val):
        self.data += val
        if self.parent is not None:
            self.parent.add_data(val)

    def add_child(self, obj):
        self.children.append(obj)

    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child


if __name__ == "__main__":
    commands = read_input("2022/day_7/input.txt")
    root = Node("/")
    current_dir = root
    dirs = [root]

    for i in range(1, len(commands)):
        if commands[i] == "$ cd ..":
            current_dir = current_dir.parent
        elif "$ cd " in commands[i]:
            current_dir = current_dir.get_child(commands[i].split()[2])
        elif commands[i].split()[0] == "dir":
            new_dir = Node(commands[i].split()[1], current_dir)
            current_dir.add_child(new_dir)
            dirs.append(new_dir)
        elif commands[i].split()[0].isdigit():
            current_dir.add_data(int(commands[i].split()[0]))

    print(sum([d.data if d.data < 100_000 else 0 for d in dirs]))
