
class TimeAverager:
    n: int = 5
    avg: float = 5.0

    def __init__(self):
        pass

    def update(self, time):
        older_time = self.avg
        older_time = (self.n - 1) * older_time / self.n
        self.avg = older_time + time / self.n


    def get_average(self):
        return self.avg