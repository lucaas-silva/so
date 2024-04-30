class Schedule:
    def __init__(self, simulation_time, scheduler_name, tasks_number, taskList):
        self.simulation_time = simulation_time
        self.scheduler_name = scheduler_name
        self.tasks_number = tasks_number
        self.taskList = taskList

        if self.scheduler_name == "FCFS":
            self.FCFS()

    def FCFS(self):
        def print_order(self):
            print("task execution sequence: ")
            position = 0
            for task in self.taskList:
                print(f"{task}\nposition: {position}")
                print("-" * 27)
                position += 1

        def print_utilization(self):
            u = 0
            for task in self.taskList:
                u += task.computation_time / task.period_time

            print(f"system usage level: {(u) * 100}%")

        def print_turnaround_time(self):
            print("turnaround time: ")
            cp, cp_total, of, tf = 0, 0, 0, 0

            for task in self.taskList:
                cp += task.computation_time
                cp_total += cp
                of += task.offset

                print(f"task {tf}: {cp - task.offset}")
                tf += 1

            print(f"avarege turnaround time: {(cp_total - of)/self.tasks_number}")

        def waiting_time(self):
            """
            waiting_time = turnaround_time - computation_time
            """
            pass

        print_order(self)
        print_utilization(self)
        print_turnaround_time(self)
        print_waiting_time(self)
