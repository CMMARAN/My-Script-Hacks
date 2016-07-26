import glob
import os
import time
start_time = time.time()
lst = ['GDS1nnn','GDS2nnn','GDS3nnn','GDS4nnn','GDS5nnn','GDSnnn']
url = 'ftp://ftp.ncbi.nlm.nih.gov/geo/datasets/'
ltx = []
for i in lst:
	ind = i.replace('nnn','')
	url1 = url+i
	for g in range(1,1001):
		st1 = str("000")+str(g)
		print(str(url1)+"/"+ind+str(st1[-3:])+"/soft/"+ind+str(st1[-3:])+"_full.soft.gz")
		lt = (str(url1)+"/"+ind+str(st1[-3:])+"/soft/"+ind+str(st1[-3:])+"_full.soft.gz")	
		lx = 'wget '+lt
		os.system(lx)
print("--- %s seconds ---" % (time.time() - start_time))
