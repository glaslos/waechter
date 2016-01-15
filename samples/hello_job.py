# Waechter - Job Scheduling Helper
# Copyright (C) 2016  Lukas Rist

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
    main_worker = waechter.scheduler.JobScheduler().run()
