class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        outs =[]
        for i in range(n):

            if i != 0 and nums[i-1] == nums[i]:
                continue


            # 2 sum 

            left = i+1
            right =n - 1

            while left < right :

                current_sum = nums[left] + nums[right]

                target = - nums[i]
                if  current_sum == target :
                    outs.append([nums[i],nums[left],nums[right]])
                    right -=1
                    left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right-=1

                    while left < right and nums[left] == nums[left-1]:
                        left +=1

                elif current_sum > target:
                    right-=1

                    while left < right  and nums[right] == nums[right+1]:
                        right-=1

                elif current_sum <  target:
                    left +=1
                
                    while left < right and nums[left] == nums[left-1]:
                        left +=1
                    
        print(outs)
        return outs






        