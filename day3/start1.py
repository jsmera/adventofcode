from sys import stdin


def convert_set(compartment: str) -> set:
    return set(compartment)


def in_common(compartment_a: set, compartment_b: set) -> set:
    return compartment_a.intersection(compartment_b)


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
    for line in stdin:
        rucksacks = line.strip()
        cut_index = len(rucksacks) // 2
        compartment1 = rucksacks[:cut_index]
        compartment2 = rucksacks[cut_index:]
        compartment_a = convert_set(compartment1)
        compartment_b = convert_set(compartment2)
        common_items = in_common(compartment_a, compartment_b)
        total += calculate_priority(common_items)
    print(total)


main()
