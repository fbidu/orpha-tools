# -*- encoding: utf-8 -*-
"""
The main module
"""
import argparse
import utils

def main():

    orpha_genes = {}
    hyb_db = {} 
    hyb_db_gene = {}
    hyb_db_annotation = {}
    biogrid_db = {}

    ap = argparse.ArgumentParser()
    ap.add_argument('--xml')
    ap.add_argument('--hyb_db')
    ap.add_argument('--biogrid')
    ap.add_argument('--output')
    args = ap.parse_args()

    orpha_genes = utils.load_orpha_genes(args.xml)

    hyb_db = utils.load_hyb_db_genes(args.hyb_db)

    biogrid_db = utils.load_biogrid_genes(args.biogrid)

    i = 0
    hyb_db_list = sorted(hyb_db.keys())
    while i <= len(hyb_db):
        uplimit = i+500
        if uplimit > len(hyb_db_list):
            uplimit = len(hyb_db_list)
    	
        tmp_list = hyb_db_list[i:uplimit]
        gene_symbol_list = utils.convert_entrez_to_gene_symbol(tmp_list)
        i=i+500
        print(str(i))
        for line in gene_symbol_list.iter_lines():
            line = line.decode('utf-8')
            gene = line.split("\t")[0]
            description = line.split("\t")[1]
            entrez = line.split("\t")[2]
            hyb_db_gene[entrez] = hyb_db[entrez]
            hyb_db_annotation[entrez] = [gene,description]
    
    output = open(args.output, 'w')

    for entrez in hyb_db_gene:
        bio = ""
        if hyb_db_gene[entrez][1] in orpha_genes:
            for hyb_inter in hyb_db_gene[entrez]:
                if entrez in biogrid_db:
                    for biogrid_inter in biogrid_db[entrez]:
                        if hyb_inter == biogrid_inter:
                            bio = "*"
                            break
                output.write(bio +"\t")
                output.write(entrez+"\t")
                output.write(hyb_inter+"\t")
                output.write(hyb_db_annotation[entrez][0]+"\t")
                if hyb_inter in hyb_db_annotation:
                    output.write(hyb_db_annotation[hyb_inter][0]+"\t")
                else:
                    output.write("No hit\t")
                output.write(hyb_db_annotation[entrez][1]+"\t")
                if hyb_inter in hyb_db_annotation:
                    output.write(hyb_db_annotation[hyb_inter][1]+"\t")
                else:
                    output.write("No hit\t")  
                output.write(orpha_genes[hyb_db_annotation[entrez][0]][0]+"\t")
                output.write(orpha_genes[hyb_db_annotation[entrez][0]][1]+"\thttp://www.orpha.net/consor/cgi-bin/Disease_Search_Simple.php?lng=EN&Disease_Disease_Search_diseaseGroup="+orpha_genes[hyb_db_annotation[entrez][0]][0]+"&Disease_Disease_Search_diseaseType=ORPHA\n")
    
    output.close()

if __name__ == '__main__':
    main()
