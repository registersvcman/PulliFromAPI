import pandas as pd
import requests
import csv


response = requests.get('https://api.github.com/search/repositories?q=fun+python&s=stars')
jsonout=response.json()
outdata =[]
csvheader=["full_name","url","star"]
for x in jsonout['items']:
    listing =[x["full_name"],x["html_url"],x["stargazers_count"]]
    outdata.append(listing)

with open("repo.csv","w",encoding="UTF8",newline='') as f:
    writer= csv.writer(f)
    writer.writerow(csvheader) 
    writer.writerows(outdata)
#print( outdata)
#print(jsonout['items'])
