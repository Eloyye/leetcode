from typing import List


def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    # empty prerequisite either means:
    # 1. You can complete this course
    adj_list = {i : [] for i in range(numCourses)}
    for courseNum, prereqNum in prerequisites:
        adj_list[courseNum].append(prereqNum)

    #loop detection
    coursesVisited = set()

    # Explore traverses graphs using DFS starting from courseNum,
    # returns whether courseNum can be completed
    def explore(courseNum):
        isInLoop = courseNum in coursesVisited
        if isInLoop:
            return False
        hasNoPrereq = not len(adj_list[courseNum])
        #there is no prereq
        if hasNoPrereq:
            return True
        #visit current node
        coursesVisited.add(courseNum)
        #iterate through the neighbors
        for prereqNum in adj_list[courseNum]:
            if not explore(prereqNum):
                return False
        coursesVisited.remove(courseNum)
        #we have asserted that courseNum can be finished, so we could technically have this have no prereq
        adj_list[courseNum] = []
        return True


    #dfs
    for courseNum in range(numCourses):
        if not explore(courseNum):
            return False
    return True

