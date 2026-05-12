import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    numbers = []

    for operation in operations:
        command, number = operation.split()
        number = int(number)

        if command == "I":
            heapq.heappush(min_heap, number)
            heapq.heappush(max_heap, -number)
            numbers.append(number)

        elif command == "D":
            try:
                if number == 1:
                    num = -heapq.heappop(max_heap)
                    min_heap.remove(num)
                    numbers.remove(num)
                    heapq.heapify(min_heap)

                elif number == -1:
                    num = heapq.heappop(min_heap)
                    max_heap.remove(-num)
                    numbers.remove(num)
                    heapq.heapify(max_heap)

            except:
                pass

    if len(numbers) == 0:
        return [0, 0]

    return [max(numbers), min(numbers)]
