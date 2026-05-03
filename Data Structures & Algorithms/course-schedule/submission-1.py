class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg = [0] * numCourses
        coursegraph = [[] for _ in range(numCourses)]
        for c, p in prerequisites:
            coursegraph[p].append(c)
            indeg[c] += 1
        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        while len(q) != 0:
            p = q.popleft()
            for c in coursegraph[p]:
                if indeg[c] != 0:
                    indeg[c] -= 1
                    if indeg[c] == 0:
                        q.append(c)
        return sum(indeg) == 0