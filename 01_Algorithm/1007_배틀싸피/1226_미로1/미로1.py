import sys
sys.stdin = open('미로1_input.txt')

for _ in range(10):
    t = int(input())
    maze = [[] for _ in range(16)]
    start = (0, 0)
    check = False

    for i in range(16):
        now = list(map(int, list(input())))
        if 2 in now:
            tmp = now.index(2)
            start = (i, tmp)
        maze[i] = now


    def dfs(x, y):
        global check
        if x < 0 or y < 0 or x >= 16 or y >= 16 or maze[x][y] == 1 or check:
            return

        if maze[x][y] == 3:
            check = True
            return

        if maze[x][y] == 0 or 2:
            maze[x][y] = 1

        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)


    dfs(start[0], start[1])
    print("#" + str(t) + " " + ("1" if check else "0"))

