# https://leetcode.com/problems/palindrome-partitioning/
from typying import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
    	l = list(s)
    	ans = [l]
    	n = len(l)
    	for i in range(n):
    		sub_s = s[i]
    		for j in range(i+1, n):
    			sub_s += s[j]
    			if sub_s == sub_s[::-1]:
    				ans.append(sub_s)