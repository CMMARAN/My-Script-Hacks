# My-Script-Hacks
pullgeodata-v1.py
Python script to download all GEO datasets from NCBI-GEO website. Script will also print the time taken to download all datasets.
qpubchem.py
Python script to fetch compound information from PubChem through API. It contains functions listed below:
1. def qpubchem(l):
Function returns dictionary of information of compound-id, l. The Dictionary contains 
IUPAC NAME, 
SMILES (Isomeric Smiles)
InChI Key
2. def chemquery(lst):
Function returns list of dictionaries ( containing IUPAC, SMILES, InChI) for given input of compound ids.
