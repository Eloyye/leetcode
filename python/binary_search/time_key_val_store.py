#Design a time-based key-value data structure that can store multiple values for the same key
# at different time stamps and retrieve the key's value at a certain timestamp.
class TimeMap:
    def __init__(self):
        self.store = {} #hashmap {key: list[val, timestamp]
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, []) #get the list of values containing value and timestamp
        #binary search
        left, right = 0, len(values) - 1
        while right >= left:
            mid = left + (right - left) // 2
            if values[mid][1] <= timestamp:
                #we do this so we get a timestamp that is the latest timestamp
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        res = values[-1][0] if values else res
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)