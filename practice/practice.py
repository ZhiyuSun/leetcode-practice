#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def find_next_node(self, current_position, step):
        master = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
        21,22,23,24,25,31,32,33,1]
        branch = [26,27,28,29,30]

        if current_position == 19 and step > 0:
            return branch[step-1]
        
        if current_position == 25 and step < 0:
            return branch[step+5]

        if 26 <= current_position <= 30:
            if 0 <= branch.index(current_position)+step <= 4:
                return branch[branch.index(current_position)+step]
            else:
                return master[19+branch.index(current_position)+step]

        return master[(master.index(current_position) + step) % 28]

solution = Solution()
print solution.find_next_node(1,4)
print solution.find_next_node(5, -4) # 1 
print solution.find_next_node(17, 5) # 22 
print solution.find_next_node(19, 2) # 27 
print solution.find_next_node(27, -3) # 18 
print solution.find_next_node(30, 3) # 32 
print solution.find_next_node(32, -4) # 23 
print solution.find_next_node(25, -2) # 29 
print solution.find_next_node(33, 3) # 3 
print solution.find_next_node(1, -2) # 32