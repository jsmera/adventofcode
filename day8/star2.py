from sys import stdin


def main():
    grid = []

    for line in stdin:
        grid_str = line.strip()
        grid.append(list(map(int, grid_str)))

    N = len(grid)
    M = len(grid[0])
    high_score = float("-inf")

    for i in range(1, N - 1):
        for j in range(1, M - 1):
            candidate = grid[i][j]
            left = 0
            for z in reversed(range(j)):
                left += 1
                if candidate <= grid[i][z]:
                    break

            right = 0
            for z in range(j + 1, M):
                right += 1
                if candidate <= grid[i][z]:
                    break

            top = 0
            for z in reversed(range(i)):
                top += 1
                if candidate <= grid[z][j]:
                    break

            down = 0
            for z in range(i + 1, N):
                down += 1
                if candidate <= grid[z][j]:
                    break

            score = left * right * top * down

            high_score = max(high_score, score)

    print(high_score)


main()
