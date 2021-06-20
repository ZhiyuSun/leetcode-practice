from typing import List
import collections
import string
# 200. 岛屿数量
class Solution200:
    def numIslands(self, grid: List[List[str]]) -> int:
        def _dfs(i, j):
            grid[i][j] = "0"
            for dx, dy in directions:
                n_i, n_j = i + dx, j + dy
                if 0 <= n_i < row and 0 <= n_j < col and grid[n_i][n_j] == "1":
                    _dfs(n_i, n_j)
            
        count = 0
        row, col = len(grid), len(grid[0])
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    count += 1
                    _dfs(i, j)
        return count

    def numIslands1(self, grid: List[List[str]]) -> int:
        def _dfs(i, j):
            visited.add((i, j))
            for m, n in direction:
                if 0 <= i+m < row and 0 <= j+n < col and grid[i+m][j+n] == '1' and (i+m, j+n) not in visited:
                    _dfs(i+m, j+n)

        if not grid or not grid[0]: return 0
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        row, col = len(grid), len(grid[0])
        visited = set()
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and (i, j) not in visited:
                    count += 1
                    _dfs(i, j)
        return count

    def numIslands2(self, grid: List[List[str]]) -> int:
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        row = len(grid)
        col = len(grid[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    count += 1
                    # 采取贪心的原则，这里能置为0就先置为0
                    grid[i][j] = '0'
                    queue = [(i, j)]
                    while queue:
                        a, b = queue.pop(0)
                        for m, n in direction:
                            if 0 <= a+m < row and 0 <= b+n < col and grid[a+m][b+n] == '1':
                                queue.append((a+m, b+n))
                                grid[a+m][b+n] = '0'

        return count

    def numIslands3(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0

        uf = UnionFind(grid)
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        row, col = len(grid), len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    continue
                for d in direction:
                    nr, nc = i+d[0], j+d[1]
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == '1':
                        uf.union(i*col+j, nr*col+nc)

        return uf.count

class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m*n)
        self.rank = [0] * (m*n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.parent[i*n+j] = i*n+j
                    self.count += 1
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            self.parent[rootx] = rooty
            self.count -= 1

# 130. 被围绕的区域
class Solution139:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def _dfs(i, j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] in ['X', '#']: return
            board[i][j] = '#'
            _dfs(i-1, j)
            _dfs(i+1, j)
            _dfs(i, j-1)
            _dfs(i, j+1)

        if not board or not board[0]: return
        m, n = len(board), len(board[0])
        for i in range(0, m):
            for j in range(0, n):
                is_edge = i == 0 or j == 0 or i == m-1 or j == n-1
                if is_edge and board[i][j] == 'O':
                    _dfs(i, j)
        print(board)

        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'
    def solve2(self, board: List[List[str]]) -> None:
        if not board:
            return
        
        n, m = len(board), len(board[0])
        que = collections.deque()
        for i in range(n):
            if board[i][0] == "O":
                que.append((i, 0))
            if board[i][m - 1] == "O":
                que.append((i, m - 1))
        for i in range(m - 1):
            if board[0][i] == "O":
                que.append((0, i))
            if board[n - 1][i] == "O":
                que.append((n - 1, i))
        
        while que:
            x, y = que.popleft()
            board[x][y] = "A"
            for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= mx < n and 0 <= my < m and board[mx][my] == "O":
                    que.append((mx, my))
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

# 127. 单词接龙
class Solution127:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = [(beginWord, 1)]
        while queue:
            word, length = queue.pop(0)

            if word == endWord:
                return length
            
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        queue.append((next_word, length+1))
                        wordList.remove(next_word)
        return 0

    def ladderLength1(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        front = {beginWord}
        back = {endWord}
        dist = 1
        wordList = set(wordList)
        word_len = len(beginWord)
        while front:
            dist += 1
            next_front = set()
            for word in front:
                for i in range(word_len):
                    for c in string.ascii_lowercase:
                        if c != word[i]:
                            new_word = word[:i] + c + word[i+1:]
                            if new_word in back:
                                return dist
                            if new_word in wordList:
                                next_front.add(new_word)
                                wordList.remove(new_word)
            front = next_front
            if len(back) < len(front):
                front, back = back, front
        return 0

# 433. 最小基因变化
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1

        change_map = {
            "A": "CGT",
            "C": "AGT",
            "G": "CAT",
            "T": "CGA",
        }

        min_count = len(bank) + 1

        def dfs(current, count, current_bank):
            nonlocal min_count

            # terminator
            if count > min_count:
                return
            if current == end:
                if count < min_count:
                    min_count = count
                return
            if not current_bank:
                return

            # process
            for i, s in enumerate(current):
                for char in change_map[s]:
                    new = current[:i] + char + current[i + 1:]
                    if new not in current_bank:
                        continue
                    current_bank.remove(new)
                    # drill down
                    dfs(new, count + 1, current_bank)

                    # reverse state
                    current_bank.add(new)

        dfs(start, 0, bank)

        return min_count if min_count <= len(bank) else -1

    def minMutation1(self, start, end, bank):
        queue = [(start, 0)]
        bank = set(bank)
        while queue:
            cur, count = queue.pop(0)
            if cur == end: return count
            for i in range(0, len(start)):
                for ch in ['A', 'C', 'G', 'T']:
                    new = cur[0:i] + ch + cur[i+1:]
                    if new in bank:
                        queue.append((new, count+1))
                        bank.remove(new)
        return -1

    def minMutation2(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        start_set = {start}
        end_set = {end}
        bank = set(bank)
        length = 0
        change_map = {'A': 'TCG', 'T': 'ACG', 'C': 'ATG', 'G': 'ATC'}
        while start_set:
            length += 1
            new_set = set()
            for node in start_set:
                for i, s in enumerate(node):
                    for c in change_map[s]:
                        new = node[:i] + c + node[i + 1:]
                        if new in end_set:
                            return length
                        if new in bank:
                            new_set.add(new)
                            bank.remove(new)
            start_set = new_set
            if len(end_set) < len(start_set):
                start_set, end_set = end_set, start_set
        return -1