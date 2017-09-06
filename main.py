# -*- encoding: utf-8 -*-
"""
The main module
"""
import argparse
import utils
from lxml import etree


def main():

    d = {}
    ap = argparse.ArgumentParser()
    ap.add_argument('--input')
    ap.add_argument('--xml')
    ap.add_argument('--output')
    args = ap.parse_args()

    #gene_symbol_list = ()
    tree = etree.parse(args.xml)
    symbols = tree.findall('//Symbol')
    for gene in symbols:
        d[gene.text] = [gene.getparent().getparent().getparent().getparent().find("OrphaNumber").text, gene.getparent().getparent().getparent().getparent().find("Name").text]


    lines_list = open(args.input).read().splitlines()
    output = open(args.output, 'w')
    k=0
    i=0
    while i <= len(lines_list):
        uplimit = i+200
        if uplimit > len(lines_list):
            uplimit = len(lines_list)
    	
        tmp_list = lines_list[i:uplimit]
        gene_symbol_list = utils.convert_refseq_to_gene_symbol(tmp_list)
#    	gene_symbol_list = gene_symbol_list + tmp_gene_symbol_list
        i=i+200
        print(str(i))
        for line in gene_symbol_list.iter_lines():
            line = line.decode('utf-8')
            gene = line.split("\t")[0]
            description = line.split("\t")[1]

            if gene in d:
            	output.write(gene+"\t"+description+"\t"+d[gene][0]+"\t"+d[gene][1]+"\n")

#            html_text=utils.search_orphanet(gene)
#            result=utils.get_first_result(html_text)
#            if result != '':
#            	teste=''.join([linha.strip() for linha in result.strip().splitlines()])
#            	print(gene+"\t"+description+"\thttp://www.orpha.net/consor/cgi-bin/"+teste)

    #        html_text=utils.search_orphanet(gene)
#            result=utils.get_first_result(html_text)
#            if result != '':
#                teste=''.join([linha.strip() for linha in result.strip().splitlines()])
#                print(gene+"\thttp://www.orpha.net/consor/cgi-bin/"+teste)

if __name__ == '__main__':
    main()
