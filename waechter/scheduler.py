import gevent.monkey
gevent.monkey.patch_all(thread=False)

import json

import gevent
import requests

from pprint import pprint


def report_data(data_points):
    stats = list()
    for key, value in data_points.items():
        stats.append([key, value])
    data = {
        "name": "asgard.queue.gauges",
        "columns": ["queue_name", "value"],
        "points": stats
    }
    pprint(data)
    requests.post('http://172.17.2.33:8086/db/asgarddb/series?u=root&p=root', data=json.dumps([data, ]))


class BaseJob(object):
    pass


class JobScheduler(object):
    @classmethod
    def scheduler(cls, interval=60):
        while True:
            try:
                gevent.sleep(interval)
            except KeyboardInterrupt:
                break
            # We fork here to minimize the scheduler drift
            pid = gevent.fork()
            if pid == 0:
                # child
                job_workers = list()
                for JobClass in BaseJob.__subclasses__():
                    job_workers.append(gevent.spawn(JobClass().work))
                gevent.joinall(job_workers)
                break


if __name__ == '__main__':
    main_worker = gevent.spawn(JobScheduler.scheduler)
    try:
        main_worker.join()
    except KeyboardInterrupt:
        print 'bye'
