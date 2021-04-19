"""
有 n 个城市，按从 0 到 n-1 编号。给你一个边数组 edges，其中 edges[i] = [fromi, toi, weighti] 代表 fromi 和 toi 两个城市之间的双向加权边，距离阈值是一个整数 distanceThreshold。

返回能通过某些路径到达其他城市数目最少、且路径距离 最大 为 distanceThreshold 的城市。如果有多个这样的城市，则返回编号最大的城市。

注意，连接城市 i 和 j 的路径的距离等于沿该路径的所有边的权重之和。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

# 2021.04.19 floyd插点法
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dis=[[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):dis[i][i]=0
        for i,j,w in edges:
            dis[i][j]=w
            dis[j][i]=w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j])
        res,count=0,n+1
        for i in range(n):
            cur=0
            for j in range(n):
                if dis[i][j]<=distanceThreshold:
                    cur+=1
            if cur<=count:
                res,count=i,cur
        return res

