class Task:
    def __init__(self, offset, computation_time, period_time):
        self._offset = offset
        self._computation_time = computation_time
        self._period_time = period_time

    @property
    def offset(self):
        return self._offset

    @property
    def computation_time(self):
        return self._computation_time

    @property
    def period_time(self):
        return self._period_time

    def __str__(self):
        return f"offset: {self.offset}\ncomputation_time: {self.computation_time}\nperiod_time: {self.period_time}"
