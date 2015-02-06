from redis import StrictRedis

import waechter.scheduler
import waechter.utils


class QueueGauges(waechter.scheduler.BaseJob):
    def __init__(self):
        self.redis = StrictRedis(host='incoming-rq.internal.norman-aws.com', port=6379, db=0)

    def work(self):
        data = {
            "wait_incoming": self.redis.llen('rq:queue:incoming'),
            "wait_router": self.redis.llen('rq:queue:router'),
            "wait_mag2": self.redis.llen('rq:queue:mag2'),
            "wait_failed": self.redis.llen('rq:queue:failed'),
        }
        waechter.utils.report_data(data, 'CHANGEME!')


if __name__ == '__main__':
    main_worker = waechter.scheduler.JobScheduler.scheduler()
