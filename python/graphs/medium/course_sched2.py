from typing import List


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    adj_list = {i : [] for i in range(numCourses) }
    for courseNum, prereqNum in prerequisites:
        adj_list[courseNum].append(prereqNum)

    visitedCourses, cycle = set(), set()
    result = []

    def explore(courseNum):
        if courseNum in cycle:
            return False
        if courseNum in visitedCourses:
            return True
        cycle.add(courseNum)
        for prereq in adj_list[courseNum]:
            if not explore(prereq):
                return False
        visitedCourses.remove(courseNum)
        visitedCourses.add(courseNum)
        result.append(courseNum)
        return True
    for courseNum in range(numCourses):
        if not explore(courseNum):
            return []
    return result
