def solution(tickets):
    tickets.sort()
    visited = [False] * len(tickets)
    result = ["ICN"]

    def dfs(x, count):
        if count == len(tickets):
            return True

        for i in range(len(tickets)):
            start, end = tickets[i]

            if x == start and not visited[i]:
                visited[i] = True
                result.append(end)

                if dfs(end, count + 1):
                    return True

                visited[i] = False
                result.pop()
        return False

    dfs("ICN", 0)
    return result