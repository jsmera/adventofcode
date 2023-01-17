from sys import stdin


def main():
    grid = []

    for line in stdin:
        grid_str = line.strip()
        grid.append(list(map(int, grid_str)))

    N = len(grid)
    M = len(grid[0])
    reversed_grid = [[grid[j][i] for j in range(N)] for i in range(M)]
    outside = (N - 1) * 2 + (M - 1) * 2
    inside = 0

    for i in range(1, N - 1):
        for j in range(1, M - 1):
            left = max(grid[i][:j])
            right = max(grid[i][j + 1 :])
            top = max(reversed_grid[j][:i])
            down = max(reversed_grid[j][i + 1 :])

            if grid[i][j] > min(left, right, top, down):
                inside += 1

    total = outside + inside
    print(total)


main()
