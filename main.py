# -*- encoding: utf-8 -*-
"""
The main module
"""
import argparse
import utils
from lxml import etree


def main():

    d = {}
    f = {}
    g = {}
    biogrid_hash = {}
    ap = argparse.ArgumentParser()
    ap.add_argument('--input')
    ap.add_argument('--xml')
    ap.add_argument('--p2y')
    ap.add_argument('--biogrid')
    ap.add_argument('--output')
    args = ap.parse_args()

    #gene_symbol_list = ()
    tree = etree.parse(args.xml)
    symbols = tree.findall('//Symbol')
    for gene in symbols:
        d[gene.text] = [gene.getparent().getparent().getparent().getparent().find("OrphaNumber").text, gene.getparent().getparent().getparent().getparent().find("Name").text]


    lines_list = open(args.input).read().splitlines()
    output = open(args.output, 'w')
    i=0

    p2y_list = open(args.p2y).read().splitlines()

    for l in p2y_list:
        lines = l.split(",")
        f[lines[10]] = lines[11]
        g[lines[11]] = lines[10]

    biogrid_file = open(args.biogrid).read().splitlines()

    for l in biogrid_file:
        lines = l.split("\t")
        biogrid_hash[lines[1]+"-"+lines[2]] = lines[0]
        biogrid_hash[lines[1]+"-"+lines[1]] = lines[0]

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
            entrez = line.split("\t")[2]

            if entrez in f:
            	entrez_bait = f[entrez]
            elif entrez in g:
            	entrez_bait = g[entrez]

            gene_symbol_list = utils.convert_refseq_to_gene_symbol(entrez_bait)
            
            for line in gene_symbol_list.iter_lines():
                line = line.decode('utf-8')
                gene_bait = line.split("\t")[0]
                description_bait = line.split("\t")[1]
                entrez_bait = line.split("\t")[2]

            if gene in d:
            	if entrez+"-"+entrez_bait in biogrid_hash or entrez_bait+"-"+entrez in biogrid_hash:
            		bio = biogrid_hash[entrez+"-"+entrez_bait]+biogrid_hash[entrez_bait+"-"+entrez]
            	else:
            		bio = ""
            	output.write(bio+"\t"+entrez+"\t"+entrez_bait+"\t"+gene+"\t"+gene_bait+"\t"+description+"\t"+description_bait+"\t"+d[gene][0]+"\t"+d[gene][1]+"\thttp://www.orpha.net/consor/cgi-bin/Disease_Search_Simple.php?lng=EN&Disease_Disease_Search_diseaseGroup="+d[gene][0]+"&Disease_Disease_Search_diseaseType=ORPHA\n")

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
