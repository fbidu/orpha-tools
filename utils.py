# -*- encoding: utf-8 -*-
"""
Utilitary functions do download and parse data from Orpha net
"""
from requests import post
from bs4 import BeautifulSoup


def search_orphanet(keyword, search_type='Gen'):
    """
    Returns the HTML of a Orphanet search. By default,
    it searches for a gene
    """
    search_url = r"http://www.orpha.net/consor/cgi-bin/Disease_Search_Simple.php?lng=EN"
    search_data = {
            'Disease_Disease_Search_diseaseGroup': keyword,
            'Disease_Disease_Search_diseaseType': search_type
            }

    request = post(search_url, search_data)
    if request.status_code == 200:
        return request.text
    else:
        raise Exception("Search failed with status {}".format(request.status_code))


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
