from sys import stdin

ROCK = "Rock"
PAPPER = "Papper"
SCISSORS = "Scissors"


def normalize_opponent_reason(reason: str):
    mapper = {
        "A": ROCK,
        "B": PAPPER,
        "C": SCISSORS,
    }
    return mapper.get(reason)


def normalize_me_reason(party_scam: str, normalized_opponent_reason: str):
    lose = {
        ROCK: SCISSORS,
        PAPPER: ROCK,
        SCISSORS: PAPPER,
    }
    win = {
        ROCK: PAPPER,
        PAPPER: SCISSORS,
        SCISSORS: ROCK,
    }
    # I lose
    if party_scam == "X":
        return lose.get(normalized_opponent_reason)
    # I win
    elif party_scam == "Z":
        return win.get(normalized_opponent_reason)
    # Draw
    return normalized_opponent_reason


def calculate_reason(reason: str):
    mapper = {
        ROCK: 1,
        PAPPER: 2,
        SCISSORS: 3,
    }
    return mapper.get(reason)


def calculate_party(opponent_reason, me_reason):
    if opponent_reason == me_reason:
        return 3
    if opponent_reason == ROCK and me_reason == SCISSORS:
        return 0
    if opponent_reason == SCISSORS and me_reason == PAPPER:
        return 0
    if opponent_reason == PAPPER and me_reason == ROCK:
        return 0
    return 6


def main():
    total: int = 0
    for line in stdin:
        opponent_reason, party_scam = line.strip().split()
        normalized_opponent_reason = normalize_opponent_reason(opponent_reason)
        normalized_me_reason = normalize_me_reason(
            party_scam, normalized_opponent_reason
        )

        party = calculate_party(
            normalized_opponent_reason, normalized_me_reason
        ) + calculate_reason(normalized_me_reason)
        total += party
    print(total)


main()
