import copy 
class TimeMap:

    def __init__(self):
        self.time_map = {}
        self.timestamps = [] 
    def set(self, key: str, value: str, timestamp: int) -> None:
        if timestamp in self.time_map:
            self.time_map[timestamp][key] = value
        else:
            self.time_map[timestamp] = {}
            self.time_map[timestamp][key] = value
            print(self.time_map)
        self.timestamps.append(timestamp) 

    def get(self, key: str, timestamp: int) -> str:
        print(self.time_map)
        if timestamp in self.time_map: 
            return self.time_map[timestamp][key]
        m = -1
        result = -1
        for i in self.timestamps:
            print(timestamp, m , i, key)
            if timestamp-i>0 and (m == -1 or m>abs(i - timestamp)) and key in self.time_map[i]:
                print("a")
                m = abs(i - timestamp)
                result = i
        print(m, i, result)
        if result == -1: return ""
        return self.time_map[result][key]

            
    



