from collections import deque


class StackFromQueue:
    # use two queues, cannot use pop() instead use popleft()
    # All operations must be O(1) time complexity
    def __init__(self):
        self.q1 = deque()
        # q2 is used to store the intermediate result
        self.q2 = deque()
    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        result = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return result

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        result = self.q1.popleft()
        self.q2.append(result)
        self.q1, self.q2 = self.q2, self.q1
        return result


    def empty(self) -> bool:
        return len(self.q1) == 0
