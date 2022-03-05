from fastapi import FastAPI
from TaskModel import TaskModel
from SchedulingModel import SchedulingModel
import fcfs

app = FastAPI()


@app.get("/fcfs/")
async def root():
    return {"name": "First Come First Serve"}


# TODO: Add log statements to the response for remarks which displays input, avg time etc,.
@app.get("/fcfs/schedule/", response_model=SchedulingModel)
async def schedule(tasks: list[TaskModel]):
    executionTimeArray = []
    arrivalTimeArray = []
    periodArray = []
    tasks.sort(key=lambda x: x.executionTime)
    for task in tasks:
        executionTimeArray.append(task.executionTime)
        periodArray.append(task.period)
        arrivalTimeArray.append(task.arrivalTime)
    schedulingModel = fcfs.schedule(tasks, executionTimeArray, periodArray, arrivalTimeArray)
    return schedulingModel
