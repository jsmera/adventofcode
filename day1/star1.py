from sys import stdin


def main():
    accum_calories: int = 0
    maximum_calories: float = float("-inf")

    for line in stdin:
        cleaned_line: str = line.strip()
        if cleaned_line.isdigit():
            accum_calories += int(cleaned_line)
        else:
            maximum_calories = max(accum_calories, maximum_calories)
            accum_calories = 0

    print(maximum_calories)


main()
