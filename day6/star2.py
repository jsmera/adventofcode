from sys import stdin


def main():
    K = 14
    for line in stdin:
        cleaned_line: str = line.strip()

        start_of_packet = 1
        for i in range(len(cleaned_line) - K + 1):
            aux_set = set(cleaned_line[i : i + K])
            if len(aux_set) == K:
                start_of_packet = i + K
                break
        print(start_of_packet)


main()
