# Example of backtracking pattern to solve problems such as: find all subsets, permutations, combinations, etc.

from typing import List

# ref: https://leetcode.com/problems/combinations/solutions/844096/backtracking-cheatsheet-simple-solution/?orderBy=most_votes&languageTags=python

# Template:

class BacktrackingTemplate():
  def __init__(self, data):
    self.data = data
    self.result = []

  def subsets(self, nums: List[int]) -> List[List[int]]:
    res, path = [], []
    self.dfs(0, res, path, nums)
    return res

  def dfs(self, index, res, path, nums):
    res.append(list(path))
    for i in range(index, len(nums)):
      path.append(nums[i])
      self.dfs(i+1, res, path, nums)
      path.pop()