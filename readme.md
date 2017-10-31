
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/418485fe863f40c89cc182b00ebb93b5/badge.svg)](https://www.quantifiedcode.com/app/project/418485fe863f40c89cc182b00ebb93b5)

# ORPHATOOLS

This tools was developed with the intention to crossing data from Orphanet, Prolexys and Biogrid to find proteins-protein interaction from genes related to rare disease.

## Getting Started

To run this tools you will need to have python3 installed and have access to orphanet rare disease XML file, Biogrid database file with protein-protein interaction and Prolexys database with protein-protein interaction file.

### Running

```
python3 main.py --xml en_product6.xml --hyb_db prolexys_y2h_bait_oriented.txt --biogrid ./BIOGRID-ORGANISM-Homo_sapiens-3.4.152.tab2.txt --output prolexys_y2h_bait_oriented_orpha_biogrid.txt
```
