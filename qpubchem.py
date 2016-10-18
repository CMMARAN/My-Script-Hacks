from collections import defaultdict	
import pubchempy as pcp

def qpubchem(l):
	ldic = {}
	c = pcp.Compound.from_cid(l)
	ldic['PubchemID'] = l
	ldic['IUPAC'] = c.iupac_name
	ldic['SMILES'] = c.isomeric_smiles
	ldic['InChI'] = c.inchi
	return ldic 

def chemquery(lst):
	if isinstance(lst, list):
		lstl = []
		for l in lst:
			ldic = {}
			ldic = qpubchem(l)
			lstl.append(ldic)
		return lstl
	elif isinstance(lst, str):
		ldic = {}
		ldic = qpubchem(lst)
		return ldic
	else:
		print("Please give Correct input")
