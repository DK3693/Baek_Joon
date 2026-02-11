import sys
input = sys.stdin.readline

N = int(input())
graph = []
visited = [[False] * N for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int, input().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    count = 1   

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                count += dfs(nx, ny)
    return count

num = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            num.append(dfs(i, j))
print(len(num))
for i in sorted(num):
    print(i)

