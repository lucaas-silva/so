from operator import attrgetter

import pandas as pd


class Schedule:
    def __init__(self, simulation_time, scheduler_name, tasks_number, taskList):
        self.simulation_time = simulation_time
        self.scheduler_name = scheduler_name
        self.tasks_number = tasks_number
        self.taskList = taskList

        if self.scheduler_name == "FCFS":
            self.FCFS()
        if self.scheduler_name == "RR":
            self.RR()
        if self.scheduler_name == "RM":
            self.RM()
        if self.scheduler_name == "EDF":
            self.EDF()

    def create_table(self):
        df = pd.DataFrame(self.taskList)
        print(df)

    def print_order(self):
        print("task execution sequence: ")
        for task in self.taskList:
            position = self.taskList.index(task)
            print(f"{task}\nposition: {position}\n" + "-" * 27)

    def utilization(self):
        u = sum([task.computation_time / task.period_time for task in self.taskList])
        return f"{(u) * 100}%"

    def waiting_time(self):
        for task in self.taskList:
            task.waiting_time = task.turnaround_time - task.computation_time
        return sum([task.waiting_time for task in self.taskList]) / len(self.taskList)

    def max_waiting_time(self):
        return max([task.waiting_time for task in self.taskList])

    def min_waiting_time(self):
        return min([task.waiting_time for task in self.taskList])

    def FCFS(self):
        def turnaround_time(self):
            computation_time_total = 0
            for task in self.taskList:
                computation_time_total += task.computation_time
                task.turnaround_time = computation_time_total - task.offset
            return sum([task.turnaround_time for task in self.taskList]) / len(self.taskList)

        def starvation(self):
            res = self.taskList[-1].period_time - self.taskList[-1].turnaround_time
            if res > 0:
                starvation = False
            if res < 0:
                starvation = True
            return starvation

        self.print_order()
        self.utilization()
        turnaround_time(self)
        self.waiting_time()
        self.max_waiting_time()
        self.min_waiting_time()
        starvation(self)
        # self.create_table()

    def RR(self):
        def turnaround_time(self):
            quantum = self.taskList[0].quantum
            time_aux = 0
            tasks = [task for task in self.taskList if task.offset == 0]
            tasks_rest = [task for task in self.taskList if task not in tasks]

            while True:
                all_completed = True
                for task in tasks:
                    if task.computation_time > 0:
                        all_completed = False
                        if task.computation_time > quantum:
                            time_aux += quantum
                            task.computation_time -= quantum
                        else:
                            time_aux += task.computation_time
                            task.computation_time = 0
                            task.turnaround_time = time_aux - task.offset
                        if tasks_rest and tasks_rest[0].offset <= time_aux:
                            if tasks_rest[0].offset <= task._computation_time + quantum:
                                tasks.append(tasks_rest.pop(0))
                            else:
                                tasks.insert(1, tasks_rest.pop(0))
                if all_completed:
                    break

        def average_turnaround_time(self):
            return sum([task.turnaround_time for task in self.taskList]) / len(self.taskList)

        def starvation(self):
            turnaround_max = max([task.turnaround_time for task in self.taskList])
            res = self.taskList[-1].period_time - turnaround_max

            if res > 0:
                starvation = False
            if res < 0:
                starvation = True
            return starvation

        self.print_order()
        self.utilization()
        turnaround_time(self)
        average_turnaround_time(self)
        self.waiting_time()
        self.waiting_time()
        self.max_waiting_time()
        self.min_waiting_time()
        starvation(self)

    def RM(self):
        def schedule_test(self):
            x = sum([task.computation_time / task.period_time for task in self.taskList])
            y = len(self.taskList) * (2 ** (1 / len(self.taskList)) - 1)
            if x <= y:
                return True
            else:
                return False

        def sort_taskList(self):
            self.taskList = sorted(self.taskList, key=attrgetter("_period_time"))
            print(self.taskList)

        def utilization(self):
            return sum([task.computation_time / task.period_time for task in self.taskList])

        def turnaround_time(self):
            time_aux = 0
            t_ant = 0
            original_deadlines = [task.deadline for task in self.taskList]
            print(original_deadlines)
            deadlines = []
            for deadline in original_deadlines:
                deadlines.extend([deadline * i for i in range(1, 6)])
            print(deadlines)
            # deadlines = [task.deadline for task in self.taskList]
            i = 0
            # deadline = deadlines[i]
            for i, task in enumerate(self.taskList):
                while task.computation_time > 0:
                    if deadline != 0:
                        t_ant += self.taskList[deadlines.index(deadline)].computation_time
                        time_aux += t_ant
                    if task.computation_time + t_ant < deadline:
                        time_aux = t_ant + task.computation_time
                        task.turnaround_time = task.computation_time + t_ant
                        task.computation_time = 0
                        t_ant = task.turnaround_time
                    else:
                        task.turnaround_time = deadline
                        task.computation_time -= deadline - t_ant
                        deadline = deadlines[i + 1]

            # for task in self.taskList:
            # task.turnaround_time = self.taskList[-1].period_time

        schedule_test(self)
        sort_taskList(self)
        self.print_order()
        utilization(self)
        turnaround_time(self)
        self.waiting_time()
        self.waiting_time()
        self.max_waiting_time()
        self.min_waiting_time()

    def EDF(self):
        def schedule_test(self):
            x = sum([task.computation_time / task.period_time for task in self.taskList])

            if x <= 1:
                return True
            else:
                return False

        def sort_taskList(self):
            self.taskList = sorted(self.taskList, key=attrgetter("_deadline"))

        def utilization(self):
            return sum([task.computation_time / task.period_time for task in self.taskList])

        schedule_test(self)
        sort_taskList(self)
        self.print_order()
        utilization(self)
        self.waiting_time()
        self.waiting_time()
        self.max_waiting_time()
        self.min_waiting_time()
