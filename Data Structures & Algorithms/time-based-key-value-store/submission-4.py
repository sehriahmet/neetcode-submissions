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
        self.timestamps.append(timestamp) 

    def get(self, key: str, timestamp: int) -> str:
        if timestamp in self.time_map: 
            return self.time_map[timestamp][key]
        m = -1
        result = -1
        for i in self.timestamps:
            if timestamp-i>0 and (m == -1 or m>abs(i - timestamp)) and key in self.time_map[i]:
                m = abs(i - timestamp)
                result = i
        if result == -1: return ""
        return self.time_map[result][key]

            
    



