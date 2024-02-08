from typing import List


class CourseSchedule:
    def can_finish(self, num_courses: int, prereq: list[list[int]]) -> bool:
        def construct_adjacency_list():
            adj_list = {i : [] for i in range(num_courses)}
            for course_num, prereq_num in prereq:
                adj_list[course_num].append(prereq_num)
            return adj_list

        adj_list = construct_adjacency_list()
        courses_visited = set()

        def explore(course_num):
            if course_num in courses_visited:
                return False
            if len(adj_list[course_num]) == 0:
                return True
            courses_visited.add(course_num)
            for prereq_num in adj_list[course_num]:
                if not explore(prereq_num):
                    return False
            courses_visited.remove(course_num)
            adj_list[course_num] = []
            return True

        for course_num in range(num_courses):
            if not explore(course_num):
                return False
        return True
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # empty prerequisite either means:
        # 1. You can complete this course
        adj_list = {i: [] for i in range(numCourses)}
        for courseNum, prereqNum in prerequisites:
            adj_list[courseNum].append(prereqNum)

        # loop detection
        coursesVisited = set()

        # Explore traverses graphs using DFS starting from courseNum,
        # returns whether courseNum can be completed
        def explore(courseNum):
            isInLoop = courseNum in coursesVisited
            if isInLoop:
                return False
            hasNoPrereq = not len(adj_list[courseNum])
            # there is no prereq
            if hasNoPrereq:
                return True
            # visit current node
            coursesVisited.add(courseNum)
            # iterate through the neighbors
            for prereqNum in adj_list[courseNum]:
                if not explore(prereqNum):
                    return False
            coursesVisited.remove(courseNum)
            # we have asserted that courseNum can be finished, so we could technically have this have no prereq
            adj_list[courseNum] = []
            return True

        # dfs
        for courseNum in range(numCourses):
            if not explore(courseNum):
                return False
        return True
