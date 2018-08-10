##11. Container With Most Water
##Link https://leetcode.com/problems/container-with-most-water/description/

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """


        maxarea = 0

        for i in range(len(height)):
            for j in range(i+1,len(height)):
                maxarea = max(maxarea,min(height[i],height[j]) * (j-i))

        return maxarea
