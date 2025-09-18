import bisect

class TaskManager:
    def __init__(self, tasks):
        self.a = {}
        self.b = []

        for userId, taskId, priority in tasks:
            self.a[taskId] = (userId, priority)
            bisect.insort(self.b, (priority, taskId))

    def add(self, userId, taskId, priority):
        self.a[taskId] = (userId, priority)
        bisect.insort(self.b, (priority, taskId))

    def edit(self, taskId, newPriority):
        userId, oldPriority = self.a[taskId]
        idx = bisect.bisect_left(self.b, (oldPriority, taskId))
        self.b.pop(idx)
        self.a[taskId] = (userId, newPriority)
        bisect.insort(self.b, (newPriority, taskId))

    def rmv(self, taskId):
        userId, priority = self.a[taskId]
        idx = bisect.bisect_left(self.b, (priority, taskId))
        self.b.pop(idx)
        del self.a[taskId]

    def execTop(self):
        if not self.a:
            return -1
        priority, taskId = self.b.pop()
        userId, _ = self.a[taskId]
        del self.a[taskId]
        return userId