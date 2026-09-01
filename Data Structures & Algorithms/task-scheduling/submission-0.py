class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        time = 0

        count = {}

        for task in tasks:
            count[task] = count.get(task, 0) + 1

        max_heap = [(-freq, task) for task, freq in count.items()]
        heapq.heapify(max_heap)

        queue = deque()

        while max_heap or queue:

            time += 1

            if max_heap:
                freq, task = heapq.heappop(max_heap)

                # Use task once
                freq += 1

                # Still tasks remaining
                if freq != 0:
                    queue.append((freq, task, time + n))

            # Task has finished cooling down
            if queue and queue[0][2] == time:
                freq, task, available_time = queue.popleft()
                heapq.heappush(max_heap, (freq, task))

        return time


            