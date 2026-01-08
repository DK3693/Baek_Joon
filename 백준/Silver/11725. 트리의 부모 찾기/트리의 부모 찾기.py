import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (N + 1)
parent[1] = -1 

q = deque([1])
while q:
    cur = q.popleft()
    for nxt in graph[cur]:
        if parent[nxt] == 0:     
            parent[nxt] = cur     
            q.append(nxt)

for i in range(2, N + 1):
    print(parent[i])
