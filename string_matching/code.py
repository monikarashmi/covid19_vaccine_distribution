import pandas as pd



import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
dblp1=pd.read_csv(r'C:\Users\monik\OneDrive\Desktop\work\git_repo\string_matching\DBLP1.csv')
print(dblp1)
#cleaning of data(removing duplicates)
#dblp1.isnull()
#print(dblp1)
#dblp_unique=dblp1.drop_duplicates()
#print(dblp_unique)
#scholar=pd.read_csv(r'C:\Users\monik\OneDrive\Desktop\work\git_repo\string_matching\Scholar.csv')
#cleaning data(removing duplicates)
#scholar_unique=scholar.drop_duplicates()
#scholar.isnull()
#print(scholar)
#print(scholar_unique)

#idDBLP=dblp_unique['idDBLP'].tolist()
#DBLP_Match=dblp_unique['Row_ID'].tolist()
#print(DBLP_Match)

