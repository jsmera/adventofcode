from sys import stdin


def is_overlap(lo_a, hi_a, lo_b, hi_b):
    return max(lo_a, lo_b) <= min(hi_a, hi_b)


def main():
    total = 0
    for line in stdin:
        raw_pair_a, raw_pair_b = line.strip().split(",")
        lo_a, hi_a = map(int, raw_pair_a.split("-"))
        lo_b, hi_b = map(int, raw_pair_b.split("-"))
        total += int(is_overlap(lo_a, hi_a, lo_b, hi_b))

    print(total)


main()
