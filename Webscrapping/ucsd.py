# -*- coding: utf-8 -*-
"""
Created on Sun May 24 21:33:50 2020

@author: jiashanwu
"""

# import the link
html = links.iloc[12,3]

# read the content of the placement website
raw_html = simple_get(html)
html = BeautifulSoup(raw_html, 'html.parser')

# store the year and placement info
names = []
year = []
fileds = []
placement = []

s = str(html)

srt, end = '\n<li>', '</li>\n'
placement = find_pattern(s, srt, end)
placement = [i for i in placement if i[0:2] != '<a']
placement = placement[1:]

srt, end = '<a href="#">', '</a>'
year = find_pattern(s, srt, end)

name_year = assign_year(s, placement, year)
names = [None] * len(name_year)

tmp = [[name_year[i], names[i], placement[i]] for i in range(len(name_year))]
tmp = pd.DataFrame(tmp)
tmp.columns = ['Year', 'Name', 'Placement']
tmp['Year'] = tmp['Year'].str.slice(0,2) + tmp['Year'].str.slice(5,7)
ucsd = tmp

ucsd.head()