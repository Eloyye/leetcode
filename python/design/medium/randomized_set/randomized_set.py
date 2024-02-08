from random import randint


class RandomizedSet:

    def __init__(self):

        self.value_to_indices = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.value_to_indices:
            return False
        self.value_to_indices[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        #
        if val not in self.value_to_indices:
            return False
        temp_target, temp_end = self.values[self.value_to_indices[val]], self.values[len(self.values) - 1]
        self.values[self.value_to_indices[val]], self.values[len(self.values) - 1] = self.values[
            len(self.values) - 1], val
        self.value_to_indices[temp_end] = self.value_to_indices[temp_target]
        # in python, a pop operation is constant time O(1)
        self.values.pop()
        del self.value_to_indices[temp_target]
        return True

    def getRandom(self) -> int:
        return self.values[randint(0, len(self.values) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
