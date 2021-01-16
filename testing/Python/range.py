
class Range:
    start = 0
    limit = 0

    def __init__(self, *args):
        if len(args) == 1:
            self.start = min(0, args[0])
            self.limit = max(0, args[0])
        elif len(args) == 2:
            self.start = min(args[0], args[1])
            self.limit = max(args[0], args[1])

    def combine(self, r):
        newStart = self.start if self.start <= r.start else r.start
        newLimit = self.limit if self.limit >= r.limit else r.limit
        return Range(newStart, newLimit)

    def overlaps(self, r) -> bool:
        if self.start >= r.start and self.start < r.limit:
            return True
        elif self.start <= r.start and r.start < self.limit:
            return True
        return False
