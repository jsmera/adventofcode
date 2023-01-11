from sys import stdin


def main():
    accum_calories = 0
    elves_calories: list = []

    for line in stdin:
        cleaned_line: str = line.strip()
        if cleaned_line.isdigit():
            accum_calories += int(cleaned_line)
        else:
            elves_calories.append(accum_calories)
            accum_calories = 0
    elves_calories.sort()
    top3_calories = elves_calories[-3:]
    total_top3 = sum(top3_calories)
    print(total_top3)


main()
