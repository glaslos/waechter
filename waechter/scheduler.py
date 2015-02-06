import gevent.monkey
gevent.monkey.patch_all(thread=False)

import gevent


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
