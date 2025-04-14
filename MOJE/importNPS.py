from google.cloud import bigquery
import os
from datetime import date 
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/radoslaw/Desktop/pol-it-pol9012318-2021052100-2f30a8d31977.json"

client = bigquery.Client(project="pol-it-pol9012318-2021052100")

query = """
    SELECT distinct E_Mail
    FROM `pol-it-pol9012318-2021052100.RADEK2.NPS`
"""

today=date.today()

query_job = client.query(query)


with open(f'/Users/radoslaw/desktop/NPS/NPS{today}.csv','w',encoding='UTF-8') as plik:
    plik.write('E_Mail')
    for i in query_job:
        plik.write('\n')
        plik.write(i[0])
