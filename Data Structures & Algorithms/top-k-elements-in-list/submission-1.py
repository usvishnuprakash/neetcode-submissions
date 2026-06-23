class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for each in nums:

            if each in count:
                count[each] +=1
            else:
                count[each] =1

        # sort

        boxes = [[] for _ in range(len(nums)+1)]

        for num,frequency in count.items():
            boxes[frequency].append(num)

        top_k = []

        for e_b in boxes[len(boxes)-1:0:-1]:

            for num in e_b:
                top_k.append(num)

            if len(top_k) == k:
                return top_k
            

        return [key for key, value in out[:k]]