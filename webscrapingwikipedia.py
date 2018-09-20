
import pandas as pd
import wikipedia as wp
 
 
#Website I used to extract the data: https://en.wikipedia.org/wiki/List_of_states_of_Mexico
#Get the html source
html = wp.page("List of states of Mexico").html()
df = pd.read_html(html)[0]
#Use encoding='iso-8859-1'for accented characters
df.to_csv('mexicostates3.csv',encoding='iso-8859-1')
print (df)
