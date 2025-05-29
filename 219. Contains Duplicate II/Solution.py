class Solution:
    def containsNearbyDuplicate(self,nums,k):
        # Solution 1
        con_dup = {}
        for i,num in enumerate(nums):
            if num in con_dup and i - con_dup[num] <= k:
                return True
            con_dup[num] = i
        return False
        



nums , k= list(map(int,input().split())) , int(input())
obj = Solution()
print(obj.containsNearbyDuplicate(nums,k))