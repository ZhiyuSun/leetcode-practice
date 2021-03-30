"""
给你一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。

 

示例 1：

输入：intervals = [[0,30],[5,10],[15,20]]
输出：2
示例 2：

输入：intervals = [[7,10],[2,4]]
输出：1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/meeting-rooms-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
import heapq
from typing import List

# 2021.03.04 直奔题解的一天
# 利用最小堆
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key= lambda x: x[0])

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0][1])

        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i[1])

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)

# 时间复杂度：O(NlogN) 。时间开销主要有两部分。第一部分是数组的 排序 过程，消耗 (NlogN) 的时间。数组中有 NN 个元素。
# 接下来是 最小堆 占用的时间。在最坏的情况下，全部 NN 个会议都会互相冲突。在任何情况下，我们都要向堆执行 NN 次插入操作。在最坏的情况下，我们要对堆进行 NN 次查找并删除最小值操作。总的时间复杂度为 (NlogN)，因为查找并删除最小值操作只消耗 O(logN) 的时间。
# 空间复杂度：O(N) 。额外空间用于建立 最小堆 。在最坏的情况下，堆需要容纳全部 NN 个元素。因此空间复杂度为 O(N) 。

# 2021.03.20 磕磕绊绊，总算写出来了
class Solution1:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        arr = [intervals[0][1]]
        heapq.heapify(arr)
        for i in intervals[1:]:
            if i[0] >= arr[0]:
                heapq.heappop(arr)
            heapq.heappush(arr, i[1])
            
        return len(arr)