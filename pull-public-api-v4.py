import requests
import csv
# importing flask
from flask import Flask, render_template
  
# importing pandas module
import pandas as pd


response = requests.get('https://api.github.com/search/repositories?q=fun+python&s=stars')
jsonout=response.json()

repo_id=jsonout["items"][0]["id"]
print(jsonout["items"][0]["id"])

print(jsonout["items"][0]["full_name"])
print(jsonout["items"][0]["url"])

#Saving to dataframe
#df = pd.DataFrame(columns=["repo_id"])

outdata =[]
csvheader=["full_name","url","star"]
for x in jsonout['items']:
    listing =[x["full_name"],x["html_url"],x["stargazers_count"]]
    outdata.append(listing)
df=pd.DataFrame(outdata)
print(df)
