import re
from sys import stdin


def main():
    horizontal_crane = stdin.readline().rstrip("\n")
    viewports = []

    while not all(map(lambda item: item.isdigit(), horizontal_crane.split())):
        viewports.append(horizontal_crane)
        horizontal_crane = stdin.readline().rstrip("\n")

    n_stack = len(horizontal_crane.split())
    stacks = [list() for _ in range(n_stack)]
    viewports.reverse()

    for viewport in viewports:
        for i in range(0, len(viewport), 4):
            crates = viewport[i + 1].strip()
            if crates:
                stack_index = i // 4
                stacks[stack_index].append(crates)

    # Empty line
    stdin.readline().strip()

    line = stdin.readline().strip()
    while line:
        raw_command = re.match(r"move (\d+) from (\d+) to (\d+)", line).groups()
        load, from_stack, to_stack = map(int, raw_command)
        for _ in range(load):
            crate = stacks[from_stack - 1].pop()
            stacks[to_stack - 1].append(crate)
        line = stdin.readline().strip()

    top_stacks = map(lambda stack: stack.pop(), stacks)
    print("".join(top_stacks))


main()
