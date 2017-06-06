"""
combination sum

input:
[2, 3, 6, 7, -1], 7

output
[7],
[2, 2, 3]
"""

# how is this dfs???


class Solution(object):
    def combinationSum(self, cand, target):
        res = []
        cand.sort()
        self.dfs(cand, target, 0, [], res)
        return res

    def dfs(self, cand, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return
        for i in list(range(index, len(cand))):
            # same list, new target, i is i, then allow repeat
            self.dfs(cand, target - cand[i], i, path + [cand[i]], res)


# other relatd code
