import requests
import re

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
    resp = []
    for link in links:
        resp.append(link[0])
    return resp
    