import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
nodes = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

# 오름차순 정렬 1번만
for row in nodes:
    row.sort()

# DFS (stack) - 방문 처리를 pop 시점에!
visited = [0] * (N + 1)
stack = [V]
dfs_out = []

while stack:
    node = stack.pop()
    if visited[node]:
        continue
    visited[node] = 1
    dfs_out.append(str(node))

    # 작은 번호부터 방문하려면 역순으로 push
    for nxt in reversed(nodes[node]):
        if not visited[nxt]:
            stack.append(nxt)

print(" ".join(dfs_out))

# BFS
visited = [0] * (N + 1)
q = deque([V])
visited[V] = 1
bfs_out = []

while q:
    node = q.popleft()
    bfs_out.append(str(node))
    for nxt in nodes[node]:
        if not visited[nxt]:
            visited[nxt] = 1
            q.append(nxt)

print(" ".join(bfs_out))
