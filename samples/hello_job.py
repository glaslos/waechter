import waechter.scheduler


class HelloJob1(waechter.scheduler.BaseJob):
    def __init__(self, interval=None):
        super(HelloJob1, self).__init__(interval)
        self.interval = interval if interval else 1

    @classmethod
    def work(cls):
        print('hello work 1')


class HelloJob2(waechter.scheduler.BaseJob):
    def __init__(self, interval=None):
        super(HelloJob2, self).__init__(interval)
        self.interval = interval if interval else 2

    @classmethod
    def work(cls):
        print('hello work 2')


if __name__ == '__main__':
    main_worker = waechter.scheduler.JobScheduler().run()
