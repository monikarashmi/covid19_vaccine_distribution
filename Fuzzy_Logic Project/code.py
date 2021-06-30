import pandas as pd
import numpy as np
import pandas_dedupe
scholar=pd.read_csv(r'C:\Users\monik\OneDrive\Desktop\Fuzzy_Logic Project\Scholar.csv')
Dblp=pd.read_csv(r'C:\Users\monik\OneDrive\Desktop\Fuzzy_Logic Project\DBLP1.csv')
scholar['title_format'] = scholar['title'].map(lambda x: str(x))
print(scholar)

#Scholar_final=pandas_dedupe.dedupe_dataframe(scholar,['idScholar','ROW_ID'])
#Scholar_final['ROW_ID']= Scholar_final['ROW_ID'].str.replace('[^\w\s.-(),:/\\]','')
#Scholar_final.to_csv('deduplication_output.csv')
#print(deduplication_output)