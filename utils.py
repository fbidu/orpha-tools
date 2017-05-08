# -*- encoding: utf-8 -*-
from requests import post
from bs4 import BeautifulSoup

def search_orphanet(keyword, search_type='Gen'):
    """
    Returns the HTML of a Orphanet search. By default,
    it searches for a gene
    """
    search_url = "http://www.orpha.net/consor/cgi-bin/Disease_Search_Simple.php?lng=EN"
    search_data = {
            'Disease_Disease_Search_diseaseGroup': keyword,
            'Disease_Disease_Search_diseaseType': search_type
            }

    r = post(search_url, search_data)
    if r.status_code == 200:
        return r.text
    else:
        raise Exception("Search failed with status {}".format(r.status_code))


def get_first_result(orphanet_search):
    """
    Returns the HTML link for the first result of a search
    """
    soup = BeautifulSoup(orphanet_search, 'html.parser')
    first = soup.find_all('div', class_="blockResults")
    if not first:
        return ''
    else:
        return first[0].a.get('href')+"\t"+first[0].a.getText()
