from time import sleep

import waechter.scheduler


class HelloJobLock(waechter.scheduler.BaseJob):
    def __init__(self, interval=None):
        super(HelloJobLock, self).__init__(interval)
        self.interval = interval if interval else 1

    @classmethod
    def work(cls):
        print('hello work lock')
        sleep(1.5)


if __name__ == '__main__':
    main_worker = waechter.scheduler.JobScheduler().run()
