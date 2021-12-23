import requests
import re
import json
def get_all_links(url):
# get url
    # url = input('Enter a URL (include `http://`): ')

# connect to the url
    website = requests.get(url)

# read html
    html = website.text

# use re.findall to grab all the links
    links = re.findall('"((http|ftp)s?://.*?)"', html)

# output links
    resp = {'links':[]}
    for link in links:
        resp['links'].append(link[0])
    # print("response dict : ",resp)
    # print("resp : ",resp)
    return resp
    