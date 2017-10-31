
[![Maintainability](https://api.codeclimate.com/v1/badges/6832006699f8d97efe23/maintainability)](https://codeclimate.com/github/fbidu/orpha-tools/maintainability)

# ORPHATOOLS

This tools was developed with the intention to crossing data from Orphanet, Prolexys and Biogrid to find proteins-protein interaction from genes related to rare disease.


## Command line to run the software
To run this tools you will need to have python3 installed and have access to orphanet rare disease XML file, Biogrid database file with protein-protein interaction and Prolexys database with protein-protein interaction file.

`python3.6 main.py --xml sample_data/01/en_product6.xml --hyb_db sample_data/01/prolexys_y2h_bait_oriented.txt --biogrid sample_data/01/BIOGRID-ORGANISM-Homo_sapiens-3.4.152.tab2.txt --output sample_data/01/prolexys_y2h_bait_oriented_orpha_biogrid.txt`