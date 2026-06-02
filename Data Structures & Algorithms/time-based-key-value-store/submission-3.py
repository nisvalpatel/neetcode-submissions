class TimeMap:

    def __init__(self):
        self.d = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = [(value, timestamp)]
        else:
            self.d[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:

        def binary_search(key_list: list, timestamp):
            left = 0
            right = len(key_list) - 1
            middle = (left + right) // 2
            res = ""
            while left <= right:
                middle =  (left + right) // 2
                if key_list[middle][1] == timestamp:
                    return key_list[middle][0]
                elif key_list[middle][1] > timestamp:
                    right = middle - 1
                else:
                    left = middle + 1
                if key_list[middle][1] <= timestamp:
                    res = key_list[middle][0]
                

            return res

        if key not in self.d:
            return ""
        
        return binary_search(self.d[key], timestamp)

