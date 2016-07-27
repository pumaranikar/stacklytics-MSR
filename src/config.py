import ConfigParser
from objects.params import Params

config_path = "../msr-config.ini"

class ConfigureMSR(object):

    SECTION_PROJECT = "projects"
    SECTION_USERS = "-users"
    SECTION_DATES = "dates"

    SECTION_ALL = [SECTION_PROJECT, SECTION_USERS, SECTION_USERS]

    def __init__(self):
        self.cfg_parser = ConfigParser.ConfigParser(allow_no_value=True)
        self.read_file(file_path=config_path)

    def read_file(self, file_path=config_path):

        self.cfg_parser.read(file_path)
        sections = self.cfg_parser.sections()

        project_users = {}

        for section in sections:
            if section == ConfigureMSR.SECTION_PROJECT:
                project_list = self.cfg_parser.options(section)

        for project in project_list:
            if (project+ConfigureMSR.SECTION_USERS) in sections:
                user_list = self.cfg_parser.options(project+ConfigureMSR.SECTION_USERS)
                project_users.update({project:user_list})

        if ConfigureMSR.SECTION_DATES in sections:
            start_date = self.cfg_parser.get(ConfigureMSR.SECTION_DATES, "start_date")
            end_date = self.cfg_parser.get(ConfigureMSR.SECTION_DATES, "end_date")

        params = Params(start_date, end_date, project_users)
        return params