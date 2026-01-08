import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
nodes = [tuple(map(int, input().split())) for _ in range(N - 1)]  # nodes 유지

# 각 노드 -> (nodes에서) 자신이 등장하는 간선 인덱스들
adj_edge_idx = [[] for _ in range(N + 1)]
for idx, (a, b) in enumerate(nodes):
    adj_edge_idx[a].append(idx)
    adj_edge_idx[b].append(idx)

parent = [0] * (N + 1)
parent[1] = -1  # 루트

def dfs(cur: int) -> None:
    for eidx in adj_edge_idx[cur]:
        a, b = nodes[eidx]
        nxt = b if a == cur else a  # cur의 반대편 노드
        if parent[nxt] == 0:        # 방문 체크
            parent[nxt] = cur
            dfs(nxt)

dfs(1)

for i in range(2, N + 1):
    print(parent[i])
