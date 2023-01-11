from sys import stdin


def is_overlap(lo_a, hi_a, lo_b, hi_b):
    return (lo_a <= lo_b and hi_a >= hi_b) or (lo_a >= lo_b and hi_a <= hi_b)


def main():
    total = 0
    for line in stdin:
        raw_pair_a, raw_pair_b = line.strip().split(",")
        lo_a, hi_a = map(int, raw_pair_a.split("-"))
        lo_b, hi_b = map(int, raw_pair_b.split("-"))
        total += int(is_overlap(lo_a, hi_a, lo_b, hi_b))

    print(total)


main()
