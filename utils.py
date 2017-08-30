# -*- encoding: utf-8 -*-
"""
Utilitary functions do download and parse data from Orpha net
"""
from requests import post
from bs4 import BeautifulSoup
from biomart import BiomartServer


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

def convert_refseq_to_gene_symbol(keyword_list):
    """
    Convert Refseq ID to Gene Symbol and description using Biomart
    """
    print("\nConverting Refseq to Gene Symbol\n")
    server = BiomartServer( "http://mar2017.archive.ensembl.org/biomart" )
    #server.verbose = True
    #server.show_databases()
    #server.show_datasets()


    hsapiens = server.datasets['hsapiens_gene_ensembl']
    #hsapiens.show_filters()
    #hsapiens.show_attributes()


    # run a search with custom filters and attributes (no header)
    response = hsapiens.search({
    'filters': {
        'refseq_mrna': keyword_list
    },
    'attributes': [
        'external_gene_name', 'description'
    ]   
    })
    print("\nFinished conversion\n")

    return response
