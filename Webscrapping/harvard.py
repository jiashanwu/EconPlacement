# -*- coding: utf-8 -*-
"""
Created on Sun May 24 19:56:11 2020

@author: jiashanwu
"""

# import the link
html = links.iloc[0,3]

# read the content of the placement website
raw_html = simple_get(html)
html = BeautifulSoup(raw_html, 'html.parser')

# store the year and placement info
year = []
placement = []

for i, p in enumerate(html.select('h3')):
    year.append(p.text)
    
for i, p in enumerate(html.select('tr')):
    placement.append(p.text)
    
# the idx identifies the starting of a new cohort
idx = [idx for idx,val in enumerate(placement) if 'Name' in val]
# assert len(idx)==len(year)

tmp = placement.copy()
tmp = [i for j,i in enumerate(tmp) if j not in idx]
tmp = [w.replace('\n\t\t\t\t','') for w in tmp]
tmp = [w.replace('\n\t\t\t\n',';') for w in tmp]
tmp = [w.replace('\n\n','\n') for w in tmp]
tmp = [w.replace('\n',';') for w in tmp]
tmp = [w.split(';') for w in tmp]
harvard = pd.DataFrame(tmp)

idx = [idx[i] - i for i in range(len(idx))]

# assign year values
harvard['year'] = int(max(year))
for i in range(len(idx)-1):
    harvard.loc[idx[i] :(idx[i+1] - 1), 'year'] = int(max(year)) - i 
    
harvard.loc[idx[i + 1]:len(harvard['year']), 'year'] = int(max(year)) - i - 1
harvard = harvard.iloc[:,[0,2,5]]
harvard.columns = ['Name','Placement','Year']

harvard.head()