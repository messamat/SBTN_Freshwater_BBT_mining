import asyncio
import httpx
import numpy as np
import os
from pathlib import Path
import pandas as pd
import time

#Set up project directory structure
rootdir = os.getcwd() #os.path.dirname(os.getcwd())
datdir = Path(rootdir, "data")
resdir = Path(rootdir, "results")
srcdir = Path(rootdir, 'src')

#Import table detailing OpenAlex categories to include in search
oa_cattab = pd.read_excel(
    Path(datdir, 'openalex_categories_toinclude.xlsx')
)
#Keep only categories ot include
cats_to_include = oa_cattab[oa_cattab['Include?'] == 'Y'].\
    reset_index()

cats_idarray = np.asarray(cats_to_include['openalex_id'])


import requests

#Get maximum

x = requests.get(f"https://api.openalex.org/works?filter=concept.id:{cats_idarray[1]}", verify=False)
x.json()['meta']['count']

#Get number of records
#Use cursor paging
"https://api.openalex.org/works?filter=publication_year:2020&per-page=100&cursor=*" #Example cursor
#The response to your query will include a next_cursor value in the response's meta object
#To retrieve the next page of results, copy the meta.next_cursor value into the cursor field of your next request.
"https://api.openalex.org/works?filter=publication_year:2020&per-page=100&cursor=IlsxNjA5MzcyODAwMDAwLCAnaHR0cHM6Ly9vcGVuYWxleC5vcmcvVzI0ODg0OTk3NjQnXSI="

#mailto=you@example.com




&page=1&per-page=20'

for x in range(10):
    result = {}
    for y in search['results'][x].keys():
        result[y] = search['results'][x][y]
    resultlist.append(result)

t0 = time.time()
async with httpx.AsyncClient() as client:
    r = client.get(f"https://api.openalex.org/works?filter=concept.id:{cats_idarray[1]}")

    r = [client.get(f"https://api.openalex.org/works?filter=concept.id:{i}") for i in cats_idarray[0:2]]
    s = await asyncio.gather(*r)


    r = [client.get(f"https://api.openalex.org/works?filter=concept.id:{i}") for i in x3]


t1 = time.time()
print(t1-t0)

for i in s:
    print(i)
    try:
        print(i.json()['meta']['count'])
    except:

