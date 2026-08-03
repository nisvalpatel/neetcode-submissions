class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = defaultdict(int)
        count_to_num = defaultdict(set)

        for num in nums:
            if num_to_count[num] == 0:
                count_to_num[1].add(num)
                num_to_count[num] += 1
                continue

            temp = num_to_count[num]
            count_to_num[temp].remove(num)
            count_to_num[temp + 1].add(num)
            num_to_count[num] += 1

        count = 0
        res = []
        for key in sorted(count_to_num, reverse=True):
            for num in count_to_num[key]:
                if count == k:
                    return res
                res.append(num)
                count += 1
                
        return res
            




