__author__ = 'pumarani'

from datetime import datetime
import time

class Params(object):
    __start_timestamp = 0
    __end_timestamp = 0

    def __init__(self, start_date, end_date, user_list):
        self.start_date = start_date
        self.end_date = end_date
        self.project_user_list = user_list
        self.__start_timestamp = self._get_linux_timestamp(start_date)
        self.__end_timestamp = self._get_linux_timestamp(end_date)

    def _get_linux_timestamp(self, date):
        try:
            dt_start = datetime.strptime(date,'%m/%d/%Y')
            linux_timestamp = (int(time.mktime(dt_start.timetuple())))
            return linux_timestamp
        except ValueError:
            print "Incorrect date format"

    @property
    def start_timestamp(self):
        return self.__start_timestamp

    @property
    def end_timestamp(self):
        return self.__end_timestamp


class ProjectInfo(object):

    def __init__(self, name, user_list=None):
        self.name = name
        self.user_list = user_list
