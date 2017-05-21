# Given an array of integers that is already sorted in ascending order,
# find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that
# they add up to the target, where index1 must be less than index2. Please
# note that your returned answers (both index1 and index2) are not
# zero-based.

# You may assume that each input would have exactly one solution and you may not use the same element twice.

# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2

# two pointer
# O(n) / O(1)
# note, binary search would be O(nlogn)


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # use two pointer
        i = 0
        j = len(numbers) - 1
        while i < j:
            tot = numbers[i] + numbers[j]
            if tot == target:
                return i + 1, j + 1
            elif tot < target:
                i += 1
            else:
                j -= 1

        return


# hash table solution with possible duplicated
# O(n) / O(n)
class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # hash table
        from collections import defaultdict
        dict_map = defaultdict(list)
        for index, i in enumerate(nums):
            dict_map[i].append(index)

        for i in dict_map:
            j = target - i
            if j in dict_map.keys() and i != j:
                return dict_map[i][0], dict_map[target - i][0]
            if j in dict_map.keys() and i == j:
                return dict_map[i][0], dict_map[i][1]
        return
