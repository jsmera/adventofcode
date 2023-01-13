from sys import stdin


def main():
    for line in stdin:
        cleaned_line: str = line.strip()

        start_of_packet = 1
        for i in range(len(cleaned_line) - 3):
            aux_set = set(cleaned_line[i : i + 4])
            if len(aux_set) == 4:
                start_of_packet = i + 3
                break
        print(start_of_packet + 1)


main()
