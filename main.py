import json

from schedule import Schedule
from task import Task

if __name__ == "__main__":
    with open("RM.json", "r") as file:
        file_contents = json.load(file)

    simulation_time = file_contents["simulation_time"]
    scheduler_name = file_contents["scheduler_name"].upper()
    tasks_number = file_contents["tasks_number"]
    tasks = file_contents["tasks"]

    taskList = []

    for i in range(tasks_number):
        offset = tasks[i]["offset"]
        computation_time = tasks[i]["computation_time"]
        period_time = tasks[i]["period_time"]
        quantum = tasks[i]["quantum"]
        deadline = tasks[i]["deadline"]

        temp = Task(offset, computation_time, period_time, quantum, deadline)
        taskList.append(temp)

    Schedule(simulation_time, scheduler_name, tasks_number, taskList)
