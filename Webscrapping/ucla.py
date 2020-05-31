# -*- coding: utf-8 -*-
"""
Created on Sun May 24 21:32:55 2020

@author: jiashanwu
"""

# import the link
html = links.iloc[11,3]

# read the content of the placement website
raw_html = simple_get(html)
html = BeautifulSoup(raw_html, 'html.parser')

# store the year and placement info
names = []
year = []
fileds = []
placement = []

s = str(html)

srt, end = 'class="name">', '\n'
names = find_pattern(s, srt, end)
names = [i.replace('\t', ' ').replace('</td>', '') for i in names]

srt, end = '<td>', '\r'
placement = find_pattern(s, srt, end)

srt, end = '"headline">', '<div class="special-heading-border">'
year = find_pattern(s, srt, end)

name_year = assign_year(s, names, year)

tmp = [[name_year[i], names[i], placement[i]] for i in range(len(name_year))]
tmp = pd.DataFrame(tmp)
tmp.columns = ['Year', 'Name', 'Placement']
tmp['Year'] = tmp['Year'].str.slice(0,4)
ucla = tmp

ucla.head()