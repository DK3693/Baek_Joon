from collections import deque
import sys

input = sys.stdin.readline
T = int(input().strip())
for _ in range (T):
    check = 1
    p = input().strip()
    n = int(input().strip())
    nums = input().strip()
    nums = nums[1:-1]

    if nums == "":
        nums = deque()
    else:
        nums = deque(nums.split(','))

    try:  
        for i in p:
            if i == 'R':
                check += 1
            elif i == 'D':
                if check % 2 == 1:
                    nums.popleft()
                else:
                    nums.pop()
    except:
        print("error")
        continue
    if check % 2 == 1:
        print("[" + ",".join(nums) + "]")
    else:
        nums.reverse()
        print("[" + ",".join(nums) + "]")