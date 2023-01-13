import re
from sys import stdin
from typing import List, Optional, Tuple, TypeVar

TFileTree = TypeVar("TFileTree", bound="FileTree")

ALMOST_COUNTING = 100000


class FileTree:
    nodes: List[TFileTree]
    type: str
    parent: TFileTree
    size: Optional[int]

    def __init__(
        self,
        name: str,
        size: int = None,
        type: str = "file",
        parent: Optional[TFileTree] = None,
    ):
        self.parent = parent
        self.type = type
        self.name = name
        self.size = size
        self.nodes = []

    def add_node(self, name: str, size: int = None, type: str = "file"):
        new_node = FileTree(name, size=size, type=type, parent=self)
        self.nodes.append(new_node)

    def get_nodes(self) -> List[TFileTree]:
        return self.nodes

    def is_dir(self) -> bool:
        return self.type == "dir"

    def go_dir(self, destination: str) -> Optional[TFileTree]:
        dir_nodes = filter(lambda node: node.is_dir(), self.nodes)
        dir_match = list(filter(lambda node: node.name == destination, dir_nodes))
        return dir_match.pop()

    def go_back(self) -> TFileTree:
        if self.parent is None:
            return self
        return self.parent

    def total_size(self) -> Tuple[int, int]:
        total_counting_size = 0
        me_size = self.size
        if self.is_dir():
            me_size = 0
            for node in self.nodes:
                node_size, counting_size = node.total_size()
                me_size += node_size
                total_counting_size += counting_size

            if me_size <= ALMOST_COUNTING:
                total_counting_size += me_size
        return me_size, total_counting_size


def is_command(buff) -> bool:
    return re.search(r"\$ (cd|ls)", buff) is not None


def parse_command_cd(buff: str, pointer: TFileTree, root: TFileTree) -> TFileTree:
    matched = re.search(r"\$ cd (?P<dir_name>[\w|\.|\/]+)", buff)
    dir_name = matched.group("dir_name")
    if dir_name == "..":
        return pointer.go_back(), buff
    elif dir_name == "/":
        return root, buff
    else:
        return pointer.go_dir(dir_name), buff


def parse_command_ls(pointer: TFileTree) -> Tuple[TFileTree, str]:
    sub_buff: str = stdin.readline().strip()
    while sub_buff and not is_command(sub_buff):
        dir_detail = re.search(r"dir (?P<dir_name>[\w|\.]+)", sub_buff)
        if dir_detail:
            dir_name = dir_detail.group("dir_name")
            pointer.add_node(dir_name, type="dir")
        else:
            file_details = re.search(
                r"(?P<size>[\d]+) (?P<file_name>[\w|\.]+)", sub_buff
            )
            file_name = file_details.group("file_name")
            size = int(file_details.group("size"))
            pointer.add_node(file_name, size=size, type="file")

        sub_buff: str = stdin.readline().strip()
    return pointer, sub_buff


def parse_command(
    buff: str, pointer: TFileTree, root: TFileTree
) -> Tuple[TFileTree, str, str]:
    if re.search(r"\$ cd", buff):
        return (*parse_command_cd(buff, pointer, root), "cd")
    if re.search(r"\$ ls", buff):
        return (*parse_command_ls(pointer), "ls")


def main():
    root: TFileTree = FileTree("/", type="dir")
    pointer: TFileTree = root
    buff: str = stdin.readline().strip()

    while buff:
        pointer, sub_buff, operation = parse_command(buff, pointer, root)
        if operation == "ls":
            buff = sub_buff
            continue
        buff = stdin.readline().strip()

    _, total_ans = root.total_size()
    print(total_ans)


main()
