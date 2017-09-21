from biomart import BiomartServer

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
    'refseq_mrna': ['NM_022914']
},
'attributes': [
    'external_gene_name', 'description'
]
})

for line in response.iter_lines():
	line = line.decode('utf-8')
	print(line.split("\t"))