import waechter.scheduler


class HelloJob1(waechter.scheduler.BaseJob):
    def __init__(self, interval=None):
        super(HelloJob1, self).__init__(interval)
        self.interval = interval if interval else 1

    @classmethod
    def work(cls):
        print('hello work 1')


class HelloJob21(waechter.scheduler.BaseJob):
    def __init__(self, interval=None):
        super(HelloJob21, self).__init__(interval)
        self.interval = interval if interval else 2

    @classmethod
    def work(cls):
        print('hello work 21')


class HelloJob22(waechter.scheduler.BaseJob):
    def __init__(self, interval=None):
        super(HelloJob22, self).__init__(interval)
        self.interval = interval if interval else 2

    @classmethod
    def work(cls):
        print('hello work 22')


if __name__ == '__main__':
    main_worker = waechter.scheduler.JobScheduler().run_once()
