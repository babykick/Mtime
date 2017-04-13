#coding=utf-8

from datetime import datetime

from conf import TASK_BEAT, TASK_WORKER
from schedulers import Task


def init_task_db():
    # init beat
    task = Task.objects(type='beat')
    task.update_one(set__interval=TASK_BEAT, set__last_run_at=datetime.now())
    worker = Task.objects(type='worker')
    worker.update_one(set__interval=TASK_WORKER, set__last_run_at=datetime.now())


def main():
    init_task_db()


if __name__ == '__main__':
    main()
