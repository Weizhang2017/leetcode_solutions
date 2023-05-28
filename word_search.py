# https://leetcode.com/problems/word-search/

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        col = len(board[0])
        self.ans = False
        self.traversed = []
        for i in range(rows):
            for j in range(col):
                self.search(board, i, j, word, 0)
        return self.ans

    ans = False
    traversed = []
    def search(self, board, i, j, word, l):
        print(board[i][j], word[l])
        self.traversed.append((i,j))
        print(i, j, self.traversed)
        if board[i][j] == word[l]:
            if l < len(word)-1:
                coordinates = [(i - 1, j), (i + 1 , j), (i , j - 1), (i , j + 1)]
                for k, n in  coordinates:
                    if len(board) > k >= 0 and len(board[0]) > n >=0 and (k, n) not in self.traversed:
                        # print(k, n)
                        
                        if self.search(board, k, n, word, l+1):
                            # print(k, n)
                            self.ans = True
                            return True
                        else:
                            continue
            else:
                self.ans = True
                return True
        else:
            self.traversed.pop()
            return self.ans


if __name__ == '__main__':
    s = Solution()
    board = [["C","A","A"],["A","A","A"],["B","C","D"]]
    word = "AAB"
    print(s.exist(board, word))