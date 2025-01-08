class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num in nums1:
            print(num)
            index = nums2.index(num)
            stack = []
            for i in range(index, len(nums2)):
                found  = False
                if nums2[i] > num:
                    found = True
                    res.append(nums2[i])
                    break
            if not found:
                res.append(-1)
            
                
        return res
                
        