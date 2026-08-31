class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = nums

    def add(self, val: int) -> int:
        self.stream.append(val)

        sorted_stream = sorted(self.stream)

        return sorted_stream[len(sorted_stream) - self.k]
        
