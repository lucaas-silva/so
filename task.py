class Task:
    def __init__(self, offset, computation_time, period_time, quantum, period):
        self._offset = offset
        self._computation_time = computation_time
        self._period_time = period_time
        self._quantum = quantum
        self._turnaround_time = 0
        self._computation_time_fix = computation_time
        self._waiting_time = None
        self._period = period

    @property
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, x):
        self._offset = x

    @property
    def computation_time(self):
        return self._computation_time

    @computation_time.setter
    def computation_time(self, x):
        self._computation_time = x

    @property
    def period_time(self):
        return self._period_time

    @property
    def quantum(self):
        return self._quantum

    @property
    def computation_time_fix(self):
        return self._computation_time_fix

    @property
    def turnaround_time(self):
        return self._turnaround_time

    @turnaround_time.setter
    def turnaround_time(self, x):
        self._turnaround_time = x

    @property
    def waiting_time(self):
        return self._waiting_time

    @waiting_time.setter
    def waiting_time(self, x):
        self._waiting_time = x

    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, x):
        self._period = x

    def __str__(self):
        # return f"{self.offset} {self.computation_time_fix} {self.period_time} {self.quantum} {self.turnaround_time} {self._waiting_time}"
        return f"offset: {self.offset}\ncomputation_time: {self.computation_time}\nperiod_time: {self.period_time}\nquantum: {self.quantum}"
