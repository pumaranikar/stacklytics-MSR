__author__ = 'pumarani'

import requests
from requests.exceptions import ConnectionError

try:
    import urlparse
    from urllib import urlencode
except:
    import urllib.parse as urlparse
    from urllib.parse import urlencode

socks4_proxy = "proxy.jf.intel.com"

proxyDict = {
    "socks4": socks4_proxy
}

# def get_contribution(params):
#     url = "http://stackalytics.com/api/1.0/contribution?user_id="
#     request_params = {'start_date': params.start_timestamp,
#                       'end_date': params.end_timestamp}
#     for user in params.user_list:
#         url = url + user + '&' + urlencode(request_params)
#         print url
#         resp = requests.get(url, proxies=proxyDict)
#         if resp.status_code != 200:
#             raise ConnectionError
#         print resp.json()

def get_contribution(params):
    url = "http://stackalytics.com/api/1.0/contribution?user_id="
    request_params = {'start_date': params.start_timestamp,
                      'end_date': params.end_timestamp}
    for user in params.user_list:
        url = url + user + '&' + urlencode(request_params)
        print url
        resp = requests.get(url, proxies=proxyDict)
        if resp.status_code != 200:
            raise ConnectionError
        print resp.json()
