class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # prefix 

        prefix_product = 1
        prefix = [0]*len(nums)
        for i in range(len(nums)):
            prefix[i] = prefix_product
            prefix_product *= nums[i]

        print(prefix)


        # suffix
        sufix_product = 1
        suffix= [0]*len(nums)

        for i in range(len(nums)-1,-1,-1):
            
            suffix[i] = sufix_product
            sufix_product *= nums[i]
        print(suffix)
        
        out = [0]*len(nums)
        for i in range(len(nums)):
            out[i] = prefix[i] * suffix[i]
        
        return out

            



            
        