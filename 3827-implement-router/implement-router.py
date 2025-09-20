import bisect
from collections import deque, defaultdict

class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.packet_queue = deque()
        self.in_storage = set()
        self.dest_lists = defaultdict(list)
        self.dest_start = defaultdict(int)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.in_storage:
            return False
        self.packet_queue.append(packet)
        self.in_storage.add(packet)
        self.dest_lists[destination].append(timestamp)
        if len(self.packet_queue) > self.memoryLimit:
            s, d, t = self.packet_queue.popleft()
            self.in_storage.remove((s, d, t))
            self.dest_start[d] += 1
        return True

    def forwardPacket(self) -> []:
        if not self.packet_queue:
            return []
        s, d, t = self.packet_queue.popleft()
        self.in_storage.remove((s, d, t))
        self.dest_start[d] += 1
        return [s, d, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        lst = self.dest_lists[destination]
        left = self.dest_start[destination]
        lo = bisect.bisect_left(lst, startTime, left)
        hi = bisect.bisect_right(lst, endTime, left)
        return hi - lo