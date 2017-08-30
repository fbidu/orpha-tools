# -*- encoding: utf-8 -*-
import argparse
import utils


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input')
    ap.add_argument('--out')
    args = ap.parse_args()

    lines_list = open(args.input).read().splitlines()
    print(lines_list)
   # for i in range(0, len(lines_list)):
   # 	tmp_list = lines_list[i:(i+100)]
   # 	i=i+100

    gene_symbol_list = utils.convert_refseq_to_gene_symbol(lines_list)
    bla = [x.decode('utf-8') for x in gene_symbol_list.iter_lines()]
    print('\n'.join(bla))
    
    # for line in gene_symbol_list.iter_lines():
    #     line = line.decode('utf-8')
    #     gene = line.split("\t")[0]
    #     description = line.split("\t")[1]

    #     html_text=utils.search_orphanet(gene)
    #     result=utils.get_first_result(html_text)
    #     if result != '':
    #     	teste=''.join([linha.strip() for linha in result.strip().splitlines()])
    #     	print(gene+"\t"+description+"\thttp://www.orpha.net/consor/cgi-bin/"+teste)

    #        html_text=utils.search_orphanet(gene)
#            result=utils.get_first_result(html_text)
#            if result != '':
#                teste=''.join([linha.strip() for linha in result.strip().splitlines()])
#                print(gene+"\thttp://www.orpha.net/consor/cgi-bin/"+teste)

if __name__ == '__main__':
    main()
