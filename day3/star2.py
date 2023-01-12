from sys import stdin


def convert_set(compartment: str) -> set:
    return set(compartment)


def in_common(compartment_a: set, compartment_b: set, compartment_c) -> set:
    return compartment_a.intersection(compartment_b).intersection(compartment_c)


def get_priority(item: str) -> int:
    ascii_position = ord(item)
    offset = 96
    if ascii_position <= ord("Z"):
        offset = 38
    ans = ascii_position - offset
    return ans


def calculate_priority(items: set) -> int:
    priorized_items = map(get_priority, items)
    return sum(priorized_items)


def main():
    total: int = 0
    line = stdin.readline()
    while line:
        rucksacks1 = line.strip()
        rucksacks2 = stdin.readline().strip()
        rucksacks3 = stdin.readline().strip()
        compartment_a = convert_set(rucksacks1)
        compartment_b = convert_set(rucksacks2)
        compartment_c = convert_set(rucksacks3)
        common_items = in_common(compartment_a, compartment_b, compartment_c)
        total += calculate_priority(common_items)
        line = stdin.readline().strip()
    print(total)


main()
