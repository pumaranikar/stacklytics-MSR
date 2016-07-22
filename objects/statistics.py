__author__ = 'pumarani'

from marks import Marks as marks

class Statistics(object):

    def __init__(self):
        self.email_count = 0
        self.commit_count = 0
        self.filed_bugs = 0
        self.patch_sets = 0
        self.draft_blueprints = 0
        self.completed_blueprints = 0
        self.resolved_bugs = 0
        self.marks = marks()

    def get_statistics(self):
        self.__dict__