#!/usr/bin/python
# -*- coding: utf-8 -*-

# 我的解法，有次面试考到了
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = []
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        for item in self.store:
            if item[0] == key:
                item[1] = value
                break
        else:
            self.store.append([key, value])


    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        for item in self.store:
            if item[0] == key:
                result = item
                return result[1]
        else:
            return -1
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        for item in self.store:
            if item[0] == key:
                self.store.remove([item[0], item[1]])
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


# 网络上的一种解法

class MyHashMap2:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = []
        self.values = []

    def put(self, key, value):
        """
        value will always be non-negative.
        """
        if key in self.keys:
            self.values[self.keys.index(key)] = value   # Upgrade
        else:
            self.keys.append(key)
            self.values.append(value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.keys:
            return self.values[self.keys.index(key)]
        else:
            return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.keys:
            idx = self.keys.index(key)
            self.keys.pop(idx)
            self.values.pop(idx)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


# 国外的专业解法
class ListNode:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None

class MyHashMap1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 1000;
        self.h = [None]*self.m
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        index = key % self.m
        if self.h[index] == None:
            self.h[index] = ListNode(key, value)
        else:
            cur = self.h[index]
            while True:
                if cur.pair[0] == key:
                    cur.pair = (key, value) #update
                    return
                if cur.next == None: break
                cur = cur.next
            cur.next = ListNode(key, value)
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = key % self.m
        cur = self.h[index]
        while cur:
            if cur.pair[0] == key:
                return cur.pair[1]
            else:
                cur = cur.next
        return -1
            
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        index = key % self.m
        cur = prev = self.h[index]
        if not cur: return
        if cur.pair[0] == key:
            self.h[index] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.pair[0] == key:
                    prev.next = cur.next
                    break
                else:
                    cur, prev = cur.next, prev.next