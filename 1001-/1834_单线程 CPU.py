"""
给你一个二维数组 tasks ，用于表示 n​​​​​​ 项从 0 到 n - 1 编号的任务。其中 tasks[i] = [enqueueTimei, processingTimei] 意味着第 i​​​​​​​​​​ 项任务将会于 enqueueTimei 时进入任务队列，需要 processingTimei 的时长完成执行。

现有一个单线程 CPU ，同一时间只能执行 最多一项 任务，该 CPU 将会按照下述方式运行：

如果 CPU 空闲，且任务队列中没有需要执行的任务，则 CPU 保持空闲状态。
如果 CPU 空闲，但任务队列中有需要执行的任务，则 CPU 将会选择 执行时间最短 的任务开始执行。如果多个任务具有同样的最短执行时间，则选择下标最小的任务开始执行。
一旦某项任务开始执行，CPU 在 执行完整个任务 前都不会停止。
CPU 可以在完成一项任务后，立即开始执行一项新任务。
返回 CPU 处理任务的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-threaded-cpu
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
import heapq

# 2021.07.07 完全看不懂，直奔题解
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        indices = list(range(n))
        indices.sort(key=lambda x: tasks[x][0])

        ans = list()
        # 优先队列
        q = list()
        # 时间戳
        timestamp = 0
        # 数组上遍历的指针
        ptr = 0
        
        for i in range(n):
            # 如果没有可以执行的任务，直接快进
            if not q:
                timestamp = max(timestamp, tasks[indices[ptr]][0])
            # 将所有小于等于时间戳的任务放入优先队列
            while ptr < n and tasks[indices[ptr]][0] <= timestamp:
                heapq.heappush(q, (tasks[indices[ptr]][1], indices[ptr]))
                ptr += 1
            # 选择处理时间最小的任务
            process, index = heapq.heappop(q)
            timestamp += process
            ans.append(index)
        
        return ans
