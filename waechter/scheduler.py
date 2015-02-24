import gevent.monkey
gevent.monkey.patch_all(thread=False)

import sys

import gevent


class BaseJob(object):
    def __init__(self, interval=5):
        self.interval = interval


class JobScheduler(object):

    def __init__(self):
        # initialize all the jobs
        self.job_instances = [job() for job in BaseJob.__subclasses__()]

    @classmethod
    def job_spawner(cls, job_instance):
        pid = gevent.fork()
        if pid == 0:
            # child
            gevent.spawn(job_instance.work).join()
            # exit the whole fork
            sys.exit(0)

    def run(self):
        jobs_dict = dict()
        for job_instance in self.job_instances:
            # interval can't be smaller than 1s
            assert (isinstance(job_instance.interval, int))
            # interval can't be smaller than 1
            assert (job_instance.interval >= 1)
            jobs_dict[job_instance.interval] = job_instance
        max_interval = max(jobs_dict.keys())
        sleep_count = 0
        while True:
            try:
                gevent.sleep(1)
                sleep_count += 1
                for interval, job in jobs_dict.items():
                    # spawn all jobs that match the current interval
                    if sleep_count % interval == 0:
                        self.job_spawner(job)
                # reset the sleep counter (to infinity!)
                if sleep_count > 0 and sleep_count % max_interval == 0:
                    sleep_count = 0
            except KeyboardInterrupt:
                print 'bye'
                break


if __name__ == '__main__':
    scheduler = JobScheduler()
    scheduler.run()
