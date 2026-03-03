import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    scores = []
    
    for _ in range(N):
        scores.append(list(map(int, input().split())))
    
    scores.sort(key=lambda x: x[0])
    lowest = scores[0][1]
    count = 1
    for paper, interview in scores:
        if interview < lowest:
            count += 1
            lowest = interview
        else:
            continue
    print(count)
