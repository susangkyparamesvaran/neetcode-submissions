class TimeMap:

    def __init__(self):
        self.hash_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hash_map:
            self.hash_map[key].append((timestamp, value))
        else:
            self.hash_map[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if (key not in self.hash_map):
            return ""
        
        sorted_list = self.hash_map[key]
        

        start = 0
        end = len(sorted_list) - 1
        lar_val = ""

        while (start <= end):
            midpoint = (start + end) // 2

            if (sorted_list[midpoint][0] <= timestamp):
                lar_val = sorted_list[midpoint][1]
                start = midpoint + 1
            else:
                end = midpoint - 1
            

        return lar_val