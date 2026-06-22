class Metrics:
    def __init__(self):
        self.metrics = {}

    def increment(self, metric: str) -> None:
        if metric in self.metrics:
            self.metrics[metric] += 1
        else:
            self.metrics[metric] = 1

    def get(self, metric: str) -> int:
        return self.metrics.get(metric, 0)
