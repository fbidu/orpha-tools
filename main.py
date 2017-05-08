# -*- encoding: utf-8 -*-

import utils


def main():
    with open('./kinases.txt') as f:
        for line in f:
            gene=line.rstrip()
            html_text=utils.search_orphanet(gene)
            result=utils.get_first_result(html_text)
            if result != '':
                teste=''.join([linha.strip() for linha in result.strip().splitlines()])
                print(gene+"\thttp://www.orpha.net/consor/cgi-bin/"+teste)

if __name__ == '__main__':
    main()
