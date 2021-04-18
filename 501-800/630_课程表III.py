"""
这里有 n 门不同的在线课程，他们按从 1 到 n 编号。每一门课程有一定的持续上课时间（课程时间）t 以及关闭时间第 d 天。一门课要持续学习 t 天直到第 d 天时要完成，你将会从第 1 天开始。

给出 n 个在线课程用 (t, d) 对表示。你的任务是找出最多可以修几门课。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/course-schedule-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

# 2021.04.18 是我看不懂的解法
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:  # 大根堆
    #（1）按照结束时间对课程进行排序
    #（2）使用一个大顶堆来储存已经选择的课程的长度
    #（3）一旦发现安排了当前课程之后，其结束时间超过了最晚结束时间，那么就从已经安排的课程中，取消掉一门最耗时的课程


        import heapq
        courses = sorted(courses, key = lambda x: x[1])
        d = 0
        heap = []
        for course in courses:
            d += course[0]
            heapq.heappush(heap, -course[0])
            if d > course[1]:
                d += heapq.heappop(heap)
        return len(heap)
