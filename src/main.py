__author__ = 'pumarani'

from objects.params import Params
import utils as utils
import config

def main():
    params = config.ConfigureMSR()

    if params is None:
        print "Invalid input: check .ini file."
        return

    get_stats(params)
    # lines = readfile()
    # start_date = lines[0]
    # end_date = lines[1]
    # user_list = lines[2:]
    # params = Params(start_date, end_date, user_list)
    # print "start date ", params.start_timestamp
    # print "end date ", params.end_timestamp
    # get_stats(params)
    pass

def get_stats(params):
    utils.get_contribution(params)

def readfile():
    lines = [line.rstrip('\n') for line in open('../info.txt')]
    return lines

if __name__ == "__main__":
    main()
